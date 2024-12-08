import { useState } from 'react';


function PasswordResetForm() {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:8000/api/password_reset/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email }),
      });

      const data = await response.json();

      if (response.ok) {
        setMessage('Se o email estiver registrado, um link foi enviado para redefinir a senha.');
        setError('');
      } else {
        setError(data.error || 'Erro ao solicitar o reset de senha.');
        setMessage('');
      }
    } catch (err) {
      setError('Erro na comunicação com o servidor.', err);
      setMessage('');
    }
  };

  return (
    <div>
      <h2>Redefinir Senha</h2>
      {message && <p>{message}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Digite seu email"
          required
        />
        <button type="submit">Enviar link de redefinição</button>
      </form>
    </div>
  );
}

export default PasswordResetForm;
