from db_connection import get_connection
import datetime

def create_employee(first_name, last_name, position, hire_date, salary, store_id, contact_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Employee (first_name, last_name, position, hire_date, salary, store_id, contact_id)
             VALUES (%s, %s, %s, %s, %s, %s, %s)'''
    cursor.execute(sql, (first_name, last_name, position, hire_date, salary, store_id, contact_id))
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

def update_employee(employee_id, first_name, last_name, position, hire_date, salary, store_id, contact_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Employee
             SET first_name = %s, last_name = %s, position = %s, hire_date = %s, salary = %s, store_id = %s, contact_id = %s
             WHERE employee_id = %s'''
    cursor.execute(sql, (first_name, last_name, position, hire_date, salary, store_id, contact_id, employee_id))
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

def get_all_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT employee_id, first_name, last_name, position, hire_date, salary,store_id , contact_id "
        "FROM Employee"
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


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

def clock_in_employee(emp_id, clock_in_time):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO employee_shifts (employee_id, clock_in_time) VALUES (%s, %s)"
    cursor.execute(query, (emp_id, clock_in_time))

    conn.commit()
    cursor.close()
    conn.close()
def clock_out_employee(employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        UPDATE employee_shifts
        SET clock_out_time = NOW()
        WHERE employee_id = %s AND clock_out_time IS NULL
        ORDER BY clock_in_time DESC
        LIMIT 1
    """
    cursor.execute(query, (employee_id,))
    conn.commit()
    affected_rows = cursor.rowcount
    conn.close()
    return affected_rows