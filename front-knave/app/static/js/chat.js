document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const messageInput = document.getElementById('message-input');
    const chatMessages = document.getElementById('chat-messages');
    
    // Generar un sessionID único
    const sessionID = crypto.randomUUID();
    console.log('Nueva sesión iniciada con ID:', sessionID);
    
    function addMessage(message, isUser = true) {
        const messageElement = document.createElement('div');
        messageElement.className = `message ${isUser ? 'user-message' : 'system-message'}`;
        messageElement.textContent = message;
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    async function sendToWebhook(message) {
        try {
            const response = await fetch('/webhook', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    message: message,
                    action: 'chat',
                    sessionID: sessionID
                })
            });
            
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || `Error: ${response.status} ${response.statusText}`);
            }
            
            return data;
        } catch (error) {
            console.error('Error:', error);
            throw error;
        }
    }
    
    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const message = messageInput.value.trim();
        if (!message) return;

        // Mostrar el mensaje del usuario
        addMessage(message, true);
        messageInput.value = '';

        try {
            // Enviar mensaje al webhook y mostrar la respuesta
            const response = await sendToWebhook(message);

            if (response.error) {
                addMessage(`Error: ${response.error}`, false);
            } else if (Array.isArray(response.messages)) {
                response.messages.forEach(msg => addMessage(msg, false));
            } else if (typeof response.message === 'string') {
                addMessage(response.message, false);
            } else if (typeof response === 'object') {
                for (const [key, value] of Object.entries(response)) {
                    if (typeof value === 'string') {
                        addMessage(`${key}: ${value}`, false);
                    }
                }
            } else {
                addMessage('Respuesta desconocida del servidor.', false);
            }
        } catch (error) {
            addMessage(`Error al enviar el mensaje: ${error.message}`, false);
        }
    });
    
    // Mensaje de bienvenida
    addMessage('¡Bienvenido a Knave! ¿En qué puedo ayudarte?', false);
}); 