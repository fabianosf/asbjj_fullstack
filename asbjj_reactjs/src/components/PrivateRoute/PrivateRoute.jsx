import { Navigate } from 'react-router-dom';
import PropTypes from 'prop-types'; // Para validar as props

function PrivateRoute({ element, role, ...rest }) {
  // Simula a obtenção do tipo de usuário (admin ou aluno)
  const userRole = localStorage.getItem('role'); // O role pode vir do localStorage ou de um Contexto Global

  if (!userRole) {
    // Redireciona para o login se o usuário não estiver autenticado
    return <Navigate to="/login" />;
  }

  if (role && userRole !== role) {
    // Se o role do usuário não corresponder, redireciona para a página apropriada
    return <Navigate to={userRole === 'admin' ? '/admin-dashboard' : '/area-do-aluno'} />;
  }

  // Se todas as condições forem atendidas, renderiza o componente passado
  return element;
}

// Validação de props com PropTypes
PrivateRoute.propTypes = {
  element: PropTypes.element.isRequired, // O elemento passado para a rota
  role: PropTypes.string, // O papel do usuário (admin ou aluno)
};

export default PrivateRoute;
