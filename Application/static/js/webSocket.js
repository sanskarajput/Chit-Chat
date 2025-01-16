const socket = new WebSocket(`ws://${window.location.host}/ws/conversation/${current_user.id}/${other_user.id}`);

const allMessages = [];

const chatMessages = document.getElementById('chatMessages');
const messageInput = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');
const emojiBtn = document.getElementById('emojiBtn');


socket.onmessage = (e) => {
    const data = JSON.parse(e.data);
    console.log('WebSocket connectioned successfully');
    console.log(data);
    // appendMessage(data);
};

socket.onclose = (e) => {
    console.log('WebSocket connection closed');
};

// Add event listeners
sendBtn.addEventListener('click', sendMessage);
messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function appendMessage(text, sent = true, timestamp = getCurrentTime()) {
    allMessages.push({ text, sent, timestamp });
    renderMessages();  // Re-render the messages
}

function renderMessages() {
    // Clear existing messages
    chatMessages.innerHTML = '';

    // Display all messages
    allMessages.forEach(message => {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', message.sent ? 'sent' : 'received');

        const messageContent = document.createElement('div');
        messageContent.innerHTML = message.text;

        const timeSpan = document.createElement('div');
        timeSpan.textContent = message.timestamp;
        timeSpan.style.fontSize = '0.75rem';
        timeSpan.style.opacity = '0.7';
        timeSpan.style.marginTop = '0.25rem';

        messageDiv.appendChild(messageContent);
        messageDiv.appendChild(timeSpan);

        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    });
}

function sendMessage() {
    const text = messageInput.value.trim();
    if (text) {
        const message = {
            message: text,
            sender_id: current_user.id
        };

        // Send the message via WebSocket
        socket.send(JSON.stringify(message));

        appendMessage(text, true);
        messageInput.value = '';
    }
}