# ⚡ PASOS RÁPIDOS PARA LANZAR CON SUPABASE

## 📝 RESUMEN DE CAMBIOS REALIZADOS

He migrado completamente tu aplicación de SQLite a Supabase. Estos son los archivos modificados/creados:

### ✅ Archivos Modificados:
- `app.py` - Actualizado para usar Supabase en lugar de SQLite
- `requirements.txt` - Agregadas dependencias de Supabase

### ✅ Archivos Nuevos:
- `config.py` - Manejo de configuración y variables de entorno
- `supabase_schema.sql` - Esquema de base de datos para PostgreSQL
- `.env.example` - Plantilla de variables de entorno
- `.gitignore` - Protección de archivos sensibles
- `verify_setup.py` - Script de verificación de configuración
- `GUIA_DESPLIEGUE.md` - Guía completa paso a paso
- `README.md` - Documentación del proyecto
- `PASOS_RAPIDOS.md` - Este archivo

---

## 🚀 PASOS A SEGUIR (VERSIÓN CORTA)

### 1. Crear Proyecto en Supabase (5 minutos)

1. Ve a https://supabase.com y crea una cuenta
2. Crea un nuevo proyecto:
   - Nombre: `gym-app`
   - Contraseña de BD: (guárdala bien)
   - Región: South America - São Paulo
3. Espera 1-2 minutos a que se cree

### 2. Configurar Base de Datos (2 minutos)

1. En Supabase, ve a **SQL Editor** (icono de código)
2. Haz clic en **"New query"**
3. Abre el archivo `supabase_schema.sql` de este proyecto
4. Copia TODO el contenido y pégalo en el editor
5. Haz clic en **"Run"** (▶️)
6. Verifica en **Table Editor** que se crearon las tablas `profesores` y `alumnos`

### 3. Obtener Credenciales (1 minuto)

1. En Supabase, ve a **Settings** → **API**
2. Copia estos valores:
   - **Project URL**: `https://xxxxx.supabase.co`
   - **anon public key**: `eyJhbGc...`
   - **service_role key**: `eyJhbGc...` ⚠️ (secreta)

### 4. Configurar Proyecto Local (3 minutos)

1. Abre una terminal en la carpeta del proyecto

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Crea un archivo `.env` (copia de `.env.example`):
   ```bash
   copy .env.example .env
   ```

4. Edita el archivo `.env` con tus credenciales:
   ```env
   SUPABASE_URL=https://xxxxx.supabase.co
   SUPABASE_ANON_KEY=eyJhbGc...
   SUPABASE_SERVICE_KEY=eyJhbGc...
   SECRET_KEY=una_clave_aleatoria_segura
   ADMIN_PASSWORD=Gym_123456
   FLASK_ENV=development
   ```

### 5. Verificar Configuración (1 minuto)

```bash
python verify_setup.py
```

Si todo está bien, verás: ✅ ¡TODO CONFIGURADO CORRECTAMENTE!

### 6. Ejecutar la Aplicación (1 minuto)

```bash
python app.py
```

Abre tu navegador en: http://localhost:5000

---

## 🎯 VERIFICACIÓN RÁPIDA

Prueba estas funcionalidades:

- [ ] La página principal carga
- [ ] Puedes ver disciplinas en `/disciplinas`
- [ ] Puedes ver alumnos de una disciplina
- [ ] Puedes iniciar sesión en `/login` (contraseña: `Gym_123456`)
- [ ] Puedes agregar un nuevo alumno
- [ ] Puedes editar un alumno
- [ ] Puedes eliminar un alumno
- [ ] Puedes agregar un nuevo profesor desde el panel admin

---

## 🌐 DESPLEGAR EN PRODUCCIÓN

### Opción Recomendada: Render (Gratis)

1. **Sube tu código a GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Migración a Supabase"
   git remote add origin https://github.com/tu-usuario/gym-app.git
   git push -u origin main
   ```

2. **Agrega gunicorn**:
   ```bash
   echo gunicorn==21.2.0 >> requirements.txt
   git add requirements.txt
   git commit -m "Add gunicorn"
   git push
   ```

3. **Despliega en Render**:
   - Ve a https://render.com
   - Crea una cuenta (usa GitHub)
   - New → Web Service
   - Conecta tu repositorio
   - Configuración:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn app:app`
   - Agrega las variables de entorno (desde tu `.env`)
   - Deploy!

4. **Tu app estará en**: `https://gym-app-xxxx.onrender.com`

---

## 🆘 PROBLEMAS COMUNES

### "Faltan variables de entorno"
→ Verifica que tu archivo `.env` existe y tiene todas las variables

### "Invalid API key"
→ Verifica que copiaste correctamente las claves desde Supabase

### "relation 'profesores' does not exist"
→ Ejecuta el script `supabase_schema.sql` en el SQL Editor de Supabase

### La app no se conecta
→ Ejecuta `python verify_setup.py` para diagnosticar

---

## 📚 MÁS INFORMACIÓN

Para una guía detallada con capturas de pantalla y más opciones de despliegue, consulta:

👉 **[GUIA_DESPLIEGUE.md](GUIA_DESPLIEGUE.md)**

---

## ✨ VENTAJAS DE SUPABASE

- ✅ **Gratis hasta 500MB** de base de datos
- ✅ **Backup automático** de tus datos
- ✅ **Escalable** a miles de usuarios
- ✅ **API REST automática** para apps móviles
- ✅ **Autenticación integrada** (Google, GitHub, etc.)
- ✅ **Realtime** para actualizaciones en vivo
- ✅ **Storage** para imágenes y archivos

---

## 🎉 ¡LISTO!

Si seguiste estos pasos, tu aplicación ya está funcionando con Supabase.

**Próximos pasos sugeridos**:
1. Cambia la contraseña de admin en producción
2. Personaliza los datos de ejemplo
3. Despliega en Render para tener tu app online 24/7
4. Comparte el link con tus usuarios

---

**¿Necesitas ayuda?** Revisa la [GUIA_DESPLIEGUE.md](GUIA_DESPLIEGUE.md) completa.
