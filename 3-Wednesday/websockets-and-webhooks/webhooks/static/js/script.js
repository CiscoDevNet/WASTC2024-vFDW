document.addEventListener("DOMContentLoaded", function() {
    fetch('/webhook-data')
        .then(response => response.json())
        .then(data => {
            const dataContainer = document.getElementById('webhook-data');
            dataContainer.innerHTML = '';

            if (data.length === 0) {
                const noDataMessage = document.createElement('p');
                noDataMessage.className = 'no-data';
                noDataMessage.textContent = 'No webhook data received yet.';
                dataContainer.appendChild(noDataMessage);
            } else {
                data.forEach(event => {
                    const eventDiv = document.createElement('div');
                    eventDiv.className = 'webhook-event';

                    const eventHeader = document.createElement('h3');
                    eventHeader.textContent = `Event: ${event.event}`;
                    eventDiv.appendChild(eventHeader);

                    const eventId = document.createElement('p');
                    eventId.innerHTML = `<span>ID:</span> ${event.data.id}`;
                    eventDiv.appendChild(eventId);

                    const eventMessage = document.createElement('p');
                    eventMessage.innerHTML = `<span>Message:</span> ${event.data.message}`;
                    eventDiv.appendChild(eventMessage);

                    dataContainer.appendChild(eventDiv);
                });
            }
        })
        .catch(error => console.error('Error fetching webhook data:', error));
});
