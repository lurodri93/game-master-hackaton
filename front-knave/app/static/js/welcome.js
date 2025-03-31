document.addEventListener('DOMContentLoaded', () => {
    const characterForm = document.getElementById('character-form');
    const createCharacterForm = document.getElementById('create-character-form');
    
    // Generar un sessionID único
    const sessionID = crypto.randomUUID();
    console.log('Nueva sesión iniciada con ID:', sessionID);
    
    // Manejar la selección de acción
    window.handleAction = (action) => {
        if (action === 'create') {
            characterForm.classList.remove('hidden');
        } else {
            alert('Esta funcionalidad aún no está disponible.');
        }
    };
    
    // Manejar el envío del formulario
    createCharacterForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const characterName = document.getElementById('character-name').value.trim();
        if (!characterName) return;
        
        try {
            console.log('Enviando petición para crear personaje:', {
                name: characterName,
                sessionID: sessionID
            });
            
            const response = await fetch('/webhook', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    message: characterName,
                    action: 'create',
                    sessionID: sessionID
                })
            });
            
            const data = await response.json();
            console.log('Respuesta del servidor:', data);
            
            if (!response.ok) {
                throw new Error(data.error || `Error al crear el personaje: ${response.status} ${response.statusText}`);
            }
            
            if (data.error) {
                alert(data.error);
            } else if (data.success) {
                alert('¡Personaje creado con éxito!');
                // Aquí podríamos redirigir a la página de juego
                // window.location.href = '/game';
            } else {
                alert(data.message || 'Personaje creado con éxito');
            }
        } catch (error) {
            console.error('Error:', error);
            alert(`Error al crear el personaje: ${error.message}`);
        }
    });
}); 