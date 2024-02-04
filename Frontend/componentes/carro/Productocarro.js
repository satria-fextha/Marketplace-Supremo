import React, { useState } from 'react';


const Productocarro = ({ producto, cantidad, onAumentar, onDisminuir, onEliminar }) => {
    const [cantidadProducto, setCantidadProducto] = useState(cantidad);

    const handleAumentar = () => {
        setCantidadProducto(cantidadProducto + 1);
        onAumentar(producto);
    };

    const handleDisminuir = () => {
        if (cantidadProducto > 1) {
            setCantidadProducto(cantidadProducto - 1);
            onDisminuir(producto);
        }
    };

    const handleEliminar = () => {
        onEliminar(producto);
    };

    return (
        <div>
            <h3>{producto.nombre}</h3>
            <p>Precio: {producto.precio}</p>
            <p>Cantidad: {cantidadProducto}</p>
            <button onClick={handleAumentar}>Aumentar</button>
            <button onClick={handleDisminuir}>Disminuir</button>
            <button onClick={handleEliminar}>Eliminar</button>
        </div>
    );
};

export default Productocarro;