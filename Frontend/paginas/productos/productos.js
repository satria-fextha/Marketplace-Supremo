import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Products = () => {
    const [products, setProducts] = useState([]);
    const [categories, setCategories] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');
    const [selectedCategory, setSelectedCategory] = useState('');

    useEffect(() => {
        // Fetch products from API
        axios.get('/api/products')
            .then(response => {
                setProducts(response.data);
            })
            .catch(error => {
                console.error('Error fetching products:', error);
            });

        // Fetch categories from API
        axios.get('/api/categories')
            .then(response => {
                setCategories(response.data);
            })
            .catch(error => {
                console.error('Error fetching categories:', error);
            });
    }, []);

    const handleSearch = () => {
        // Perform search based on searchQuery and selectedCategory
        axios.get(`/api/products?search=${searchQuery}&category=${selectedCategory}`)
            .then(response => {
                setProducts(response.data);
            })
            .catch(error => {
                console.error('Error searching products:', error);
            });
    };

    const handleCategoryChange = (event) => {
        setSelectedCategory(event.target.value);
    };

    return (
        <div>
            <input
                type="text"
                value={searchQuery}
                onChange={e => setSearchQuery(e.target.value)}
            />
            <select value={selectedCategory} onChange={handleCategoryChange}>
                <option value="">All Categories</option>
                {categories.map(category => (
                    <option key={category.id} value={category.id}>{category.name}</option>
                ))}
            </select>
            <button onClick={handleSearch}>Search</button>

            <ul>
                {products.map(product => (
                    <li key={product.id}>{product.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default Products;