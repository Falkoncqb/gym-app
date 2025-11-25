import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime, timedelta
from supabase import create_client, Client
from config import Config

app = Flask(__name__)

# Validar configuración
Config.validate()

# Configurar Flask
app.secret_key = Config.SECRET_KEY

# Inicializar cliente de Supabase
supabase: Client = create_client(Config.SUPABASE_URL, Config.SUPABASE_SERVICE_KEY)

# --- FUNCIONES DE AYUDA (LOGICA) ---

def calcular_atraso(fecha_ultimo_pago):
    """Calcula días de atraso asumiendo ciclos de 30 días"""
    try:
        # Manejar tanto strings como objetos date
        if isinstance(fecha_ultimo_pago, str):
            fecha_pago = datetime.strptime(fecha_ultimo_pago, '%Y-%m-%d')
        else:
            fecha_pago = datetime.combine(fecha_ultimo_pago, datetime.min.time())
        
        hoy = datetime.now()
        diferencia = hoy - fecha_pago
        dias_pasados = diferencia.days
        # Si han pasado más de 30 días, hay atraso. Si no, devuelve 0.
        return max(0, dias_pasados - 30)
    except Exception as e:
        print(f"Error calculando atraso: {e}")
        return 0

def obtener_icono(nombre_disciplina):
    """Asigna un icono de FontAwesome según la disciplina"""
    iconos = {
        'SALSA': 'fa-music',
        'KARATE': 'fa-hand-rock',
        'JIU JITSU': 'fa-user-ninja',
        'CALISTENIA': 'fa-dumbbell',
        'JAZZ DANCE': 'fa-star'
    }
    return iconos.get(nombre_disciplina.upper(), 'fa-users')

# --- RUTAS DE LA APLICACIÓN ---

# 1. Landing Page (Nuevo Home)
@app.route('/')
def index():
    return render_template('index.html')

# 1.1 Menú de Disciplinas (Antiguo Home)
@app.route('/disciplinas')
def disciplinas_menu():
    try:
        # Obtener todos los profesores
        response = supabase.table('profesores').select('id, disciplina, nombre').execute()
        profesores = response.data
        
        # Preparamos la lista para el menú con iconos
        menu = []
        for profe in profesores:
            menu.append({
                'id': profe['id'],
                'disciplina': profe['disciplina'],
                'nombre_profe': profe['nombre'],
                'icono': obtener_icono(profe['disciplina'])
            })
        
        return render_template('disciplinas.html', menu=menu)
    except Exception as e:
        print(f"Error obteniendo disciplinas: {e}")
        return render_template('disciplinas.html', menu=[])

# 2. Vista Detalle de una Disciplina
@app.route('/disciplina/<int:profe_id>')
def ver_disciplina(profe_id):
    try:
        # Datos del profesor
        profesor_response = supabase.table('profesores').select('*').eq('id', profe_id).execute()
        
        if not profesor_response.data:
            return "Disciplina no encontrada", 404
        
        profesor = profesor_response.data[0]
        
        # Datos de sus alumnos
        alumnos_query = supabase.table('alumnos').select('*').eq('profesor_id', profe_id)
        
        # Búsqueda
        search_query = request.args.get('q')
        if search_query:
            # Supabase usa ilike para búsqueda case-insensitive
            alumnos_query = alumnos_query.or_(f'nombre_completo.ilike.%{search_query}%,run.ilike.%{search_query}%')
        
        alumnos_response = alumnos_query.execute()
        alumnos = alumnos_response.data
        
        # Procesamos alumnos para calcular atrasos
        lista_alumnos = []
        for alumno in alumnos:
            alumno['dias_atraso'] = calcular_atraso(alumno['fecha_ultimo_pago'])
            lista_alumnos.append(alumno)
        
        return render_template('detalle.html', profesor=profesor, alumnos=lista_alumnos)
    except Exception as e:
        print(f"Error obteniendo disciplina: {e}")
        return f"Error: {str(e)}", 500

# 3. Crear Alumno (Create)
@app.route('/add_alumno', methods=('POST',))
def add_alumno():
    try:
        profesor_id = request.form['profesor_id']
        nombre = request.form['nombre']
        run = request.form['run']
        email = request.form['email']
        telefono = request.form['telefono']
        valor = request.form['valor']
        fecha = request.form['fecha']
        
        # Insertar en Supabase
        supabase.table('alumnos').insert({
            'profesor_id': int(profesor_id),
            'nombre_completo': nombre,
            'run': run,
            'email': email,
            'telefono': telefono,
            'valor_plan': int(valor.replace('.', '').replace(',', '')),
            'fecha_ultimo_pago': fecha
        }).execute()
        
        return redirect(url_for('ver_disciplina', profe_id=profesor_id))
    except Exception as e:
        print(f"Error agregando alumno: {e}")
        flash('Error al agregar alumno', 'error')
        return redirect(url_for('ver_disciplina', profe_id=profesor_id))

# 4. Eliminar Alumno (Delete)
@app.route('/delete_alumno/<int:id>', methods=('POST',))
def delete_alumno(id):
    try:
        # Obtenemos el ID del profesor antes de borrar
        alumno_response = supabase.table('alumnos').select('profesor_id').eq('id', id).execute()
        
        if alumno_response.data:
            profesor_id = alumno_response.data[0]['profesor_id']
            
            # Eliminar alumno
            supabase.table('alumnos').delete().eq('id', id).execute()
            
            return redirect(url_for('ver_disciplina', profe_id=profesor_id))
        
        return redirect(url_for('disciplinas_menu'))
    except Exception as e:
        print(f"Error eliminando alumno: {e}")
        return redirect(url_for('disciplinas_menu'))

# 5. Vista Formulario de Edición (Read para Edit)
@app.route('/edit_alumno/<int:id>')
def edit_alumno(id):
    try:
        alumno_response = supabase.table('alumnos').select('*').eq('id', id).execute()
        
        if not alumno_response.data:
            return "Alumno no encontrado", 404
        
        alumno = alumno_response.data[0]
        return render_template('editar.html', alumno=alumno)
    except Exception as e:
        print(f"Error obteniendo alumno: {e}")
        return "Error al cargar alumno", 500

# 6. Guardar Cambios de Edición (Update)
@app.route('/update_alumno/<int:id>', methods=('POST',))
def update_alumno(id):
    try:
        nombre = request.form['nombre']
        run = request.form['run']
        email = request.form['email']
        telefono = request.form['telefono']
        valor = request.form['valor']
        fecha = request.form['fecha']
        
        # Obtenemos ID del profesor para redirigir
        alumno_response = supabase.table('alumnos').select('profesor_id').eq('id', id).execute()
        profesor_id = alumno_response.data[0]['profesor_id']
        
        # Actualizar alumno
        supabase.table('alumnos').update({
            'nombre_completo': nombre,
            'run': run,
            'email': email,
            'telefono': telefono,
            'valor_plan': int(valor.replace('.', '').replace(',', '')),
            'fecha_ultimo_pago': fecha
        }).eq('id', id).execute()
        
        return redirect(url_for('ver_disciplina', profe_id=profesor_id))
    except Exception as e:
        print(f"Error actualizando alumno: {e}")
        flash('Error al actualizar alumno', 'error')
        return redirect(url_for('edit_alumno', id=id))

# --- AUTENTICACIÓN ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        password = request.form['password']
        if password == Config.ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            error = 'Contraseña incorrecta'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('index'))

# --- RUTAS DE ADMINISTRACIÓN ---

@app.route('/admin')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    
    try:
        response = supabase.table('profesores').select('*').execute()
        profesores = response.data
        return render_template('admin.html', profesores=profesores, today=datetime.now().strftime('%Y-%m-%d'))
    except Exception as e:
        print(f"Error obteniendo profesores: {e}")
        return render_template('admin.html', profesores=[], today=datetime.now().strftime('%Y-%m-%d'))

@app.route('/admin/profesor/add', methods=('GET', 'POST'))
def add_profesor():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            disciplina = request.form['disciplina']
            horario = request.form['horario']
            pago_mensual = request.form['pago_mensual_gym']
            fecha_pago = request.form['fecha_pago_profe']
            
            supabase.table('profesores').insert({
                'nombre': nombre,
                'disciplina': disciplina,
                'horario': horario,
                'pago_mensual_gym': pago_mensual,
                'fecha_pago_profe': fecha_pago
            }).execute()
            
            return redirect(url_for('admin_dashboard'))
        except Exception as e:
            print(f"Error agregando profesor: {e}")
            flash('Error al agregar profesor', 'error')
    
    return render_template('profesor_form.html', action='add')

@app.route('/admin/profesor/edit/<int:id>', methods=('GET', 'POST'))
def edit_profesor(id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))

    try:
        profesor_response = supabase.table('profesores').select('*').eq('id', id).execute()
        
        if not profesor_response.data:
            return "Profesor no encontrado", 404
        
        profesor = profesor_response.data[0]
        
        if request.method == 'POST':
            nombre = request.form['nombre']
            disciplina = request.form['disciplina']
            horario = request.form['horario']
            pago_mensual = request.form['pago_mensual_gym']
            fecha_pago = request.form['fecha_pago_profe']
            
            supabase.table('profesores').update({
                'nombre': nombre,
                'disciplina': disciplina,
                'horario': horario,
                'pago_mensual_gym': pago_mensual,
                'fecha_pago_profe': fecha_pago
            }).eq('id', id).execute()
            
            return redirect(url_for('admin_dashboard'))
        
        return render_template('profesor_form.html', profesor=profesor, action='edit')
    except Exception as e:
        print(f"Error editando profesor: {e}")
        return "Error al editar profesor", 500

@app.route('/admin/profesor/delete/<int:id>', methods=('POST',))
def delete_profesor(id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))

    try:
        # Gracias a ON DELETE CASCADE en la BD, los alumnos se eliminan automáticamente
        supabase.table('profesores').delete().eq('id', id).execute()
        return redirect(url_for('admin_dashboard'))
    except Exception as e:
        print(f"Error eliminando profesor: {e}")
        flash('Error al eliminar profesor', 'error')
        return redirect(url_for('admin_dashboard'))

@app.route('/admin/profesor/pagar/<int:id>', methods=('POST',))
def pagar_profesor(id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))

    try:
        profesor_response = supabase.table('profesores').select('fecha_pago_profe').eq('id', id).execute()
        
        if profesor_response.data:
            profesor = profesor_response.data[0]
            # Parsear la fecha actual
            fecha_actual = datetime.strptime(profesor['fecha_pago_profe'], '%Y-%m-%d')
            # Sumar 30 días
            nueva_fecha = fecha_actual + timedelta(days=30)
            nueva_fecha_str = nueva_fecha.strftime('%Y-%m-%d')
            
            supabase.table('profesores').update({
                'fecha_pago_profe': nueva_fecha_str
            }).eq('id', id).execute()
        
        return redirect(url_for('admin_dashboard'))
    except Exception as e:
        print(f"Error actualizando pago de profesor: {e}")
        flash('Error al actualizar pago', 'error')
        return redirect(url_for('admin_dashboard'))

# --- EJECUCIÓN ---
if __name__ == '__main__':
    app.run(debug=True)