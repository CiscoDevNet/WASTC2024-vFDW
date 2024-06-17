# webhook_processor.py

processed_data = []


def process_webhook(data):
    # Validate and process webhook payload
    print(f"Received webhook payload: {data}")
    processed_data.append(data)
    return {"message": "Webhook processed successfully", "data": data}


def get_processed_data():
    return processed_data
