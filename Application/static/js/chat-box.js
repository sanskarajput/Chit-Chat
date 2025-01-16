// Sample messages for demonstration
const sampleMessages = [
    { text: "Hey! How are you?", sent: false, timestamp: "10:00 AM" },
    { text: "I'm good, thanks! Really excited about today!", sent: true, timestamp: "10:02 AM" },
    { text: "Pretty good! Working on a new project.", sent: false, timestamp: "10:03 AM" },
    { text: "That sounds interesting! Tell me more about it.", sent: true, timestamp: "10:05 AM" },
];

// DOM Elements
const chatMessages = document.getElementById('chatMessages');
const messageInput = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');
const emojiBtn = document.getElementById('emojiBtn');

// WebSocket connection
let socket;

// Initialize chat
function initializeChat() {
    // Display sample messages initially
    renderMessages();

    // WebSocket connection
    socket = new WebSocket('ws://localhost:8000/ws/chat/1/');  // Update with actual URL (using example room 1)

    // Handle WebSocket events
    socket.onmessage = (e) => {
        const data = JSON.parse(e.data);
        appendMessage(data.message, false, getCurrentTime());
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
}

// Append a message to the chat
function appendMessage(text, sent = true, timestamp = getCurrentTime()) {
    sampleMessages.push({ text, sent, timestamp });
    renderMessages();  // Re-render the messages
}

// Render all messages in the sampleMessages array
function renderMessages() {
    // Clear existing messages
    chatMessages.innerHTML = '';

    // Display all messages
    sampleMessages.forEach(message => {
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

// Get current time in HH:MM format
function getCurrentTime() {
    const now = new Date();
    return now.toLocaleTimeString('en-US', {
        hour: 'numeric',
        minute: '2-digit',
        hour12: true
    });
}

// Send a new message via WebSocket
function sendMessage() {
    const text = messageInput.value.trim();
    if (text) {
        const message = {
            message: text
        };

        // Send the message via WebSocket
        socket.send(JSON.stringify(message));

        appendMessage(text, true);
        messageInput.value = '';
    }
}

// Initialize the chat when the page loads
initializeChat();
