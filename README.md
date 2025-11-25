# Gym App - Sistema de Gestión de Gimnasio

Sistema web para gestionar profesores, disciplinas y alumnos de un gimnasio, construido con Flask y Supabase.

## 🌟 Características

- ✅ Gestión de profesores y disciplinas
- ✅ Gestión de alumnos por disciplina
- ✅ Cálculo automático de atrasos de pago
- ✅ Panel de administración protegido
- ✅ Búsqueda de alumnos
- ✅ Interfaz moderna y responsive
- ✅ Base de datos en la nube con Supabase

## 🚀 Inicio Rápido

### Requisitos

- Python 3.8+
- Cuenta en Supabase (gratis)

### Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/gym-app.git
   cd gym-app
   ```

2. **Crear entorno virtual**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/Mac
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar Supabase**:
   - Lee la [Guía de Despliegue](GUIA_DESPLIEGUE.md) completa
   - Crea un proyecto en [Supabase](https://supabase.com)
   - Ejecuta el script `supabase_schema.sql` en el SQL Editor
   - Copia `.env.example` a `.env` y completa tus credenciales

5. **Ejecutar la aplicación**:
   ```bash
   python app.py
   ```

6. **Abrir en el navegador**:
   ```
   http://localhost:5000
   ```

## 📖 Documentación

Para una guía completa de configuración y despliegue, consulta [GUIA_DESPLIEGUE.md](GUIA_DESPLIEGUE.md)

## 🔑 Acceso de Administrador

- **URL**: `/login`
- **Contraseña por defecto**: `Gym_123456` (cámbiala en producción)

## 🛠️ Tecnologías

- **Backend**: Flask (Python)
- **Base de Datos**: Supabase (PostgreSQL)
- **Frontend**: HTML, CSS, JavaScript
- **Iconos**: FontAwesome

## 📁 Estructura del Proyecto

```
gym_app/
├── app.py                  # Aplicación principal
├── config.py               # Configuración y variables de entorno
├── requirements.txt        # Dependencias de Python
├── supabase_schema.sql     # Esquema de base de datos
├── .env.example            # Ejemplo de variables de entorno
├── GUIA_DESPLIEGUE.md      # Guía completa de despliegue
├── templates/              # Plantillas HTML
│   ├── index.html
│   ├── disciplinas.html
│   ├── detalle.html
│   ├── admin.html
│   └── ...
└── .venv/                  # Entorno virtual (no incluido en git)
```

## 🌐 Despliegue

La aplicación puede desplegarse en:

- **Render** (Recomendado - Gratis)
- **Railway** (Gratis con límites)
- **Vercel** (Serverless)
- **Heroku** (De pago)

Consulta la [Guía de Despliegue](GUIA_DESPLIEGUE.md) para instrucciones detalladas.

## 🔐 Seguridad

- ✅ Variables de entorno para credenciales sensibles
- ✅ Sesiones seguras con Flask
- ✅ Row Level Security (RLS) en Supabase
- ✅ Validación de entrada de usuario
- ✅ Protección de rutas de administrador

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📧 Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue.

---

**Hecho con ❤️ para la gestión eficiente de gimnasios**
