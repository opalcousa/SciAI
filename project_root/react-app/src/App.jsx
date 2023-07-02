import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import InventoryComponent from './InventoryComponent';
import ProjectComponent from './ProjectComponent';
import FormulationComponent from './FormulationComponent';
import AIAssistantComponent from './AIAssistantComponent';
import UserInterfaceComponent from './UserInterfaceComponent';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/inventory" component={InventoryComponent} />
        <Route path="/projects" component={ProjectComponent} />
        <Route path="/formulations" component={FormulationComponent} />
        <Route path="/ai-assistant" component={AIAssistantComponent} />
        <Route path="/" component={UserInterfaceComponent} />
      </Switch>
    </Router>
  );
}

export default App;