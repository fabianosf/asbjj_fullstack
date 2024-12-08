

const Exclusive = () => {
  const username = localStorage.getItem('username');

  return (
    <div>
      <h1>Bem-vindo à Área Exclusiva!</h1>
      {username && <p>Olá, {username}!</p>}
      <p>Aqui você pode acessar conteúdo exclusivo.</p>
    </div>
  );
};

export default Exclusive;
