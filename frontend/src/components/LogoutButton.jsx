import React from 'react';

const LogoutButton = () => {
  const handleLogout = () => {
    // Удаляем токен из localStorage
    localStorage.removeItem('token');

    // Перенаправляем пользователя на страницу входа в систему или выполняем другие действия
  };

  return (
    <button onClick={handleLogout}>Logout</button>
  );
};

export default LogoutButton;