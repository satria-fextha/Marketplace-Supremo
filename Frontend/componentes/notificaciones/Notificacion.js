import React, { useState, useEffect } from 'react';

const Notificacion = () => {
    const [notificaciones, setNotificaciones] = useState([]);

    useEffect(() => {
        // Aquí puedes realizar una llamada a la API para obtener las notificaciones del usuario
        // y luego actualizar el estado con las notificaciones recibidas
        // Ejemplo:
        fetch('/api/notificaciones')
            .then(response => response.json())
            .then(data => setNotificaciones(data));
    }, []);

    const marcarComoLeida = (id) => {
        // Aquí puedes realizar una llamada a la API para marcar una notificación como leída
        // y luego actualizar el estado para reflejar el cambio
        // Ejemplo:
        fetch(`/api/notificaciones/${id}`, { method: 'PUT', body: JSON.stringify({ leida: true }) })
            .then(response => response.json())
            .then(data => {
                // Actualizar el estado con la notificación marcada como leída
                setNotificaciones(notificaciones.map(notificacion => notificacion.id === id ? { ...notificacion, leida: true } : notificacion));
            });
    };

    const eliminarNotificacion = (id) => {
        // Aquí puedes realizar una llamada a la API para eliminar una notificación
        // y luego actualizar el estado para reflejar el cambio
        // Ejemplo:
        fetch(`/api/notificaciones/${id}`, { method: 'DELETE' })
            .then(response => {
                if (response.ok) {
                    // Eliminar la notificación del estado
                    setNotificaciones(notificaciones.filter(notificacion => notificacion.id !== id));
                }
            });
    };

    return (
        <div>
            <h2>Notificaciones</h2>
            {notificaciones.length === 0 ? (
                <p>No tienes notificaciones.</p>
            ) : (
                <ul>
                    {notificaciones.map(notificacion => (
                        <li key={notificacion.id}>
                            <strong>{notificacion.titulo}</strong>
                            <p>{notificacion.contenido}</p>
                            {!notificacion.leida && (
                                <button onClick={() => marcarComoLeida(notificacion.id)}>Marcar como leída</button>
                            )}
                            <button onClick={() => eliminarNotificacion(notificacion.id)}>Eliminar</button>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default Notificacion;