// Notificacion.js

import { useState, useEffect } from 'react';

const Notificacion = () => {
    const [notificacion, setNotificacion] = useState('');

    useEffect(() => {
        // Lógica para obtener las notificaciones en tiempo real
        const obtenerNotificaciones = () => {
            // Aquí puedes hacer una llamada a tu API para obtener las notificaciones
            // y luego actualizar el estado de la notificación
            // Ejemplo:
            // const nuevasNotificaciones = await obtenerNotificacionesDeAPI();
            // setNotificacion(nuevasNotificaciones);
        };

        // Llama a la función para obtener las notificaciones cada cierto intervalo de tiempo
        const intervalo = setInterval(obtenerNotificaciones, 5000);

        // Limpia el intervalo cuando el componente se desmonta
        return () => clearInterval(intervalo);
    }, []);

    return (
        <div>
            <h2>Notificaciones</h2>
            <p>{notificacion}</p>
        </div>
    );
};

export default Notificacion;