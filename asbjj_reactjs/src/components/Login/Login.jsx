import { useState } from 'react';
import './Login.css';
import Footer from '../Footer/Footer';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom'; // Importando useNavigate

function Login() {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
    });
    const [message, setMessage] = useState('');
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate(); // Hook para redirecionar

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        setLoading(true);

        // Enviar dados para o backend
        axios.post('http://localhost:8000/api/login/', formData)
            .then(response => {
                setMessage(response.data.message);
                setLoading(false);

                // Verificar o tipo de usuário e redirecionar conforme o papel (role)
                if (response.data.role === 'admin') {
                    navigate('/area-do-aluno'); // Redireciona para a área do administrador
                } else if (response.data.role === 'aluno') {
                    navigate('/area-do-aluno'); // Redireciona para a área do aluno
                }
            })
            .catch(error => {
                setMessage(error.response?.data?.message || 'Erro ao fazer login');
                setLoading(false);
            });
    };

    return (
        <div id="root">
            <div className="main-content">
                <div className="form-container">
                    <h2>Entrar</h2>
                    {message && <div className="alert alert-info">{message}</div>}
                    <form onSubmit={handleSubmit}>
                        <input
                            type="text"
                            className="form-control"
                            name="username"
                            value={formData.username}
                            onChange={handleChange}
                            placeholder="Username"
                            required
                        />
                        <input
                            type="email"
                            className="form-control"
                            name="email"
                            value={formData.email}
                            onChange={handleChange}
                            placeholder="Email"
                            required
                        />
                         
                        <input
                            type="password"
                            className="form-control"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                            placeholder="Password"
                            required
                        />
                         
                        <div className="btn-container">
                            <button type="submit" className="btn btn-primary" disabled={loading}>
                                {loading ? 'Carregando...' : 'Login'}
                            </button>
                        </div>
                    </form>
                                                    
                    {/* Link para a página de cadastro */}
                    <div className="signup-link">
                        <p>Não tem uma conta? <Link to="/signup">Cadastre-se aqui</Link></p>
                        <p>Esqueceu sua senha? <Link to="/reset">Clique aqui para resetar</Link></p>
                    </div>
                                      
                </div>
            </div>  
            <Footer />          
        </div>
    );
}

export default Login;
