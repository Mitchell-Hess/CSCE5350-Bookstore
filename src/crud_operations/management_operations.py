from db_connection import get_connection

def create_store(name, address, opening_hours, contact_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Store (name, address, opening_hours, contact_id)
             VALUES (%s, %s, %s, %s)'''
    cursor.execute(sql, (name, address, opening_hours, contact_id))
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

def update_store(store_id, name, address, opening_hours, contact_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Store
             SET name = %s, address = %s, opening_hours = %s, contact_id
             WHERE store_id = %s'''
    cursor.execute(sql, (name, address, opening_hours, contact_id, store_id))
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

def create_supplier(name, contact_person, lead_time_days, contact_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Supplier (name, contact_person, lead_time_days, contact_id)
             VALUES (%s, %s, %s, %s)'''
    cursor.execute(sql, (name, contact_person, lead_time_days, contact_id))
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

def update_supplier(supplier_id, name, contact_person, lead_time_days, contact_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Supplier
             SET name = %s, contact_person = %s, lead_time_days = %s, contact_id
             WHERE supplier_id = %s'''
    cursor.execute(sql, (name, contact_person, lead_time_days, contact_id, supplier_id))
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