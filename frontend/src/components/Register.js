import React, { useState,useEffect } from 'react';
import {Link, useNavigate} from 'react-router-dom';
import axios from 'axios';

const Register = () => {

    let history = useNavigate();


   
    const [username, setUserName] = useState(null) 
    const [email, setEmail] = useState(null)
    const [password, setPassword] = useState(null)



    const addNewStudent = async () => {
        let formField = new FormData()
        formField.append('username',username)
        formField.append('email',email)
        formField.append('password',password)

        await axios({
          method: 'post',
          url:'http://localhost:8000/register',
          data: formField
        }).then(response=>{
          console.log(response.data);
            console.log(response.data.id)
            history(`/login`)
        })
    }

   
    return (
        <div className="form">
            <div className="title">Welcome</div>
            <div className="subtitle">Let's create your account!</div>


           <div className = "lox">fdhddfhdffh</div>

            <div className="input-container ic1">
                <input id="firstname" className="input" type="text" placeholder=" "  value={username}
              onChange={(e) => setUserName(e.target.value)}></input>
                <div className="cut"></div>
                <label htmlFor="firstname" className="placeholder">Username</label>
            </div>

           
             <div className="input-container ic1">
                <input id="email" name='email' className="input" type="email" placeholder=" " value={email}
             onChange={(e) => setUserName(e.target.value)}></input>
                <div className="cut"></div>
                <label htmlFor="email" className="placeholder">Email</label>
            </div>

            <div className="input-container ic8">
                <input id="password" className="input" type="password" placeholder=" "value={password}
              onChange={(e) => setPassword(e.target.value)}></input>
                <div className="cut"></div>
                <label htmlFor="password" className="placeholder">Password</label>

            </div>

      <button type="text" className="submit" onClick={addNewStudent}>submit</button>
            <br></br>
            <Link to="/login1" className='have_account'>Есть аккаунт? Авторизуйтесь</Link>
        </div>
    );
};

export default Register;