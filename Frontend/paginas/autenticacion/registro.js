
// Import necessary modules
import React, { useState } from 'react';

// Define RegistrationForm component
const RegistrationForm = () => {
    // State variables for form fields
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    // Handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();

        // Perform client-side validation
        if (!name || !email || !password) {
            alert('Please fill in all fields');
            return;
        }

        // Perform registration logic
        // ...

        // Clear form fields
        setName('');
        setEmail('');
        setPassword('');
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
                Password:
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            </label>
            <button type="submit">Register</button>
        </form>
    );
};

export default RegistrationForm;

