-- ============================================
-- ESQUEMA DE BASE DE DATOS PARA SUPABASE
-- ============================================

-- Eliminar tablas si existen (para desarrollo)
DROP TABLE IF EXISTS alumnos CASCADE;
DROP TABLE IF EXISTS profesores CASCADE;

-- ============================================
-- TABLA: profesores
-- ============================================
CREATE TABLE profesores (
    id BIGSERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    disciplina TEXT NOT NULL,
    horario TEXT NOT NULL,
    pago_mensual_gym INTEGER NOT NULL,
    fecha_pago_profe DATE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW()) NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW()) NOT NULL
);

-- ============================================
-- TABLA: alumnos
-- ============================================
CREATE TABLE alumnos (
    id BIGSERIAL PRIMARY KEY,
    profesor_id BIGINT NOT NULL REFERENCES profesores(id) ON DELETE CASCADE,
    nombre_completo TEXT NOT NULL,
    run TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL,
    valor_plan INTEGER NOT NULL,
    fecha_ultimo_pago DATE NOT NULL,
    asistencia_confirmada BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW()) NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW()) NOT NULL
);

-- ============================================
-- ÍNDICES para mejorar el rendimiento
-- ============================================
CREATE INDEX idx_alumnos_profesor_id ON alumnos(profesor_id);
CREATE INDEX idx_alumnos_run ON alumnos(run);
CREATE INDEX idx_profesores_disciplina ON profesores(disciplina);

-- ============================================
-- FUNCIÓN: Actualizar timestamp automáticamente
-- ============================================
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = TIMEZONE('utc'::text, NOW());
    RETURN NEW;
END;
$$ language 'plpgsql';

-- ============================================
-- TRIGGERS: Actualizar updated_at
-- ============================================
CREATE TRIGGER update_profesores_updated_at BEFORE UPDATE ON profesores
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_alumnos_updated_at BEFORE UPDATE ON alumnos
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- ============================================
-- DATOS DE PRUEBA (Seed Data)
-- ============================================
INSERT INTO profesores (nombre, disciplina, horario, pago_mensual_gym, fecha_pago_profe) VALUES
('Juan Pérez', 'SALSA', 'Lu-Mi 19:00', 50000, '2024-11-01'),
('Sensei Tanaka', 'KARATE', 'Ma-Ju 18:00', 60000, '2024-11-05'),
('Carlos Gracie', 'JIU JITSU', 'Lu-Vi 20:00', 70000, '2024-11-02'),
('Ana Strong', 'CALISTENIA', 'Sa 10:00', 40000, '2024-11-10'),
('Sofia Dance', 'JAZZ DANCE', 'Vi 17:00', 45000, '2024-11-01');

-- Alumno de prueba para Salsa
INSERT INTO alumnos (profesor_id, nombre_completo, run, email, telefono, valor_plan, fecha_ultimo_pago)
VALUES (1, 'Pedro Alumno', '12.345.678-9', 'pedro@mail.com', '+56912345678', 25000, '2024-10-01');

-- ============================================
-- POLÍTICAS DE SEGURIDAD (Row Level Security)
-- ============================================
-- Habilitar RLS en las tablas
ALTER TABLE profesores ENABLE ROW LEVEL SECURITY;
ALTER TABLE alumnos ENABLE ROW LEVEL SECURITY;

-- Política: Permitir lectura pública (puedes ajustar según tus necesidades)
CREATE POLICY "Permitir lectura pública de profesores" ON profesores
    FOR SELECT USING (true);

CREATE POLICY "Permitir lectura pública de alumnos" ON alumnos
    FOR SELECT USING (true);

-- Política: Permitir todas las operaciones para usuarios autenticados
-- (En producción, deberías usar service_role key o políticas más específicas)
CREATE POLICY "Permitir todo a usuarios autenticados - profesores" ON profesores
    FOR ALL USING (true);

CREATE POLICY "Permitir todo a usuarios autenticados - alumnos" ON alumnos
    FOR ALL USING (true);
