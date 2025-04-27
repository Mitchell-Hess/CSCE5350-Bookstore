from db_connection import get_connection

def create_customer(first_name, last_name, email, phone, address, registration_date):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Customer (first_name, last_name, email, phone, address, registration_date)
             VALUES (%s, %s, %s, %s, %s, %s)'''
    cursor.execute(sql, (first_name, last_name, email, phone, address, registration_date))
    conn.commit()
    cursor.close()
    conn.close()

def read_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Customer WHERE customer_id = %s"
    cursor.execute(sql, (customer_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_customer(customer_id, first_name, last_name, email, phone, address):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Customer
             SET first_name = %s, last_name = %s, email = %s, phone = %s, address = %s
             WHERE customer_id = %s'''
    cursor.execute(sql, (first_name, last_name, email, phone, address, customer_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Customer WHERE customer_id = %s"
    cursor.execute(sql, (customer_id,))
    conn.commit()
    cursor.close()
    conn.close()


# MEMBERSHIP CRUD

def create_membership(customer_id, level, join_date, expiration_date, points_balance):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Membership (customer_id, level, join_date, expiration_date, points_balance)
             VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(sql, (customer_id, level, join_date, expiration_date, points_balance))
    conn.commit()
    cursor.close()
    conn.close()

def read_membership(membership_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Membership WHERE membership_id = %s"
    cursor.execute(sql, (membership_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_membership(membership_id, level, join_date, expiration_date, points_balance):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Membership
             SET level = %s, join_date = %s, expiration_date = %s, points_balance = %s
             WHERE membership_id = %s'''
    cursor.execute(sql, (level, join_date, expiration_date, points_balance, membership_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_membership(membership_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Membership WHERE membership_id = %s"
    cursor.execute(sql, (membership_id,))
    conn.commit()
    cursor.close()
    conn.close()


# BOOK SEARCH FUNCTIONS

def search_books_by_title(title):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Book WHERE title LIKE %s"
    cursor.execute(sql, (f"%{title}%",))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def search_books_by_author(author_name):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''SELECT Book.* FROM Book
             JOIN Book_Author ON Book.book_id = Book_Author.book_id
             JOIN Author ON Book_Author.author_id = Author.author_id
             WHERE CONCAT(Author.first_name, ' ', Author.last_name) LIKE %s'''
    cursor.execute(sql, (f"%{author_name}%",))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def search_books_by_isbn(isbn):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Book WHERE ISBN = %s"
    cursor.execute(sql, (isbn,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def search_books_by_genre(genre_name):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''SELECT Book.* FROM Book
             JOIN Book_Genre ON Book.book_id = Book_Genre.book_id
             JOIN Genre ON Book_Genre.genre_id = Genre.genre_id
             WHERE Genre.name LIKE %s'''
    cursor.execute(sql, (f"%{genre_name}%",))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


# ORDER / CART / CHECKOUT FUNCTIONS

def create_order(customer_id, order_date, total_amount, status, payment_method):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO `Order` (customer_id, order_date, total_amount, status, payment_method)
             VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(sql, (customer_id, order_date, total_amount, status, payment_method))
    conn.commit()
    order_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return order_id

def add_book_to_order(order_id, book_id, quantity, unit_price, discount):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Order_Detail (order_id, book_id, quantity, unit_price, discount)
             VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(sql, (order_id, book_id, quantity, unit_price, discount))
    conn.commit()
    cursor.close()
    conn.close()

def complete_order(order_id):
    conn = get_connection()
    cursor = conn.cursor()
    # Get order details
    cursor.execute("SELECT book_id, quantity FROM Order_Detail WHERE order_id = %s", (order_id,))
    items = cursor.fetchall()
    for book_id, quantity in items:
        cursor.execute("UPDATE Inventory SET quantity_in_stock = quantity_in_stock - %s WHERE book_id = %s", (quantity, book_id))
    cursor.execute("UPDATE `Order` SET status = 'Completed' WHERE order_id = %s", (order_id,))
    conn.commit()
    cursor.close()
    conn.close()

def apply_membership_discount(order_id, discount_percentage):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT total_amount FROM `Order` WHERE order_id = %s", (order_id,))
    total = cursor.fetchone()
    if total:
        new_total = total[0] * (1 - discount_percentage / 100)
        cursor.execute("UPDATE `Order` SET total_amount = %s WHERE order_id = %s", (new_total, order_id))
        conn.commit()
    cursor.close()
    conn.close()
