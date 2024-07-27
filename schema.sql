-- Crear la base de datos (si no existe)
ATTACH DATABASE 'bancos.db' AS bancos;

-- Crear el esquema Institucion (si no existe)
CREATE TABLE IF NOT EXISTS bancos.Institucion (
    sNombre TEXT PRIMARY KEY, 
    bSofipo BOOLEAN,          
    sDescripcion TEXT         
);

-- Crear el esquema Deposito (si no existe)
CREATE TABLE IF NOT EXISTS bancos.Deposito (
    sNombre TEXT,
    nIdInstitucion TEXT,
    sDescripcion TEXT, 
    nMonto REAL,
    nTasaInteresAnual REAL,
    PRIMARY KEY (sNombre, nIdInstitucion),
    FOREIGN KEY (nIdInstitucion) REFERENCES Institucion(sNombre)
);

-- Insertar datos en la tabla Institucion
INSERT OR IGNORE INTO bancos.Institucion (sNombre, bSofipo, sDescripcion)
VALUES
    ('Klar', 1, 'SOFIPO con servicios financieros digitales'),
    ('Nu', 1, 'SOFIPO con servicios financieros digitales'),
    ('MercadoPago', 1, 'SOFIPO con servicios financieros digitales'),
    ('Santander', 0, 'Banco tradicional con servicios financieros completos');
