CREATE TABLE "User" (
    id SERIAL PRIMARY KEY,
    user_type VARCHAR(5),
    name VARCHAR(50),
    email VARCHAR(50) 
);

INSERT INTO "User" (user_type, name, email) VALUES
('Host', 'Mykola', 'mykola@gmail.com'),
('Guest', 'Kateryna', 'kat@gmail.com'),
('Guest', 'Oreo', 'oreo@gmail.com'),
('Guest', 'David', 'david@gmail.com'),
('Guest', 'Taras', 'taras@gmail.com');	


CREATE TABLE room (
    room_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES "User"(id),
    title VARCHAR(50),
    price DECIMAL(10, 2),
    ac BOOLEAN,
    refrigerator BOOLEAN,
    description TEXT,
    available_from_date DATE,
    available_till_date DATE
);


INSERT INTO room (user_id, title, price, ac, refrigerator, description, available_from_date, available_till_date) VALUES
(1, 'Cozy room', 34.00, TRUE, TRUE, 'Include balcony', '2024-05-20', '2024-05-31'),
(1, 'Big apartment', 70.00, TRUE, TRUE, 'Beautiful city view and pool', '2024-05-20', '2024-06-20'),
(1, 'Studio with kitchen', 25.00, FALSE, TRUE, 'Cozy room with nearest bus stop', '2024-05-25', '2024-06-07');


CREATE TABLE reservation (
    reservation_id SERIAL PRIMARY KEY,
    room_id INT REFERENCES room(room_id),
    guest_id INT REFERENCES "User"(id),
    check_in_date DATE,
    check_out_date DATE,
    total_price DECIMAL(10, 2)
);


INSERT INTO reservation (room_id, guest_id, check_in_date, check_out_date, total_price) VALUES
(1, 2, '2024-05-20', '2024-05-25', 170.00),
(2, 2, '2024-06-01', '2024-06-10', 630.00),
(3, 3, '2024-05-25', '2024-06-05', 275.00),
(2, 4, '2024-06-05', '2024-06-12', 490.00),
(3, 5, '2024-06-15', '2024-06-20', 125.00);


CREATE TABLE payment (
    payment_id SERIAL PRIMARY KEY,
    reservation_id INT REFERENCES reservation(reservation_id),
    user_id INT REFERENCES "User"(id),
    amount DECIMAL(10, 2),
    payment_method VARCHAR(20),
    payment_date DATE
);


INSERT INTO payment (reservation_id, user_id, amount, payment_method, payment_date) VALUES
(1, 2, 170.00, 'Credit Card', '2024-05-18'),
(2, 2, 630.00, 'PayPal', '2024-06-02'),
(3, 3, 275.00, 'Bank Transfer', '2024-05-26');


CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    room_id INT REFERENCES room(room_id),
    guest_id INT REFERENCES "User"(id),
    rating INT,
    review_date DATE
);


INSERT INTO reviews (room_id, guest_id, rating, review_date) VALUES
(1, 2, 5, '2024-05-30'),
(2, 2, 4, '2024-06-15'),
(3, 3, 3, '2024-06-07');


COMMIT;
