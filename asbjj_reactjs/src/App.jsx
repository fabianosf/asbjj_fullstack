import './App.css';
import Navbar from './components/Navbar/Navbar';
import Home from './components/Home/Home';
import About from './components/About/About';
import Contact from './components/Contact/Contact';
import Service from './components/Service/Service';
import Login from './components/Login/Login';
import Signup from './components/Signup/Signup';
import Exclusive from './components/Exclusive/Exclusive'; // Componente protegido
import PrivateRoute from './components/PrivateRoute/PrivateRoute'; // Rota protegida
import AreaDoAluno from './components/AreaDoAluno/AreaDoAluno'; // Página da Área do Aluno
import PasswordResetForm from './components/PasswordResetForm/PasswordResetForm'; // Importa o componente de reset de senha
import PasswordResetConfirmForm from './components/PasswordResetConfirmForm/PasswordResetConfirmForm'; // Importa o componente de confirmação de reset

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div>
      <Router>
        <Navbar />
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/about' element={<About />} />
          <Route path='/contact' element={<Contact />} />
          <Route path='/service' element={<Service />} />          
          <Route path='/login' element={<Login />} />
          <Route path='/signup' element={<Signup />} /> 
          <Route path="/area-do-aluno" element={<AreaDoAluno />} /> {/* Página da Área do Aluno */}
          
          
          {/* Rota para Resetar Senha */}
          <Route path='/reset' element={<PasswordResetForm />} /> {/* Página para solicitar o reset */}
          
          {/* Rota para Confirmar Reset de Senha */}
          <Route path='/reset/:uid/:token' element={<PasswordResetConfirmForm />} /> {/* Página para inserir nova senha */}

          {/* Rota protegida */}
          <Route path='/exclusive' element={<PrivateRoute component={Exclusive} />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
