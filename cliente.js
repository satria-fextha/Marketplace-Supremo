const evtSource = new EventSource("/sse/");  // Asegúrate de que la ruta coincida con tu configuración en Django

evtSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    // Actualiza la interfaz de usuario con los datos recibidos
};

evtSource.onerror = (err) => {
    console.error("EventSource failed:", err);
    evtSource.close();  // Cierra la conexión en caso de error
};

// No es necesario cerrar la conexión aquí, ya que en la práctica, la conexión permanecerá abierta hasta que se cierre explícitamente o hasta que ocurra un error.
