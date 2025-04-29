from db_connection import get_connection

def create_contact(email, phone):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Contact (email, phone)
             VALUES (%s, %s)'''
    cursor.execute(sql, (email, phone))
    conn.commit()
    cursor.close()
    conn.close()

def update_contact(contact_id, email, phone):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Contact
             SET email = %s, phone = %s
             WHERE contact_id = %s'''
    cursor.execute(sql, (email, phone, contact_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_contact(contact_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Contact WHERE contact_id = %s"
    cursor.execute(sql, (contact_id,))
    conn.commit()
    cursor.close()
    conn.close()