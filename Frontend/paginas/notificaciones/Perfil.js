import React, { useState, useEffect } from 'react';

const Perfil = () => {
    const [notificaciones, setNotificaciones] = useState([]);

    useEffect(() => {
        // Lógica para obtener las notificaciones del usuario
        // Puedes hacer una llamada a la API o utilizar datos de prueba
        const obtenerNotificaciones = async () => {
            try {
                const response = await fetch('/api/notificaciones');
                const data = await response.json();
                setNotificaciones(data);
            } catch (error) {
                console.error('Error al obtener las notificaciones:', error);
            }
        };

        obtenerNotificaciones();
    }, []);

    const marcarComoLeida = (id) => {
        // Lógica para marcar una notificación como leída
        // Puedes hacer una llamada a la API o actualizar el estado localmente
        // Aquí solo se muestra un ejemplo de cómo actualizar el estado localmente
        setNotificaciones((prevNotificaciones) =>
            prevNotificaciones.map((notificacion) =>
                notificacion.id === id ? { ...notificacion, leida: true } : notificacion
            )
        );
    };

    const eliminarNotificacion = (id) => {
        // Lógica para eliminar una notificación
        // Puedes hacer una llamada a la API o actualizar el estado localmente
        // Aquí solo se muestra un ejemplo de cómo actualizar el estado localmente
        setNotificaciones((prevNotificaciones) =>
            prevNotificaciones.filter((notificacion) => notificacion.id !== id)
        );
    };

    return (
        <div>
            <h1>Perfil</h1>
            <h2>Notificaciones</h2>
            {notificaciones.length === 0 ? (
                <p>No tienes notificaciones.</p>
            ) : (
                <ul>
                    {notificaciones.map((notificacion) => (
                        <li key={notificacion.id}>
                            {notificacion.mensaje}
                            {!notificacion.leida && (
                                <button onClick={() => marcarComoLeida(notificacion.id)}>
                                    Marcar como leída
                                </button>
                            )}
                            <button onClick={() => eliminarNotificacion(notificacion.id)}>
                                Eliminar
                            </button>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default Perfil;