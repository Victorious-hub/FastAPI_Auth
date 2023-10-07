import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

const Register = () => {
  
  const [username, setUserName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  
  const handleSubmit = event => {
    event.preventDefault();

    fetch(`http://localhost:8000/user/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        id: 1,
        username: username,
        email: email,
        password: password,
      }),
    })
      .then(response => {
        if (response.status === 201) {
          console.log('Title added successfully!');
          // Дополнительные действия при успешном сохранении
        } else {
          console.log('Error:', response.statusText);
          // Дополнительная обработка ошибки
        }
      })
      .catch(error => {
        console.error('Error:', error);
        // Обработка ошибок
      });
  };

  return (
    <div className="form">
      <div className="title">Welcome</div>
      <div className="subtitle">Let's create your account!</div>

      <form onSubmit={handleSubmit}>
        <div className="input-container ic1">
          <input
            id="username"
            name="username"
            className="input"
            type="text"
            placeholder=" "
            value={username}
            onChange={(e) => setUserName(e.target.value)}
          />
          <div className="cut"></div>
          <label htmlFor="username" className="placeholder">
            Username
          </label>
        </div>

        <div className="input-container ic1">
          <input
            id="email"
            name="email"
            className="input"
            type="email"
            placeholder=" "
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <div className="cut"></div>
          <label htmlFor="email" className="placeholder">
            Email
          </label>
        </div>

        <div className="input-container ic8">
          <input
            id="password"
            className="input"
            type="password"
            placeholder=" "
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <div className="cut"></div>
          <label htmlFor="password" className="placeholder">
            Password
          </label>
        </div>

        <button type="submit" className="submit">
          Register
        </button>
      </form>

      <br></br>
      <Link to="/login1" className="have_account">
        Already have an account? Log in
      </Link>
    </div>
    
  );
};

export default Register;