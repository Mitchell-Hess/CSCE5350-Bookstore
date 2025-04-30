from db_connection import get_connection

def create_publisher(name, address, website, contact_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO publisher (name, address, website, contact_id)
             VALUES (%s, %s, %s, %s)'''
    cursor.execute(sql, (name, address, website, contact_id))
    conn.commit()
    cursor.close()
    conn.close()

def update_publisher(publisher_id, name, address, website, contact_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE publisher
             SET name = %s, address = %s, website = %s, contact_id = %s
             WHERE publisher_id = %s'''
    cursor.execute(sql, (name, address, website, contact_id, publisher_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_publisher(publisher_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM publisher WHERE publisher_id = %s"
    cursor.execute(sql, (publisher_id,))
    conn.commit()
    cursor.close()
    conn.close()

def create_book(ISBN, title, publication_date, edition, price, page_count, description, publisher_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO book (ISBN, title, publication_date, edition, price, page_count, description, publisher_id)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
    cursor.execute(sql, (ISBN, title, publication_date, edition, price, page_count, description, publisher_id))
    book_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return book_id

def read_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM book WHERE book_id = %s"
    cursor.execute(sql, (book_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_book(book_id, ISBN, title, publication_date, edition, price, page_count, description, publisher_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE book
             SET ISBN = %s, title = %s, publication_date = %s, edition = %s, price = %s, page_count = %s, description = %s, publisher_id = %s
             WHERE book_id = %s'''
    cursor.execute(sql, (ISBN, title, publication_date, edition, price, page_count, description, publisher_id, book_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM book WHERE book_id = %s"
    cursor.execute(sql, (book_id,))
    conn.commit()
    cursor.close()
    conn.close()

def create_book_author(book_id, author_id, role):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO book_author (book_id, author_id, role)
             VALUES (%s, %s, %s)'''
    cursor.execute(sql, (book_id, author_id, role))
    conn.commit()
    cursor.close()
    conn.close()

def delete_book_author(book_id, author_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM book_author WHERE book_id = %s AND author_id = %s"
    cursor.execute(sql, (book_id, author_id))
    conn.commit()
    cursor.close()
    conn.close()

def find_author_id(first_name, last_name):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT author_id FROM author WHERE first_name = %s and last_name = %s"
    cursor.execute(sql, (first_name, last_name))
    author_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return author_id

def find_publisher_id(publisher_name):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT publisher_id FROM publisher WHERE publisher_name = %s"
    cursor.execute(sql, (publisher_name))
    author_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return author_id

def create_inventory_entry(book_id, quantity_in_stock, last_restock_date, location_in_store):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO inventory (book_id, quantity_in_stock, last_restock_date, location_in_store)
             VALUES (%s, %s, %s, %s)'''
    cursor.execute(sql, (book_id, quantity_in_stock, last_restock_date, location_in_store))
    conn.commit()
    cursor.close()
    conn.close()

def read_inventory_by_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM inventory WHERE book_id = %s"
    cursor.execute(sql, (book_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_inventory(inventory_id, quantity_in_stock, last_restock_date, location_in_store):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE inventory
             SET quantity_in_stock = %s, last_restock_date = %s, location_in_store = %s
             WHERE inventory_id = %s'''
    cursor.execute(sql, (quantity_in_stock, last_restock_date, location_in_store, inventory_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_inventory(inventory_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM inventory WHERE inventory_id = %s"
    cursor.execute(sql, (inventory_id,))
    conn.commit()
    cursor.close()
    conn.close()