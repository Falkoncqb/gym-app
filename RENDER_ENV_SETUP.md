# 🚀 CONFIGURAR VARIABLES DE ENTORNO EN RENDER

## ⚠️ IMPORTANTE
El archivo `.env` NO funciona en Render. Debes configurar las variables de entorno directamente en el dashboard de Render.

---

## 📋 PASO A PASO

### 1. Ir a la Configuración de Environment

1. Ve a https://render.com/dashboard
2. Haz clic en tu servicio `gym-app`
3. En la barra lateral izquierda, haz clic en **"Environment"**
4. Verás un botón **"Add Environment Variable"**

---

### 2. Agregar las Variables de Entorno

Haz clic en **"Add Environment Variable"** y agrega cada una de estas variables:

#### Variable 1: SUPABASE_URL
```
Key: SUPABASE_URL
Value: https://ljajbmtviwiulasshaqo.supabase.co
```

#### Variable 2: SUPABASE_ANON_KEY
```
Key: SUPABASE_ANON_KEY
Value: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqYWpibXR2aXdpdWxhc3NoYXFvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQwOTAwMzksImV4cCI6MjA3OTY2NjAzOX0.aD6dm3Nn67NCr1f_RAoox9Lfu7QjsKcCuVq5SlL9BYA
```

#### Variable 3: SUPABASE_SERVICE_KEY
```
Key: SUPABASE_SERVICE_KEY
Value: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqYWpibXR2aXdpdWxhc3NoYXFvIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NDA5MDAzOSwiZXhwIjoyMDc5NjY2MDM5fQ.ZiLR1QwBWgswhkIr2QRRSpT6LOP_zdwCpi2GRXnODN0
```

#### Variable 4: SECRET_KEY
```
Key: SECRET_KEY
Value: Sebastian4123..
```

#### Variable 5: ADMIN_PASSWORD
```
Key: ADMIN_PASSWORD
Value: Gym_123456
```

#### Variable 6: FLASK_ENV
```
Key: FLASK_ENV
Value: production
```

---

### 3. Guardar y Redesplegar

1. Después de agregar todas las variables, haz clic en **"Save Changes"**
2. Render automáticamente redespliegará tu aplicación
3. Espera 2-3 minutos mientras se despliega

---

## 🎯 RESUMEN RÁPIDO

Debes agregar estas 6 variables en Render → Environment:

| Key | Value |
|-----|-------|
| `SUPABASE_URL` | `https://ljajbmtviwiulasshaqo.supabase.co` |
| `SUPABASE_ANON_KEY` | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqYWpibXR2aXdpdWxhc3NoYXFvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQwOTAwMzksImV4cCI6MjA3OTY2NjAzOX0.aD6dm3Nn67NCr1f_RAoox9Lfu7QjsKcCuVq5SlL9BYA` |
| `SUPABASE_SERVICE_KEY` | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqYWpibXR2aXdpdWxhc3NoYXFvIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NDA5MDAzOSwiZXhwIjoyMDc5NjY2MDM5fQ.ZiLR1QwBWgswhkIr2QRRSpT6LOP_zdwCpi2GRXnODN0` |
| `SECRET_KEY` | `Sebastian4123..` |
| `ADMIN_PASSWORD` | `Gym_123456` |
| `FLASK_ENV` | `production` |

---

## 🔍 VERIFICAR QUE FUNCIONÓ

Después de que Render termine de redesplegar:

1. Ve a la URL de tu app (algo como `https://gym-app-xxxx.onrender.com`)
2. Deberías ver la página principal
3. Ve a `/disciplinas` para verificar que carga los datos de Supabase
4. Ve a `/login` para probar el acceso de admin

---

## ❓ PREGUNTAS FRECUENTES

### ¿Por qué no funciona el archivo .env en Render?
Render no lee archivos `.env` por seguridad. Las variables de entorno se configuran en el dashboard.

### ¿Debo subir el archivo .env a GitHub?
**NO**. El archivo `.env` está en `.gitignore` y no debe subirse a GitHub porque contiene claves secretas.

### ¿Puedo usar un archivo .env en producción?
No es recomendado. Las plataformas como Render, Railway, Vercel, etc. usan variables de entorno del dashboard.

### ¿Qué pasa si cambio una variable?
Render automáticamente redespliegará tu aplicación cuando guardes los cambios.

---

## 🆘 SI AÚN HAY ERRORES

### Error: "Invalid API key"
- Verifica que copiaste correctamente las claves de Supabase
- Asegúrate de no tener espacios al inicio o final

### Error: "relation 'profesores' does not exist"
- Ve a Supabase → SQL Editor
- Ejecuta el script `supabase_schema.sql` nuevamente

### Error: "Module not found"
- Verifica que `requirements.txt` tenga todas las dependencias
- Asegúrate de que `gunicorn==21.2.0` esté en `requirements.txt`

---

## ✅ CHECKLIST

- [ ] Ir a Render → Environment
- [ ] Agregar `SUPABASE_URL`
- [ ] Agregar `SUPABASE_ANON_KEY`
- [ ] Agregar `SUPABASE_SERVICE_KEY`
- [ ] Agregar `SECRET_KEY`
- [ ] Agregar `ADMIN_PASSWORD`
- [ ] Agregar `FLASK_ENV=production`
- [ ] Guardar cambios
- [ ] Esperar redespliegue (2-3 min)
- [ ] Verificar que la app funciona

---

**¡Después de esto, tu app estará online 24/7!** 🚀
