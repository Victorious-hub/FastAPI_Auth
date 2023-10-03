import './App.css';
import { Link, useNavigate, BrowserRouter as Router, Route, Routes, NavLink } from "react-router-dom";
import { useState } from "react";
import axios from 'axios';
import Register from "./components/Register";

function App() {
    return (
        <Router>
            <Routes>
                <Route exact path="/register" element={<Register />} />
            </Routes>
        </Router>
    );
}

export default App;