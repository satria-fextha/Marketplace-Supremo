import { useState } from 'react';


const Filtro = () => {
    const [busqueda, setBusqueda] = useState('');
    const [filtro, setFiltro] = useState('');

    const handleBusqueda = (event) => {
        setBusqueda(event.target.value);
        // Aquí puedes implementar la lógica para manejar la consulta de búsqueda
    };

    const handleFiltro = (event) => {
        setFiltro(event.target.value);
        // Aquí puedes implementar la lógica para aplicar filtros a los resultados de búsqueda
    };

    return (
        <div>
            <input type="text" value={busqueda} onChange={handleBusqueda} placeholder="Buscar productos" />
            <select value={filtro} onChange={handleFiltro}>
                <option value="">Todos los productos</option>
                <option value="categoria1">Categoría 1</option>
                <option value="categoria2">Categoría 2</option>
                <option value="categoria3">Categoría 3</option>
            </select>
        </div>
    );
};

export default Filtro;