
import React, { useState } from 'react';

const Perfil = () => {
    const [nombre, setNombre] = useState('');
    const [email, setEmail] = useState('');
    const [telefono, setTelefono] = useState('');

    const handleNombreChange = (e) => {
        setNombre(e.target.value);
    };

    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    };

    const handleTelefonoChange = (e) => {
        setTelefono(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Aquí puedes implementar la lógica para actualizar la información del perfil del usuario
    };

    return (
        <div>
            <h1>Perfil</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Nombre:
                    <input type="text" value={nombre} onChange={handleNombreChange} />
                </label>
                <br />
                <label>
                    Email:
                    <input type="email" value={email} onChange={handleEmailChange} />
                </label>
                <br />
                <label>
                    Teléfono:
                    <input type="tel" value={telefono} onChange={handleTelefonoChange} />
                </label>
                <br />
                <button type="submit">Guardar</button>
            </form>
        </div>
    );
};

export default Perfil;

