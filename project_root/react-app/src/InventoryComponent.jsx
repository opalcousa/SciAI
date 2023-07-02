import React, { Component } from 'react';
import axios from 'axios';

class InventoryComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {
            materials: []
        };
    }

    componentDidMount() {
        this.getMaterials();
    }

    getMaterials() {
        axios.get('/api/materials/')
            .then(response => {
                this.setState({ materials: response.data });
            })
            .catch(error => {
                console.log(error);
            });
    }

    render() {
        return (
            <div>
                <h2>Inventory</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Density</th>
                            <th>Price</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.materials.map(material => (
                            <tr key={material.id}>
                                <td>{material.name}</td>
                                <td>{material.density}</td>
                                <td>{material.price}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        );
    }
}

export default InventoryComponent;