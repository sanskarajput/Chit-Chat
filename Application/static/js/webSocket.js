const socket = new WebSocket(`ws://${window.location.host}/ws/conversation/${current_user_id}/${other_user_id}`);

const allMessages = [];

const chatMessages = document.getElementById('chatMessages');
const messageInput = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');
const emojiBtn = document.getElementById('emojiBtn');

socket.onopen = (e) => {
    console.log('WebSocket connectioned successfully');
    }

socket.onmessage = (e) => {
    const data = JSON.parse(e.data);
    const message = data.message;
    // console.log(message);
    if (typeof(message) == 'object') {
        appendMessage(message.content,message.sender,message.timestamp);
    }
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

function sendMessage() {
    const text = messageInput.value.trim();
    
    if (text) {
        const message = {
            message: text,
            sender_id: current_user_id
        };

        // Send the message via WebSocket
        socket.send(JSON.stringify(message));

        messageInput.value = '';

    }
}




function appendMessage(text, sender, timestamp) {
    allMessages.push({ text, sender, timestamp });
    renderMessages();  // Re-render the messages
}

function renderMessages() {
    // Clear existing messages
    chatMessages.innerHTML = '';

    // Display all messages
    allMessages.forEach(message => {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', message.sender === current_user_id ? 'sent' : 'received');

        const messageContent = document.createElement('div');
        messageContent.innerHTML = message.text;

        const timeSpan = document.createElement('div');
        timeSpan.textContent = timeAgo(message.timestamp);
        timeSpan.style.fontSize = '0.75rem';
        timeSpan.style.opacity = '0.7';
        timeSpan.style.marginTop = '0.25rem';
        timeSpan.style.textAlign = 'end';

        messageDiv.appendChild(messageContent);
        messageDiv.appendChild(timeSpan);

        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    });
}


function timeAgo(timestamp) {
    const now = new Date();
    const diff = (now - new Date(timestamp)) / 1000; // Difference in seconds

    if (diff < 60) {
        return "just now";
    } else if (diff < 3600) {
        const minutes = Math.floor(diff / 60);
        return `${minutes} ${minutes === 1 ? "min" : "mins"} ago`;
    } else if (diff < 86400) {
        const hours = Math.floor(diff / 3600);
        return `${hours} ${hours === 1 ? "hour" : "hours"} ago`;
    } else {
        const days = Math.floor(diff / 86400);
        return days === 1
            ? "yesterday"
            : new Date(timestamp).toLocaleDateString(); // Returns date for older timestamps
    }
}