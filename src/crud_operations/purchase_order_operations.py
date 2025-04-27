from db_connection import get_connection

def create_purchase_order(supplier_id, order_date, expected_delivery_date, status, total_amount):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Purchase_Order (supplier_id, order_date, expected_delivery_date, status, total_amount)
             VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(sql, (supplier_id, order_date, expected_delivery_date, status, total_amount))
    conn.commit()
    po_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return po_id

def read_purchase_order(po_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Purchase_Order WHERE po_id = %s"
    cursor.execute(sql, (po_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_purchase_order(po_id, supplier_id, order_date, expected_delivery_date, status, total_amount):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Purchase_Order
             SET supplier_id = %s, order_date = %s, expected_delivery_date = %s, status = %s, total_amount = %s
             WHERE po_id = %s'''
    cursor.execute(sql, (supplier_id, order_date, expected_delivery_date, status, total_amount, po_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_purchase_order(po_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Purchase_Order WHERE po_id = %s"
    cursor.execute(sql, (po_id,))
    conn.commit()
    cursor.close()
    conn.close()

def add_book_to_purchase_order(po_id, book_id, quantity, unit_cost):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO Purchase_Order_Detail (po_id, book_id, quantity, unit_cost)
             VALUES (%s, %s, %s, %s)'''
    cursor.execute(sql, (po_id, book_id, quantity, unit_cost))
    conn.commit()
    cursor.close()
    conn.close()

def update_purchase_order_detail(po_detail_id, quantity, unit_cost):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''UPDATE Purchase_Order_Detail
             SET quantity = %s, unit_cost = %s
             WHERE po_detail_id = %s'''
    cursor.execute(sql, (quantity, unit_cost, po_detail_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_purchase_order_detail(po_detail_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Purchase_Order_Detail WHERE po_detail_id = %s"
    cursor.execute(sql, (po_detail_id,))
    conn.commit()
    cursor.close()
    conn.close()