USE banking_platform;

-- SELECT * FROM users;

-- DROP TABLE users;

-- CREATE TABLE users (
--     user_id INT AUTO_INCREMENT PRIMARY KEY,
--     full_name VARCHAR(255) NOT NULL,
--     mailing_address VARCHAR(255) NOT NULL,
--     date_of_birth DATE NOT NULL,
--     phone_number VARCHAR(15),
--     email_address VARCHAR(100) NOT NULL,
--     ssn CHAR(9) NOT NULL,
--     UNIQUE (ssn),
--     UNIQUE (email_address)
-- );

-- DESCRIBE users;

-- INSERT INTO users (full_name, mailing_address, date_of_birth, phone_number, email_address, ssn) 
-- VALUES
--     ('John Doe', '123 Queen St, Toronto, ON, M5V 2B8', '1985-05-15', '123-45-6789', 'johndoe@email.com', '123456789'),
--     ('Jane Smith', '456 Maple Rd, Montreal, QC, H3A 2A5', '1990-08-25', '514-987-6543', 'janesmith@email.com', '223456789'),
--     ('Bob Johnson', '789 Birch St, Vancouver, BC, V6B 1A9', '1982-11-10', '604-555-5555', 'bobjohnson@email.com', '323456789');