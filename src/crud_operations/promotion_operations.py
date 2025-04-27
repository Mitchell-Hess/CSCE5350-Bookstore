from db_connection import get_connection

def create_promotion(name, description, discount_percentage, start_date, end_date):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Promotion (name, description, discount_percentage, start_date, end_date)
             VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(sql, (name, description, discount_percentage, start_date, end_date))
    conn.commit()
    promotion_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return promotion_id

def add_book_to_promotion(promotion_id, book_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Promotion_Book (promotion_id, book_id)
             VALUES (%s, %s)'''
    cursor.execute(sql, (promotion_id, book_id))
    conn.commit()
    cursor.close()
    conn.close()

def update_promotion(promotion_id, name, description, discount_percentage, start_date, end_date):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Promotion
             SET name = %s, description = %s, discount_percentage = %s, start_date = %s, end_date = %s
             WHERE promotion_id = %s'''
    cursor.execute(sql, (name, description, discount_percentage, start_date, end_date, promotion_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_promotion(promotion_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Promotion WHERE promotion_id = %s"
    cursor.execute(sql, (promotion_id,))
    conn.commit()
    cursor.close()
    conn.close()