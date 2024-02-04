import React, { useState } from 'react';

const Producto = () => {
    const [calificacion, setCalificacion] = useState(0);
    const [resena, setResena] = useState('');

    const handleCalificacionChange = (event) => {
        setCalificacion(event.target.value);
    };

    const handleResenaChange = (event) => {
        setResena(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        // Aquí puedes enviar la calificación y reseña al servidor para su procesamiento
        // Por ejemplo, puedes hacer una solicitud HTTP POST utilizando fetch o axios
        // y enviar los datos al backend para guardarlos en la base de datos

        // Después de enviar los datos, puedes actualizar la interfaz para mostrar la calificación y reseña enviadas
    };

    return (
        <div>
            <h2>Calificar Producto</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Calificación:
                    <input type="number" min="1" max="5" value={calificacion} onChange={handleCalificacionChange} />
                </label>
                <br />
                <label>
                    Reseña:
                    <textarea value={resena} onChange={handleResenaChange} />
                </label>
                <br />
                <button type="submit">Enviar Calificación</button>
            </form>
        </div>
    );
};

export default Producto;