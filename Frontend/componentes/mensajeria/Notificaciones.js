import React, { useState, useEffect } from 'react';

const Notificaciones = () => {
    const [notificaciones, setNotificaciones] = useState([]);

    useEffect(() => {
        // Lógica para obtener las notificaciones de nuevos mensajes
        const obtenerNotificaciones = async () => {
            try {
                const response = await fetch('/api/notificaciones'); // Endpoint para obtener las notificaciones
                const data = await response.json();
                setNotificaciones(data);
            } catch (error) {
                console.error('Error al obtener las notificaciones:', error);
            }
        };

        obtenerNotificaciones();

        // Establecer una conexión en tiempo real para recibir nuevas notificaciones
        const socket = new WebSocket('wss://tu-servidor-websocket.com');

        socket.addEventListener('message', (event) => {
            const nuevaNotificacion = JSON.parse(event.data);
            setNotificaciones((prevNotificaciones) => [...prevNotificaciones, nuevaNotificacion]);
        });

        // Limpiar la conexión al desmontar el componente
        return () => {
            socket.close();
        };
    }, []);

    return (
        <div>
            <h2>Notificaciones</h2>
            {notificaciones.map((notificacion) => (
                <div key={notificacion.id}>{notificacion.mensaje}</div>
            ))}
        </div>
    );
};

export default Notificaciones;