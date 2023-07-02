import React, { Component } from 'react';
import axios from 'axios';

class FormulationComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {
            formulations: [],
            rawMaterials: [],
            newFormulation: {
                rawMaterials: [],
                quantities: []
            }
        };
    }

    componentDidMount() {
        this.getFormulations();
        this.getRawMaterials();
    }

    getFormulations = () => {
        axios.get('/api/formulations/')
            .then(res => {
                this.setState({ formulations: res.data });
            })
            .catch(err => console.log(err));
    }

    getRawMaterials = () => {
        axios.get('/api/raw_materials/')
            .then(res => {
                this.setState({ rawMaterials: res.data });
            })
            .catch(err => console.log(err));
    }

    handleFormulationChange = (e) => {
        const { name, value } = e.target;
        this.setState(prevState => ({
            newFormulation: {
                ...prevState.newFormulation,
                [name]: value
            }
        }));
    }

    handleFormulationSubmit = (e) => {
        e.preventDefault();
        axios.post('/api/formulations/', this.state.newFormulation)
            .then(res => {
                this.getFormulations();
                this.setState(prevState => ({
                    newFormulation: {
                        ...prevState.newFormulation,
                        rawMaterials: [],
                        quantities: []
                    }
                }));
            })
            .catch(err => console.log(err));
    }

    render() {
        return (
            <div>
                <h1>Formulations</h1>
                {this.state.formulations.map(formulation => (
                    <div key={formulation.id}>
                        <h2>{formulation.name}</h2>
                        <p>{formulation.description}</p>
                    </div>
                ))}
                <form onSubmit={this.handleFormulationSubmit}>
                    <h2>New Formulation</h2>
                    <label>
                        Raw Materials:
                        <select name="rawMaterials" onChange={this.handleFormulationChange}>
                            {this.state.rawMaterials.map(material => (
                                <option key={material.id} value={material.id}>{material.name}</option>
                            ))}
                        </select>
                    </label>
                    <label>
                        Quantities:
                        <input type="number" name="quantities" onChange={this.handleFormulationChange} />
                    </label>
                    <button type="submit">Create Formulation</button>
                </form>
            </div>
        );
    }
}

export default FormulationComponent;