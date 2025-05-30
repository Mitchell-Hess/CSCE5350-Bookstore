-- 1. Contact
INSERT INTO Contact (email, phone)
VALUES
('contact@publisher1.com', '111-234-3456'),
('contact@publisher2.com', '111-764-0294'),
('contact@publisher3.com', '111-859-0129'),
('contact@publisher4.com', '111-459-2348'),
('contact@publisher5.com', '111-394-5834'),
('contact@supplier1.com', '222-234-3456'),
('contact@supplier2.com', '222-764-0294'),
('contact@supplier3.com', '222-859-0129'),
('contact@supplier4.com', '222-459-2348'),
('contact@supplier5.com', '222-394-5834'),
('contact@employee1.com', '333-234-3456'),
('contact@employee2.com', '333-764-0294'),
('contact@employee3.com', '333-859-0129'),
('contact@employee4.com', '333-459-2348'),
('contact@employee5.com', '333-394-5834'),
('contact@store1.com', '444-234-3456'),
('contact@store2.com', '444-764-0294'),
('contact@store3.com', '444-859-0129'),
('contact@customer1.com', '555-234-3456'),
('contact@customer2.com', '555-764-0294'),
('contact@customer3.com', '555-859-0129'),
('contact@customer4.com', '555-459-2348'),
('contact@customer5.com', '5552-394-5834');

-- 1. Publisher
INSERT INTO Publisher (name, address, website, contact_id)
VALUES
('Belhune Publishing', '8 Arch Ave, Indianapolis, IN', 'www.BelhunePublishing.com', 1),
('Bento Books','400 Millet Blvd, New York, NY', 'www.BentoBooks.com', 2),
('Cleis Press','9800 Datrod Rd, El Paso, TX', 'www.CleisPress.com', 3),
('Paton Press', '11 Mallard St, Normal, IL', 'www.PatonPress.com', 4),
('Epic Reads', '654 York Ln, Denton, TX', 'www.epicreads.com', 5);

-- 2. Book
INSERT INTO Book (ISBN, title, publication_date, edition, price, page_count, description, publisher_id)
VALUES 
('0793162484100', 'Introduction to MySQL','2020-01-15', '1st', 39.99, 300, 'An introduction to MySQL.', 1),
('1723131484101', 'Chemistry for beginners','2019-07-10', '2nd', 29.98, 350, 'An introduction to Chemistry', 1),
('4781161474132', 'Database Design','2021-03-20', '1st', 34.99, 400, 'Fundamental concepts for designing relational databases.', 2),
('5723161484103', 'Learning Python','2018-05-25', '3rd', 39.99, 450, 'Comprehensive Python programming guide.', 3),
('0783161484104', 'Romeo and Juliet',   '2022-07-11', '1st', 15.99, 150, 'Love story of Romeo and Juliet', 5);

-- 3. Author
INSERT INTO Author (first_name, last_name, birth_date, nationality, biography)
VALUES
('Abby','Dogg','1999-05-20', 'American', 'Expert in database systems.'),
('Mitchell','Dregg', '1995-07-15', 'Indian', 'Author in SQL programming.'),
('Carl','Hang','1985-12-08', 'British',  'Technical writer'),
('Bet', 'Sack','1990-02-28', 'Ghanaian',  'Author of Love stories'),
('Pei','Geng','1972-11-10', 'Chinese',  'Database performance expert.');

-- 4. Genre
INSERT INTO Genre (name, description)
VALUES
('Technology', 'Books related to technology and computing.'),
('Fiction',    'Fictional stories and narratives.'),
('Non-fiction','Informative non-fiction books covering various topics.'),
('Science',    'Books on scientific and technology topics.'),
('Biography',  'Life stories of notable individuals.');

-- 5. Customer
INSERT INTO Customer (first_name, last_name, address, registration_date, contact_id)
VALUES
('Liz','Pott', '789 Maple St, Denton, TX', '2021-11-01', 19),
('Bobby', 'Wills', '122 Hope St, Metro, NY', '2023-01-15', 20),
('Brown','Rice', '2 Pinnal St, youngtown, OH', '2024-01-20', 21),
('Yu', 'Princes', '300 Elmis St, New York City, NY','2025-03-05', 22),
('Bimbo','Ade', '404 Oak St, Chicago, IL', '2025-03-20', 23);

-- 6. Inventory
INSERT INTO Inventory (book_id, quantity_in_stock, last_restock_date, location_in_store)
VALUES
(1, 40, '2025-03-01', 'Aisle 1'),
(2, 30, '2024-12-05', 'Aisle 2'),
(3, 25, '2025-08-07', 'Aisle 2'),
(4, 20, '2024-11-10', 'Aisle 4'),
(5, 23, '2025-01-30', 'Aisle 3');

-- 7. Order
INSERT INTO `Order` (customer_id, order_date, total_amount, status, payment_method)
VALUES
(1, '2023-08-01', 59.98, 'Completed','Credit Card'),
(2, '2023-09-30', 50.99, 'Completed', 'PayPal'),
(4, '2024-09-03', 89.97, 'Completed','Debit Card'),
(2, '2024-12-30', 98.96, 'Pending', 'Credit Card'),
(3, '2025-03-05', 49.99,'Processing','PayPal');

-- 8. Order_Detail
INSERT INTO Order_Detail (order_id, book_id, quantity, unit_price, discount)
VALUES
(1, 1, 1, 39.99, 0.00),
(1, 2, 2, 59.96, 1.00),
(2, 1, 1, 39.99, 0.00),
(3, 3, 2, 34.99, 5.00),
(4, 4, 1, 39.99, 0.00);

-- 9. Employee
INSERT INTO Employee (first_name, last_name, position, hire_date, salary, contact_id)
VALUES
('Eva', 'Bogo', 'Manager', '2020-01-10', 65000.00, 11),
('Frank','Brown','Sales Associate', '2021-06-15', 35000.00, 12),
('Bruce', 'Thomp', 'Cashier', '2022-03-01', 40000.00, 13),
('Harry', 'Disks', 'Stock Manager', '2019-11-20', 45000.00, 14),
('Isa', 'Hang', 'Customer Service', '2023-01-05', 35000.00, 15);

-- 10. Shift
INSERT INTO Shift (employee_id, start_time, end_time, date)
VALUES
(1, '2025-04-26 09:00:00', '2025-04-26 17:00:00', '2025-04-26'),
(2, '2025-04-26 10:00:00', '2025-04-26 18:00:00', '2025-04-26'),
(3, '2025-04-27 09:00:00', '2025-04-27 17:00:00', '2025-04-27'),
(4, '2025-04-27 11:00:00', '2025-04-27 19:00:00', '2025-04-27'),
(5, '2025-04-28 08:00:00', '2025-04-28 16:00:00', '2025-04-28');

-- 11. Store
INSERT INTO Store (name, address, opening_hours, contact_id)
VALUES
('Dallas Bookstore', '102 Mingo St, Dallas, TX', '9AM - 9PM', 16),
('Denton Bookstore','200 Colorado Ln, Denton, TX', '10AM - 8PM', 17),
('Plano Bookstore','301 plano road, Plano, TX', '8AM - 10PM', 18);

-- 12. Supplier
INSERT INTO Supplier (name, contact_person, lead_time_days, contact_id)
VALUES
('Independent Publishers Group','Lee Cook', 7, 6),
('Baker & Taylor','Henry Coke', 10, 7),
('Bella Distribution', 'Belle White', 5, 8),
('PrintGoods Ltd.', 'Brown Lings', 14, 9),
('DeVorss Books', 'Oliv Davis', 12, 19);

-- 13. Purchase_Order
INSERT INTO Purchase_Order (supplier_id, order_date, expected_delivery_date, status, total_amount)
VALUES
(1, '2023-08-15', '2023-12-22', 'Delivered', 650.00),
(2, '2024-08-20', '2024-12-27', 'Delivered',300.00),
(3, '2024-10-25', '2025-01-30', 'Delivered', 500.00),
(4, '2025-03-30', '2025-06-06', 'Pending', 450.00),
(5, '2025-04-01', '2025-05-08', 'Processing',700.00);

-- 14. Purchase_Order_Detail
INSERT INTO Purchase_Order_Detail (po_id, book_id, quantity, unit_cost)
VALUES
(1, 1, 20, 25.00),
(2, 2, 15, 28.00),
(3, 3, 30, 30.00),
(4, 4, 25, 27.50),
(5, 5, 40, 10.00);

-- 15. Review
INSERT INTO Review (book_id, customer_id, rating, comment, review_date)
VALUES
(1, 1, 5, 'Excellent introduction to MySQL.I love it', '2022-01-03'),
(2, 2, 5, 'Very informative and good examples', '2023-09-04'),
(1, 3, 3, 'Good but could gave more examples.', '2023-06-15'),
(2, 4, 5, 'Good Python book.', '2024-01-06'),
(5, 5, 4, 'Great love story', '2024-09-07');

-- 16. Book_Author
INSERT INTO Book_Author (book_id, author_id, role)
VALUES
(1, 1, 'Primary Author'),
(2, 2, 'Primary Author'),
(2, 3, 'Co-Author'),
(3, 1, 'Co-Author'),
(4, 4, 'Primary Author');

-- 17. Book_Genre
INSERT INTO Book_Genre (book_id, genre_id)
VALUES
(1, 1),
(2, 1),
(2, 3),
(3, 1),
(4, 4);

-- 18. Promotion
INSERT INTO Promotion (name, description, discount_percentage, start_date, end_date)
VALUES
('Summer Sales','Get 20% off on all technology books.', 20.00, '2025-05-01', '2023-08-30'),
('Back to School Sales', 'Discounts for students on select books.', 10.00, '2025-08-01', '2025-09-01'),
('Holiday Specials', '20% off select titles for holiday season.', 20.00, '2025-01-01', '2025-01-31'),
('Clearance', 'Up to 50% off clearance items.', 50.00, '2025-01-01', '2025-12-30'),
('Black Friday', 'BOGO on select books for Black Friday.', 100.00, '2025-11-20', '2025-12-01');

-- 19. Promotion_Book
INSERT INTO Promotion_Book (promotion_id, book_id)
VALUES
(1, 1),
(2, 2),
(1, 3),
(3, 4),
(5, 5);

-- 20. Membership
INSERT INTO Membership (customer_id, level, join_date, expiration_date, points_balance)
VALUES
(1, 'Premium', '2021-11-01', '2026-11-01', 1500),
(2, 'Basic',   '2023-01-15', '2025-12-15',  500),
(3, 'Basic',   '2024-01-20', '2026-01-20',  200),
(4, 'Premium', '2025-03-05', '2027-03-05',  800),
(5, 'Basic',   '2025-03-30', '2027-03-30',  300);