import sqlite3

def create_table():
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Patients (
            id TEXT PRIMARY KEY,
            name TEXT,
            gender TEXT,
            dob TEXT,
            address TEXT,
            contact TEXT
        )
    ''')
    conn.commit()
    conn.close()

def fetch_patients():
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Patients')
    patients = cursor.fetchall()
    conn.close()
    return patients

def insert_patient(id, name, gender, dob, address, contact):
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Patients (id, name, gender, dob, address, contact) VALUES (?,?,?,?,?,?)', (id, name, gender, dob, address, contact))
    conn.commit()
    conn.close()

def delete_patient(id):
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Patients WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def update_patient(new_name, new_gender, new_dob, new_address, new_contact, id):
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Patients SET name = ?, gender = ?, dob = ?, address = ?, contact = ? WHERE id = ?', (new_name, new_gender, new_dob, new_address, new_contact, id))
    conn.commit()
    conn.close()

def id_exists(id):
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Patients WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

create_table()

