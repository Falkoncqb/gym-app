# 🚀 Guía Completa de Despliegue con Supabase

Esta guía te llevará paso a paso para migrar tu aplicación de gimnasio a Supabase.

---

## 📋 Tabla de Contenidos

1. [Requisitos Previos](#requisitos-previos)
2. [Configuración de Supabase](#configuración-de-supabase)
3. [Configuración Local](#configuración-local)
4. [Despliegue en Producción](#despliegue-en-producción)
5. [Solución de Problemas](#solución-de-problemas)

---

## 1️⃣ Requisitos Previos

Antes de comenzar, asegúrate de tener:

- ✅ Python 3.8 o superior instalado
- ✅ Una cuenta en [Supabase](https://supabase.com) (gratis)
- ✅ Git instalado (opcional, pero recomendado)

---

## 2️⃣ Configuración de Supabase

### Paso 1: Crear un Proyecto en Supabase

1. Ve a [https://supabase.com](https://supabase.com)
2. Haz clic en **"Start your project"** o **"Sign In"** si ya tienes cuenta
3. Crea una nueva organización (si es tu primera vez)
4. Haz clic en **"New Project"**
5. Completa los datos:
   - **Name**: `gym-app` (o el nombre que prefieras)
   - **Database Password**: Crea una contraseña segura y **guárdala** (la necesitarás)
   - **Region**: Selecciona la región más cercana a ti (ej: South America - São Paulo)
   - **Pricing Plan**: Free (suficiente para empezar)
6. Haz clic en **"Create new project"**
7. Espera 1-2 minutos mientras Supabase configura tu base de datos

### Paso 2: Obtener las Credenciales

Una vez creado el proyecto:

1. En el panel de Supabase, ve a **Settings** (⚙️) en la barra lateral izquierda
2. Haz clic en **API**
3. Encontrarás dos valores importantes:
   - **Project URL**: Algo como `https://xxxxxxxxxxxxx.supabase.co`
   - **API Keys**:
     - `anon` / `public`: Clave pública (puedes compartirla)
     - `service_role`: Clave privada ⚠️ **NUNCA la compartas públicamente**

4. **Copia estos valores**, los necesitarás en el siguiente paso

### Paso 3: Crear las Tablas en Supabase

1. En el panel de Supabase, ve a **SQL Editor** en la barra lateral
2. Haz clic en **"New query"**
3. Abre el archivo `supabase_schema.sql` de tu proyecto
4. **Copia TODO el contenido** del archivo
5. **Pégalo** en el editor SQL de Supabase
6. Haz clic en **"Run"** (▶️) en la esquina inferior derecha
7. Deberías ver el mensaje: **"Success. No rows returned"**

### Paso 4: Verificar las Tablas

1. Ve a **Table Editor** en la barra lateral
2. Deberías ver dos tablas:
   - `profesores` (con 5 registros de ejemplo)
   - `alumnos` (con 1 registro de ejemplo)
3. Haz clic en cada tabla para verificar que los datos de prueba se cargaron correctamente

---

## 3️⃣ Configuración Local

### Paso 1: Instalar Dependencias

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
# Activar el entorno virtual (si usas uno)
.venv\Scripts\activate

# Instalar las nuevas dependencias
pip install -r requirements.txt
```

### Paso 2: Configurar Variables de Entorno

1. En la carpeta del proyecto, crea un archivo llamado `.env` (sin extensión antes del punto)
2. Copia el contenido de `.env.example` al nuevo archivo `.env`
3. Completa con tus credenciales de Supabase:

```env
# URL de tu proyecto Supabase
SUPABASE_URL=https://xxxxxxxxxxxxx.supabase.co

# Clave anon/public de Supabase
SUPABASE_ANON_KEY=tu_clave_anon_aqui

# Clave de servicio de Supabase
SUPABASE_SERVICE_KEY=tu_clave_service_role_aqui

# Clave secreta para sesiones de Flask (genera una aleatoria)
SECRET_KEY=cambia_esto_por_una_clave_segura_aleatoria

# Contraseña del administrador
ADMIN_PASSWORD=Gym_123456

# Entorno
FLASK_ENV=development
```

**⚠️ IMPORTANTE**: 
- Reemplaza `https://xxxxxxxxxxxxx.supabase.co` con tu **Project URL**
- Reemplaza `tu_clave_anon_aqui` con tu **anon key**
- Reemplaza `tu_clave_service_role_aqui` con tu **service_role key**
- Para `SECRET_KEY`, genera una clave aleatoria (puedes usar un generador online)

### Paso 3: Probar la Aplicación Localmente

1. Asegúrate de que el servidor anterior esté detenido (presiona `Ctrl+C` en la terminal donde corre)
2. Ejecuta la aplicación:

```bash
python app.py
```

3. Abre tu navegador en `http://localhost:5000`
4. Verifica que:
   - ✅ La página principal carga correctamente
   - ✅ Puedes ver las disciplinas en `/disciplinas`
   - ✅ Puedes ver los alumnos de cada disciplina
   - ✅ Puedes iniciar sesión en `/login` con la contraseña `Gym_123456`
   - ✅ Puedes agregar, editar y eliminar alumnos y profesores

---

## 4️⃣ Despliegue en Producción

### Opción A: Despliegue en Render (Recomendado - Gratis)

1. **Crear cuenta en Render**:
   - Ve a [https://render.com](https://render.com)
   - Regístrate con GitHub (recomendado)

2. **Subir código a GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Migración a Supabase"
   git branch -M main
   git remote add origin https://github.com/tu-usuario/gym-app.git
   git push -u origin main
   ```

3. **Crear Web Service en Render**:
   - En Render, haz clic en **"New +"** → **"Web Service"**
   - Conecta tu repositorio de GitHub
   - Configura:
     - **Name**: `gym-app`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Instance Type**: `Free`

4. **Agregar gunicorn a requirements.txt**:
   ```bash
   echo gunicorn==21.2.0 >> requirements.txt
   git add requirements.txt
   git commit -m "Add gunicorn"
   git push
   ```

5. **Configurar Variables de Entorno en Render**:
   - En la configuración del servicio, ve a **"Environment"**
   - Agrega las siguientes variables (copia desde tu `.env`):
     - `SUPABASE_URL`
     - `SUPABASE_ANON_KEY`
     - `SUPABASE_SERVICE_KEY`
     - `SECRET_KEY`
     - `ADMIN_PASSWORD`
     - `FLASK_ENV=production`

6. **Desplegar**:
   - Haz clic en **"Create Web Service"**
   - Espera 2-3 minutos mientras Render despliega tu app
   - Tu app estará disponible en `https://gym-app-xxxx.onrender.com`

### Opción B: Despliegue en Railway

1. Ve a [https://railway.app](https://railway.app)
2. Regístrate con GitHub
3. Haz clic en **"New Project"** → **"Deploy from GitHub repo"**
4. Selecciona tu repositorio
5. Agrega las variables de entorno (igual que en Render)
6. Railway detectará automáticamente que es una app Flask y la desplegará

### Opción C: Despliegue en Vercel (con Serverless)

1. Instala Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Crea un archivo `vercel.json`:
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

3. Despliega:
   ```bash
   vercel
   ```

4. Configura las variables de entorno en el dashboard de Vercel

---

## 5️⃣ Solución de Problemas

### Error: "Faltan las siguientes variables de entorno"

**Solución**: Verifica que tu archivo `.env` existe y contiene todas las variables requeridas.

### Error: "Invalid API key"

**Solución**: 
- Verifica que copiaste correctamente las claves desde Supabase
- Asegúrate de usar la `service_role` key, no la `anon` key en `SUPABASE_SERVICE_KEY`

### Error: "relation 'profesores' does not exist"

**Solución**: 
- Ve al SQL Editor de Supabase
- Ejecuta nuevamente el script `supabase_schema.sql`

### La aplicación no se conecta a Supabase

**Solución**:
1. Verifica que tu proyecto de Supabase esté activo
2. Verifica que la URL de Supabase sea correcta (debe terminar en `.supabase.co`)
3. Verifica que las políticas RLS estén configuradas correctamente

### Error al desplegar en producción

**Solución**:
- Verifica que todas las variables de entorno estén configuradas en la plataforma
- Revisa los logs de la plataforma para ver el error específico
- Asegúrate de que `gunicorn` esté en `requirements.txt` si usas Render o Railway

---

## 📚 Recursos Adicionales

- [Documentación de Supabase](https://supabase.com/docs)
- [Documentación de Flask](https://flask.palletsprojects.com/)
- [Guía de Python Supabase Client](https://supabase.com/docs/reference/python/introduction)

---

## 🎉 ¡Felicidades!

Si llegaste hasta aquí, tu aplicación debería estar funcionando con Supabase. 

### Ventajas de usar Supabase:

✅ **Escalabilidad**: Soporta miles de usuarios simultáneos
✅ **Backup automático**: Tus datos están respaldados
✅ **API REST automática**: Puedes crear apps móviles fácilmente
✅ **Autenticación integrada**: Puedes agregar login con Google, GitHub, etc.
✅ **Realtime**: Puedes agregar actualizaciones en tiempo real
✅ **Storage**: Puedes almacenar imágenes y archivos

---

## 🔐 Seguridad en Producción

Antes de lanzar a producción, considera:

1. **Cambiar la contraseña de admin**: Usa una contraseña más segura
2. **Usar HTTPS**: Todas las plataformas mencionadas lo incluyen automáticamente
3. **Revisar políticas RLS**: Ajusta las políticas de seguridad según tus necesidades
4. **Rotar claves**: Cambia periódicamente tus claves de API
5. **Monitorear uso**: Revisa el dashboard de Supabase para detectar uso anormal

---

**¿Necesitas ayuda?** Revisa la sección de [Solución de Problemas](#solución-de-problemas) o contacta al soporte de Supabase.
