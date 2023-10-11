import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import axios from 'axios';
import Register from './components/Register';
import UserList from './components/UserList';
import LoginForm from './components/LoginForm';
import UserProfile from './components/UserProfile';

const App = () => {
 
  return (
    <Router>
      <Routes>
        <Route path="/register" element={<Register />} />
        <Route path="/users" element={<UserList />} />
        <Route path="/login" element={<LoginForm />} />
        <Route path="/profile" element={<UserProfile />} />
      </Routes>
    </Router>
  );
};

export default App;