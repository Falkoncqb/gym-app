"""
Configuración de la aplicación
Carga las variables de entorno desde el archivo .env
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

class Config:
    """Configuración base de la aplicación"""
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey-change-in-production')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    
    # Supabase
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_ANON_KEY = os.getenv('SUPABASE_ANON_KEY')
    SUPABASE_SERVICE_KEY = os.getenv('SUPABASE_SERVICE_KEY')
    
    # Admin
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'Gym_123456')
    
    @staticmethod
    def validate():
        """Valida que las variables de entorno requeridas estén configuradas"""
        required_vars = ['SUPABASE_URL', 'SUPABASE_SERVICE_KEY']
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            raise ValueError(
                f"Faltan las siguientes variables de entorno: {', '.join(missing_vars)}\n"
                f"Por favor, crea un archivo .env basado en .env.example"
            )
