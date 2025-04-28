CREATE DATABASE IF NOT EXISTS Bookstore;
USE Bookstore;

-- Core Entities
CREATE TABLE Author (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    birth_date DATE,
    nationality VARCHAR(100),
    biography TEXT
);

CREATE TABLE Publisher (
    publisher_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    website VARCHAR(255)
);

CREATE TABLE Genre (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);

CREATE TABLE Book (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    ISBN VARCHAR(20),
    title VARCHAR(255),
    publication_date DATE,
    edition VARCHAR(50),
    price DECIMAL(10, 2),
    page_count INT,
    description TEXT,
    publisher_id INT,
    FOREIGN KEY (publisher_id) REFERENCES Publisher(publisher_id)
);

CREATE TABLE Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    registration_date DATE
);

-- Inventory & Sales
CREATE TABLE Inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    quantity_in_stock INT,
    last_restock_date DATE,
    location_in_store VARCHAR(100),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

CREATE TABLE `Order` (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    status VARCHAR(50),
    payment_method VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Order_Detail (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity INT,
    unit_price DECIMAL(10, 2),
    discount DECIMAL(5, 2),
    FOREIGN KEY (order_id) REFERENCES `Order`(order_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

CREATE TABLE Employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    position VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10, 2),
    email VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE Shift (
    shift_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    start_time TIME,
    end_time TIME,
    date DATE,
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
);

-- Store Operations
CREATE TABLE Store (
    store_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    opening_hours VARCHAR(100)
);

CREATE TABLE Supplier (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    contact_person VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    lead_time_days INT
);

CREATE TABLE Purchase_Order (
    po_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_id INT,
    order_date DATE,
    expected_delivery_date DATE,
    status VARCHAR(50),
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id)
);

CREATE TABLE Purchase_Order_Detail (
    po_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    po_id INT,
    book_id INT,
    quantity INT,
    unit_cost DECIMAL(10, 2),
    FOREIGN KEY (po_id) REFERENCES Purchase_Order(po_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

-- Additional Features
CREATE TABLE Review (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    customer_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    review_date DATE,
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Book_Author (
    book_id INT,
    author_id INT,
    role VARCHAR(100),
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (author_id) REFERENCES Author(author_id)
);

CREATE TABLE Book_Genre (
    book_id INT,
    genre_id INT,
    PRIMARY KEY (book_id, genre_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);

CREATE TABLE Promotion (
    promotion_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    discount_percentage DECIMAL(5, 2),
    start_date DATE,
    end_date DATE
);

CREATE TABLE Promotion_Book (
    promotion_id INT,
    book_id INT,
    PRIMARY KEY (promotion_id, book_id),
    FOREIGN KEY (promotion_id) REFERENCES Promotion(promotion_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

CREATE TABLE Membership (
    membership_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    level VARCHAR(50),
    join_date DATE,
    expiration_date DATE,
    points_balance INT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);