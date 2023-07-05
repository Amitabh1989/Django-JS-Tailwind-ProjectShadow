import './App.css';
import './css/navbar.css';
import Navbar from './components/Navbar';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  // Link,
} from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path='/' />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
