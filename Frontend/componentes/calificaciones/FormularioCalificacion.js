import React, { useState } from 'react';

const FormularioCalificacion = () => {
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

        // Aquí puedes enviar la calificación y reseña al servidor
        // utilizando una API o cualquier otro método de tu elección

        // Luego puedes realizar cualquier lógica adicional, como
        // actualizar la lista de calificaciones y reseñas en la página

        // Por último, puedes limpiar los campos del formulario
        setCalificacion(0);
        setResena('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Calificación:
                <input type="number" min="0" max="5" value={calificacion} onChange={handleCalificacionChange} />
            </label>
            <br />
            <label>
                Reseña:
                <textarea value={resena} onChange={handleResenaChange} />
            </label>
            <br />
            <button type="submit">Enviar</button>
        </form>
    );
};

export default FormularioCalificacion;