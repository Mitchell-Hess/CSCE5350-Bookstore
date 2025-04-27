from db_connection import get_connection

def create_store(name, address, phone, email, opening_hours):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Store (name, address, phone, email, opening_hours)
             VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(sql, (name, address, phone, email, opening_hours))
    conn.commit()
    cursor.close()
    conn.close()

def read_store(store_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Store WHERE store_id = %s"
    cursor.execute(sql, (store_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_store(store_id, name, address, phone, email, opening_hours):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Store
             SET name = %s, address = %s, phone = %s, email = %s, opening_hours = %s
             WHERE store_id = %s'''
    cursor.execute(sql, (name, address, phone, email, opening_hours, store_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_store(store_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Store WHERE store_id = %s"
    cursor.execute(sql, (store_id,))
    conn.commit()
    cursor.close()
    conn.close()

def create_supplier(name, contact_person, phone, email, lead_time_days):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Supplier (name, contact_person, phone, email, lead_time_days)
             VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(sql, (name, contact_person, phone, email, lead_time_days))
    conn.commit()
    cursor.close()
    conn.close()

def read_supplier(supplier_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Supplier WHERE supplier_id = %s"
    cursor.execute(sql, (supplier_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_supplier(supplier_id, name, contact_person, phone, email, lead_time_days):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Supplier
             SET name = %s, contact_person = %s, phone = %s, email = %s, lead_time_days = %s
             WHERE supplier_id = %s'''
    cursor.execute(sql, (name, contact_person, phone, email, lead_time_days, supplier_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_supplier(supplier_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Supplier WHERE supplier_id = %s"
    cursor.execute(sql, (supplier_id,))
    conn.commit()
    cursor.close()
    conn.close()