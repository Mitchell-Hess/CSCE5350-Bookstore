from db_connection import get_connection

def create_employee(first_name, last_name, position, hire_date, salary, email, phone):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Employee (first_name, last_name, position, hire_date, salary, email, phone)
             VALUES (%s, %s, %s, %s, %s, %s, %s)'''
    cursor.execute(sql, (first_name, last_name, position, hire_date, salary, email, phone))
    conn.commit()
    cursor.close()
    conn.close()

def read_employee(employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Employee WHERE employee_id = %s"
    cursor.execute(sql, (employee_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_employee(employee_id, first_name, last_name, position, hire_date, salary, email, phone):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Employee
             SET first_name = %s, last_name = %s, position = %s, hire_date = %s, salary = %s, email = %s, phone = %s
             WHERE employee_id = %s'''
    cursor.execute(sql, (first_name, last_name, position, hire_date, salary, email, phone, employee_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_employee(employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Employee WHERE employee_id = %s"
    cursor.execute(sql, (employee_id,))
    conn.commit()
    cursor.close()
    conn.close()

def create_shift(employee_id, start_time, end_time, date):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Shift (employee_id, start_time, end_time, date)
             VALUES (%s, %s, %s, %s)'''
    cursor.execute(sql, (employee_id, start_time, end_time, date))
    conn.commit()
    cursor.close()
    conn.close()

def read_shift(shift_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Shift WHERE shift_id = %s"
    cursor.execute(sql, (shift_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_shift(shift_id, employee_id, start_time, end_time, date):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Shift
             SET employee_id = %s, start_time = %s, end_time = %s, date = %s
             WHERE shift_id = %s'''
    cursor.execute(sql, (employee_id, start_time, end_time, date, shift_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_shift(shift_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Shift WHERE shift_id = %s"
    cursor.execute(sql, (shift_id,))
    conn.commit()
    cursor.close()
    conn.close()