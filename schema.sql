-- schema.sql
DROP TABLE IF EXISTS profesores;
DROP TABLE IF EXISTS alumnos;

-- Tabla de Profesores (Uno por disciplina para el demo)
CREATE TABLE profesores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    disciplina TEXT NOT NULL,
    horario TEXT NOT NULL,
    pago_mensual_gym INTEGER NOT NULL, -- Lo que el profe paga al gym
    fecha_pago_profe DATE NOT NULL
);

-- Tabla de Alumnos
CREATE TABLE alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profesor_id INTEGER NOT NULL,
    nombre_completo TEXT NOT NULL,
    run TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL,
    valor_plan INTEGER NOT NULL,
    fecha_ultimo_pago DATE NOT NULL,
    asistencia_confirmada BOOLEAN DEFAULT 0,
    FOREIGN KEY (profesor_id) REFERENCES profesores (id)
);

-- Datos Semilla (Demo: 1 profe por disciplina)
INSERT INTO profesores (nombre, disciplina, horario, pago_mensual_gym, fecha_pago_profe) VALUES
('Juan Pérez', 'SALSA', 'Lu-Mi 19:00', 50000, '2023-11-01'),
('Sensei Tanaka', 'KARATE', 'Ma-Ju 18:00', 60000, '2023-11-05'),
('Carlos Gracie', 'JIU JITSU', 'Lu-Vi 20:00', 70000, '2023-11-02'),
('Ana Strong', 'CALISTENIA', 'Sa 10:00', 40000, '2023-11-10'),
('Sofia Dance', 'JAZZ DANCE', 'Vi 17:00', 45000, '2023-11-01');

-- Un alumno de prueba para Salsa
INSERT INTO alumnos (profesor_id, nombre_completo, run, email, telefono, valor_plan, fecha_ultimo_pago)
VALUES (1, 'Pedro Alumno', '12.345.678-9', 'pedro@mail.com', '+56912345678', 25000, '2023-10-01');