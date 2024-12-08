import './AreaDoAluno.css'; // Adicione estilos específicos aqui
import { FaUser, FaFileAlt, FaClipboardList, FaTrophy, FaTags, FaChartLine } from 'react-icons/fa';
import { useState, useEffect } from 'react';

function AreaDoAluno() {
  const [role, setRole] = useState('aluno'); // Suponha que você obteve o role ao fazer login
  
  // Se você estiver usando algo como o Redux ou Context API para armazenar o estado do usuário,
  // você pode obter esse valor de lá, ou então, pode passar essa informação como uma prop para esse componente.
  
  useEffect(() => {
    // Aqui você deve obter o role do usuário de onde você armazenou, exemplo de localStorage ou estado global
    const userRole = localStorage.getItem('role'); // Ou de algum outro lugar
    if (userRole) {
      setRole(userRole);
    }
  }, []);
  
  return (
    <div className="app-container">
      {/* Sidebar */}
      <nav className="sidebar">
        <ul>
          <li><FaClipboardList/> Inicio</li>
          <li><FaFileAlt/> Carga de dados</li>
          <li><FaUser/> Clientes</li>
          
          {/* Renderiza "Faturas" e "Movimentos" somente se o usuário for admin */}
          {role === 'admin' && (
            <>
              <li><FaFileAlt/> Faturas</li>
              <li><FaChartLine/> Movimentos</li>
            </>
          )}

          <li><FaClipboardList/> Grupos de parametros</li>
          <li><FaTrophy/> Nivel de beneficios</li>
          <li><FaTags/> Promoções / Exclusões</li>
        </ul>
      </nav>

      {/* Main Content */}
      <div className="main-content">
        {/* Top Bar */}
        <header className="top-bar">
          <span>UserName</span>
        </header>

        {/* Cards Section */}
        <div className="cards-container">
          <div className="card">Carga de dados</div>
          <div className="card">Clientes</div>
          
          {/* Renderiza "Faturas" e "Movimentos" somente se o usuário for admin */}
          {role === 'admin' && (
            <>
              <div className="card">Faturas</div>
              <div className="card">Movimentos</div>
            </>
          )}

          <div className="card">Grupos de parâmetros</div>
          <div className="card">Nivel de beneficios</div>
          <div className="card">Programas de referência</div>
          <div className="card">Promoções / Exclusões</div>
          <div className="card">Pontos de venda</div>
          <div className="card">Redenções</div>
        </div>
      </div>
    </div>
  );
}

export default AreaDoAluno;
