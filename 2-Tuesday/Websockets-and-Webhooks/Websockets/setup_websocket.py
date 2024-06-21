#!/usr/local/bin/python
import websocket
import threading
import requests
import yaml
import json
import time
import ssl
import sys
import os

from pathlib import Path
from os import path as ospath

# Variables for input and output data
pathConfig = "config.yml"
pathNxosLoginTemplate = "nxosLoginTemplate.json"
pathSubscriptionIds = "subscriptionIds.json"
basePathLogs = "logs/"
basePathOutput = "output/"
loginToken = ""

# Load config file, it is required in multiple follwing functions
with open(pathConfig, "r") as handle:
    config = yaml.full_load(handle)

# Disable warning for APIC Self-Signed Certificate
requests.packages.urllib3.disable_warnings()

# Write Tool logs to local logfile, can be mapped to host volume
# Messages are provided by the calling functions
def writeLog(message):
    Path(basePathLogs).mkdir(parents=True, exist_ok=True)
    logPath = basePathLogs + time.strftime('%Y-%m-%d', time.localtime()) + ".txt"
    timestamp = time.strftime("%d/%m/%Y-%H:%M:%S", time.localtime())

    old_stdout = sys.stdout
    sys.stdout = open(logPath,"a+")
    print(timestamp)
    print(message)
    sys.stdout.close()
    sys.stdout = old_stdout

def outputToFile(message):
    toFile = config['data_output']['toFile']

    baseList = []

    Path(basePathOutput).mkdir(parents=True, exist_ok=True)
    outputPath = basePathOutput + toFile['baseFilename'] + "_" + time.strftime('%Y-%m-%d', time.localtime()) + ".json"

    if ospath.exists(outputPath):
        with open(outputPath, "r") as handle:
            baseList = json.load(handle)

        baseList.append(json.JSONDecoder().decode(message))

    else:
        baseList.append(json.JSONDecoder().decode(message))

    old_stdout = sys.stdout
    sys.stdout = open(outputPath,"w+")
    print(json.dumps(baseList))
    sys.stdout.close()
    sys.stdout = old_stdout

    return True

def nxosLogin():

    with open(pathNxosLoginTemplate, "r") as handle:
        nxosLoginTemplate = json.load(handle)

    nxosLoginTemplate['aaaUser']['attributes']['name'] = config['nxos_login']['username']
    nxosLoginTemplate['aaaUser']['attributes']['pwd'] = config['nxos_login']['password']

    response = requests.post(
            'https://' + config['nxos_login']['address'] + '/api/aaaLogin.json',
            headers = {'Content-Type': 'application/json'},
            data = json.dumps(nxosLoginTemplate),
            verify = False
    )

    responseDict = json.loads(response.text)
    token = responseDict['imdata'][0]['aaaLogin']['attributes']['token']

    message = "NXOS Login successful."
    writeLog(message)

    return token

def subscribe(loginToken):
    subIds = []

    if not config['monitored_objects']:
        response = requests.get(
            "https://" + config['nxos_login']['address'] + "/api/node/class/faultInst.json?subscription=yes",
            headers = {'Cookie': "APIC-cookie=" + loginToken},
            verify = False
        )
        subIds.append(json.loads(response.text)['subscriptionId'])
    else:
        for sub in config['monitored_objects']:
            response = requests.get(
                "https://" + config['nxos_login']['address'] + sub + ".json?subscription=yes",
                headers = {'Cookie': "APIC-cookie=" + loginToken},
                verify = False
            )
            subIds.append(json.loads(response.text)['subscriptionId'])

    message = "Subscription successful. Subscription IDs:\n"
    for subid in subIds:
        message = message + subid + "\n"
    writeLog(message)

    with open(pathSubscriptionIds, "w") as handle:
        json.dump(subIds, handle)

def refresh():

    while True:
        time.sleep(45)

        with open(pathSubscriptionIds, "r") as handle:
            subscriptionIds = json.load(handle)

        loginToken = nxosLogin()

        message = "Subscription Refresh successful. Refreshed subscription IDs: \n"
        for sub in subscriptionIds:
            response = requests.get(
                "https://" + config['nxos_login']['address'] + "/api/subscriptionRefresh.json?id=" + sub,
                headers = {'Cookie': "APIC-cookie=" + loginToken},
                verify = False
            )
            print(response.text)
            if not json.loads(response.text)['imdata']:
                message = message + sub + "; "
            else:
                message = message + "Subscription " + sub + " could not be refreshed.\n"

        writeLog(message)

def on_message(ws, message):
    outputToFile(message)

def on_error(ws, error):
    writeLog(error)

def on_close(ws):
    os.remove(pathSubscriptionIds)
    message = "Socket was closed."
    writeLog(message)

def on_open(ws):
    subscribe(loginToken)

if __name__ == "__main__":
    loginToken = nxosLogin()

    refreshThread = threading.Thread(target=refresh)
    refreshThread.start()

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://" + config['nxos_login']['address'] + "/socket" + loginToken,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close,
                                on_open = on_open)

    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})