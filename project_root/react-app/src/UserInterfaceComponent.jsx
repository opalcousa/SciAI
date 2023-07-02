import React, { Component } from 'react';
import InventoryComponent from './InventoryComponent.jsx';
import ProjectComponent from './ProjectComponent.jsx';
import FormulationComponent from './FormulationComponent.jsx';
import AIAssistantComponent from './AIAssistantComponent.jsx';

class UserInterfaceComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {
            rawMaterials: [],
            projects: [],
            formulations: [],
            assistantMessages: [],
        };
    }

    componentDidMount() {
        // Fetch data from Django views and update state
    }

    handleRawMaterialUpdate = (rawMaterials) => {
        this.setState({ rawMaterials });
    }

    handleProjectUpdate = (projects) => {
        this.setState({ projects });
    }

    handleFormulationUpdate = (formulations) => {
        this.setState({ formulations });
    }

    handleAssistantUpdate = (assistantMessages) => {
        this.setState({ assistantMessages });
    }

    render() {
        return (
            <div>
                <InventoryComponent 
                    rawMaterials={this.state.rawMaterials} 
                    onRawMaterialUpdate={this.handleRawMaterialUpdate} 
                />
                <ProjectComponent 
                    projects={this.state.projects} 
                    onProjectUpdate={this.handleProjectUpdate} 
                />
                <FormulationComponent 
                    rawMaterials={this.state.rawMaterials} 
                    formulations={this.state.formulations} 
                    onFormulationUpdate={this.handleFormulationUpdate} 
                />
                <AIAssistantComponent 
                    assistantMessages={this.state.assistantMessages} 
                    onAssistantUpdate={this.handleAssistantUpdate} 
                />
            </div>
        );
    }
}

export default UserInterfaceComponent;