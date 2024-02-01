import React, { useState } from 'react';

const FormularioPerfil = () => {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [bio, setBio] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Handle form submission logic here
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Name:
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
            </label>
            <label>
                Email:
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
            </label>
            <label>
                Bio:
                <textarea value={bio} onChange={(e) => setBio(e.target.value)} />
            </label>
            <button type="submit">Save</button>
        </form>
    );
};

export default FormularioPerfil;
