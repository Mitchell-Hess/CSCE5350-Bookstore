from db_connection import get_connection

def create_review(book_id, customer_id, rating, comment, review_date):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Review (book_id, customer_id, rating, comment, review_date)
             VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(sql, (book_id, customer_id, rating, comment, review_date))
    conn.commit()
    cursor.close()
    conn.close()

def read_reviews_for_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Review WHERE book_id = %s"
    cursor.execute(sql, (book_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def update_review(review_id, rating, comment, review_date):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Review
             SET rating = %s, comment = %s, review_date = %s
             WHERE review_id = %s'''
    cursor.execute(sql, (rating, comment, review_date, review_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_review(review_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Review WHERE review_id = %s"
    cursor.execute(sql, (review_id,))
    conn.commit()
    cursor.close()
    conn.close()
