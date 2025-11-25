"""
Script de verificación de configuración
Ejecuta este script para verificar que todo está configurado correctamente
"""
import os
import sys

def check_env_file():
    """Verifica que el archivo .env existe"""
    if not os.path.exists('.env'):
        print("❌ ERROR: No se encontró el archivo .env")
        print("   Crea un archivo .env basado en .env.example")
        return False
    print("✅ Archivo .env encontrado")
    return True

def check_env_variables():
    """Verifica que las variables de entorno están configuradas"""
    from dotenv import load_dotenv
    load_dotenv()
    
    required_vars = {
        'SUPABASE_URL': 'URL de tu proyecto Supabase',
        'SUPABASE_SERVICE_KEY': 'Service Role Key de Supabase',
    }
    
    missing = []
    for var, description in required_vars.items():
        value = os.getenv(var)
        if not value or value.startswith('tu_'):
            missing.append(f"   - {var}: {description}")
            print(f"❌ {var} no configurada")
        else:
            print(f"✅ {var} configurada")
    
    if missing:
        print("\n❌ ERROR: Faltan las siguientes variables de entorno:")
        print('\n'.join(missing))
        return False
    
    return True

def check_dependencies():
    """Verifica que las dependencias están instaladas"""
    try:
        import flask
        print("✅ Flask instalado")
    except ImportError:
        print("❌ Flask no instalado")
        return False
    
    try:
        import supabase
        print("✅ Supabase instalado")
    except ImportError:
        print("❌ Supabase no instalado")
        return False
    
    try:
        import dotenv
        print("✅ python-dotenv instalado")
    except ImportError:
        print("❌ python-dotenv no instalado")
        return False
    
    return True

def test_supabase_connection():
    """Intenta conectarse a Supabase"""
    try:
        from dotenv import load_dotenv
        from supabase import create_client
        
        load_dotenv()
        
        url = os.getenv('SUPABASE_URL')
        key = os.getenv('SUPABASE_SERVICE_KEY')
        
        if not url or not key:
            print("❌ No se pueden probar la conexión sin credenciales")
            return False
        
        client = create_client(url, key)
        
        # Intentar una consulta simple
        response = client.table('profesores').select('count').execute()
        
        print("✅ Conexión a Supabase exitosa")
        print(f"   Profesores en la base de datos: {len(response.data) if response.data else 0}")
        return True
        
    except Exception as e:
        print(f"❌ Error al conectar con Supabase: {str(e)}")
        return False

def main():
    print("=" * 60)
    print("🔍 VERIFICACIÓN DE CONFIGURACIÓN - GYM APP")
    print("=" * 60)
    print()
    
    checks = [
        ("Archivo .env", check_env_file),
        ("Dependencias", check_dependencies),
        ("Variables de entorno", check_env_variables),
        ("Conexión a Supabase", test_supabase_connection),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n📋 Verificando: {name}")
        print("-" * 60)
        result = check_func()
        results.append(result)
        print()
    
    print("=" * 60)
    if all(results):
        print("✅ ¡TODO CONFIGURADO CORRECTAMENTE!")
        print("   Puedes ejecutar la aplicación con: python app.py")
    else:
        print("❌ HAY PROBLEMAS DE CONFIGURACIÓN")
        print("   Por favor, revisa los errores arriba y consulta GUIA_DESPLIEGUE.md")
    print("=" * 60)
    
    return 0 if all(results) else 1

if __name__ == '__main__':
    sys.exit(main())
