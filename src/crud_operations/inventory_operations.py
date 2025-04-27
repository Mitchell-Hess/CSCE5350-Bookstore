from db_connection import get_connection

def create_book(ISBN, title, publication_date, edition, price, page_count, description, publisher_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Book (ISBN, title, publication_date, edition, price, page_count, description, publisher_id)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
    cursor.execute(sql, (ISBN, title, publication_date, edition, price, page_count, description, publisher_id))
    conn.commit()
    cursor.close()
    conn.close()

def read_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Book WHERE book_id = %s"
    cursor.execute(sql, (book_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_book(book_id, ISBN, title, publication_date, edition, price, page_count, description, publisher_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Book
             SET ISBN = %s, title = %s, publication_date = %s, edition = %s, price = %s, page_count = %s, description = %s, publisher_id = %s
             WHERE book_id = %s'''
    cursor.execute(sql, (ISBN, title, publication_date, edition, price, page_count, description, publisher_id, book_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Book WHERE book_id = %s"
    cursor.execute(sql, (book_id,))
    conn.commit()
    cursor.close()
    conn.close()

def create_inventory_entry(book_id, quantity_in_stock, last_restock_date, location_in_store):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Inventory (book_id, quantity_in_stock, last_restock_date, location_in_store)
             VALUES (%s, %s, %s, %s)'''
    cursor.execute(sql, (book_id, quantity_in_stock, last_restock_date, location_in_store))
    conn.commit()
    cursor.close()
    conn.close()

def read_inventory_by_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Inventory WHERE book_id = %s"
    cursor.execute(sql, (book_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_inventory(inventory_id, quantity_in_stock, last_restock_date, location_in_store):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Inventory
             SET quantity_in_stock = %s, last_restock_date = %s, location_in_store = %s
             WHERE inventory_id = %s'''
    cursor.execute(sql, (quantity_in_stock, last_restock_date, location_in_store, inventory_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_inventory(inventory_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Inventory WHERE inventory_id = %s"
    cursor.execute(sql, (inventory_id,))
    conn.commit()
    cursor.close()
    conn.close()