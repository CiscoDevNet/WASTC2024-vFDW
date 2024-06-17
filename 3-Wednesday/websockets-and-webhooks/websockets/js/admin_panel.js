const ws = new WebSocket('ws://localhost:6789/admin');

ws.addEventListener('message', function (event) {
    const data = JSON.parse(event.data);
    console.log('Message received:', data); // Debugging log
    switch (data.type) {
        case 'stats':
            document.getElementById('connectedClients').textContent = data.data.connected_clients;
            document.getElementById('totalMessages').textContent = data.data.total_messages;
            break;
        case 'client_list':
            displayClientList(data.data);
            break;
        case 'message_history':
            displayMessageHistory(data.data);
            break;
    }
});

document.getElementById('showClients').addEventListener('click', function() {
    console.log('Show Clients button clicked'); // Debugging log
    const clientListContainer = document.getElementById('clientList');
    if (clientListContainer.style.display === 'none' || clientListContainer.style.display === '') {
        ws.send(JSON.stringify({ action: 'get_clients' }));
    } else {
        clientListContainer.style.display = 'none';
    }
});

document.getElementById('showMessages').addEventListener('click', function() {
    console.log('Show Messages button clicked'); // Debugging log
    const messageHistoryContainer = document.getElementById('messageHistory');
    if (messageHistoryContainer.style.display === 'none' || messageHistoryContainer.style.display === '') {
        ws.send(JSON.stringify({ action: 'get_messages' }));
    } else {
        messageHistoryContainer.style.display = 'none';
    }
});

function displayClientList(clientList) {
    const clientListContainer = document.getElementById('clientList');
    clientListContainer.innerHTML = clientList.map(name => `<p>${name}</p>`).join('');
    clientListContainer.style.display = 'block';
}

function displayMessageHistory(messages) {
    const messageHistoryContainer = document.getElementById('messageHistory');
    messageHistoryContainer.innerHTML = messages.map(
        ([clientName, message]) => `<p><b>${clientName}:</b> ${message}</p>`
    ).join('');
    messageHistoryContainer.style.display = 'block';
}

ws.addEventListener('open', function(event) {
    console.log('WebSocket connection established'); // Debugging log
});

ws.addEventListener('close', function(event) {
    console.log('WebSocket connection closed', event);
});

ws.addEventListener('error', function(event) {
    console.error('WebSocket error observed:', event);
});
