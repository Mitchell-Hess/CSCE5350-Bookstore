from db_connection import get_connection



def customer_exists(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM Customer WHERE customer_id = %s", (customer_id,))
    exists = cursor.fetchone() is not None
    cursor.close()
    conn.close()
    return exists

def grant_membership_to_customer(customer_id, level):
    from datetime import datetime, timedelta
    conn = get_connection()
    cursor = conn.cursor()
    join_date = datetime.now().date()
    expiration_date = join_date + timedelta(days=365)
    points_balance = 0

    sql = """
    INSERT INTO Membership (customer_id, join_date, expiration_date, level, points_balance)
    VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        join_date = VALUES(join_date),
        expiration_date = VALUES(expiration_date),
        level = VALUES(level),
        points_balance = VALUES(points_balance)
    """
    cursor.execute(sql, (customer_id, join_date, expiration_date, level, points_balance))
    conn.commit()
    cursor.close()
    conn.close()
