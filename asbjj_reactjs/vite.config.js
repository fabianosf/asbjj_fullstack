import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',  // Permite o acesso de qualquer endereço IP
    port: 5173,       // Porta configurada para o frontend
  }
})
