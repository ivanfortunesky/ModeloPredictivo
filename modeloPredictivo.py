import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('decision_tree.db')
c = conn.cursor()

# Crear la tabla
c.execute('''CREATE TABLE IF NOT EXISTS data (
                Tid INTEGER PRIMARY KEY,
                Propietario TEXT,git pull
                Talle TEXT,
                Sueldo TEXT,
                Deudor TEXT
            )''')

# Insertar los datos - Meto TODOS los datos juntos
data = [
    (1, 'Yes', 'Large', '125K', 'No'),
    (2, 'No', 'Medium', '100K', 'No'),
    (3, 'No', 'Small', '70K', 'No'),
    (4, 'Yes', 'Medium', '120K', 'No'),
    (5, 'No', 'Large', '95K', 'Yes'),
    (6, 'No', 'Medium', '60K', 'No'),
    (7, 'Yes', 'Large', '220K', 'No'),
    (8, 'No', 'Small', '85K', 'Yes'),
    (9, 'No', 'Medium', '75K', 'No'),
    (10, 'No', 'Small', '90K', 'Yes'),
    (11, 'No', 'Small', '55K', '?'),
    (12, 'Yes', 'Medium', '80K', '?'),
    (13, 'Yes', 'Large', '110K', '?'),
    (14, 'No', 'Small', '95K', '?'),
    (15, 'No', 'Large', '67K', '?')
]

c.executemany('INSERT INTO data VALUES (?, ?, ?, ?, ?)', data)
conn.commit()
conn.close()

#
