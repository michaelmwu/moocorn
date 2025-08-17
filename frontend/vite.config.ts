import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  // Load env file from parent directory
  const env = loadEnv(mode, '../', '')
  
  return {
    plugins: [react()],
    envDir: '../', // Look for .env files in parent directory
    server: {
      port: parseInt(env.MOOCORN_FRONTEND_PORT) || 5173
    }
  }
})
