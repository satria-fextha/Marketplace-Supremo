import { useState } from 'react';

const BarraBusqueda = () => {
    const [busqueda, setBusqueda] = useState('');

    const handleBusqueda = (e) => {
        setBusqueda(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Aquí puedes realizar la lógica para manejar la consulta de búsqueda
        // y aplicar los filtros a los resultados de la búsqueda
        console.log('Realizar búsqueda:', busqueda);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" value={busqueda} onChange={handleBusqueda} />
            <button type="submit">Buscar</button>
        </form>
    );
};

export default BarraBusqueda;