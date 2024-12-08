
import { useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';


function PasswordResetConfirmForm() {
  const { uid, token } = useParams(); // Obtendo o uid e token da URL
  const [newPassword, setNewPassword] = useState('');
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');
  const history = useNavigate(); // Para redirecionar após o sucesso

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:8000/api/password_reset_confirm/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ uid, token, new_password: newPassword }),
      });

      const data = await response.json();

      if (response.ok) {
        setMessage('Senha alterada com sucesso.');
        setError('');
        setTimeout(() => {
          history.push('/login'); // Redireciona para a tela de login
        }, 2000);
      } else {
        setError(data.error || 'Erro ao alterar a senha.');
        setMessage('');
      }
    } catch (err) {
      setError('Erro na comunicação com o servidor.', err);
      setMessage('');
    }
  };

  return (
    <div>
      <h2>Alterar Senha</h2>
      {message && <p>{message}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="password"
          value={newPassword}
          onChange={(e) => setNewPassword(e.target.value)}
          placeholder="Nova Senha"
          required
        />
        <button type="submit">Alterar Senha</button>
      </form>
    </div>
  );
}

export default PasswordResetConfirmForm;
