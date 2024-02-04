import React, { useState } from 'react';

const Carro = () => {
    const [productos, setProductos] = useState([]);

    // Función para agregar un producto al carro
    const agregarProducto = (producto) => {
        setProductos([...productos, producto]);
    };

    // Función para eliminar un producto del carro
    const eliminarProducto = (producto) => {
        const nuevosProductos = productos.filter((p) => p.id !== producto.id);
        setProductos(nuevosProductos);
    };

    // Función para aumentar la cantidad de un producto en el carro
    const aumentarCantidad = (producto) => {
        const nuevosProductos = productos.map((p) => {
            if (p.id === producto.id) {
                return { ...p, cantidad: p.cantidad + 1 };
            }
            return p;
        });
        setProductos(nuevosProductos);
    };

    // Función para disminuir la cantidad de un producto en el carro
    const disminuirCantidad = (producto) => {
        const nuevosProductos = productos.map((p) => {
            if (p.id === producto.id && p.cantidad > 1) {
                return { ...p, cantidad: p.cantidad - 1 };
            }
            return p;
        });
        setProductos(nuevosProductos);
    };

    return (
        <div>
            <h1>Carro de Compras</h1>
            {productos.length === 0 ? (
                <p>No hay productos en el carro.</p>
            ) : (
                <ul>
                    {productos.map((producto) => (
                        <li key={producto.id}>
                            {producto.nombre} - Cantidad: {producto.cantidad}
                            <button onClick={() => aumentarCantidad(producto)}>+</button>
                            <button onClick={() => disminuirCantidad(producto)}>-</button>
                            <button onClick={() => eliminarProducto(producto)}>Eliminar</button>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default Carro;