import React, {useContext} from 'react'
import AuthContext from '../Context/AuthContext'

const LoginPage = () => {
    let {loginUser} = useContext(AuthContext)
  return (
    <div>
        <form onSubmit={loginUser}>
            <input type="text" name='username' placeholder='Enter UserName' />
            <input type="password" name='password' placeholder='Enter Password' />
            <input type="submit"/>
        </form>
    </div>
  )
}

export default LoginPage