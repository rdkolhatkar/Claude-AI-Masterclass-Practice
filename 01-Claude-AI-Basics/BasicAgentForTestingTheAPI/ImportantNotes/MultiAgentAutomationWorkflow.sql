CREATE SCHEMA IF NOT EXISTS MultiAgentAutomationWorkflow;

USE MultiAgentAutomationWorkflow;

CREATE TABLE IF NOT EXISTS Customers (
    unique_Id   INT           NOT NULL AUTO_INCREMENT,
    name        VARCHAR(100)  NOT NULL,
    city        VARCHAR(100)  NOT NULL,
    age         INT           NOT NULL,
    CONSTRAINT pk_customers PRIMARY KEY (unique_Id),
    CONSTRAINT chk_customers_age CHECK (age > 0 AND age <= 150)
);

CREATE TABLE IF NOT EXISTS Orders (
    order_Id     INT           NOT NULL AUTO_INCREMENT,
    customer_Id  INT           NOT NULL,
    subject      VARCHAR(200)  NOT NULL,
    company      VARCHAR(150)  NOT NULL,
    order_date   DATE          NOT NULL,
    CONSTRAINT pk_orders PRIMARY KEY (order_Id),
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_Id)
        REFERENCES Customers (unique_Id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO Customers (name, city, age) VALUES
    ('Aarav Sharma',   'Pune',      28),
    ('Priya Verma',    'Mumbai',    34),
    ('Rahul Mehta',    'Bangalore', 25),
    ('Sneha Kapoor',   'Delhi',     41),
    ('Vikram Singh',   'Hyderabad', 30);


INSERT INTO Orders (customer_Id, subject, company, order_date) VALUES
    (1, 'Laptop Purchase',        'Dell India',       '2026-01-10'),
    (2, 'Office Chairs',          'Godrej Interio',   '2026-02-14'),
    (3, 'Cloud Hosting Plan',     'AWS',              '2026-03-05'),
    (4, 'Software License',       'Microsoft',        '2026-04-22'),
    (5, 'Network Equipment',      'Cisco Systems',    '2026-05-18');


SELECT * FROM Customers;
SELECT * FROM Orders;

CREATE SCHEMA IF NOT EXISTS MultiAgentAutomationWorkflow;

USE MultiAgentAutomationWorkflow;

CREATE TABLE IF NOT EXISTS RegistrationData (
    registration_Id  INT           NOT NULL AUTO_INCREMENT,
    FirstName        VARCHAR(50)   NOT NULL,
    LastName         VARCHAR(50)   NOT NULL,
    Email            VARCHAR(100)  NOT NULL,
    PhoneNumber      VARCHAR(15)   NOT NULL,
    Gender           VARCHAR(10)   NOT NULL,
    Occupation       VARCHAR(50)   NOT NULL DEFAULT 'Student',
    Password         VARCHAR(255)  NOT NULL,
    CONSTRAINT pk_registration_data PRIMARY KEY (registration_Id),
    CONSTRAINT uq_registration_email UNIQUE (Email),
    CONSTRAINT chk_registration_gender CHECK (Gender IN ('Male', 'Female', 'Other'))
);

INSERT INTO RegistrationData (FirstName, LastName, Email, PhoneNumber, Gender, Occupation, Password) VALUES
    ('Aarav',    'Sharma',   'aarav.sharma@example.com',    '9876543210', 'Male',   'Software Engineer', 'Aarav@1234'),
    ('Priya',    'Verma',    'priya.verma@example.com',     '9123456780', 'Female', 'Student',           'Priya@5678'),
    ('Rahul',    'Mehta',    'rahul.mehta@example.com',     '9988776655', 'Male',   'Data Analyst',      'Rahul@9012'),
    ('Sneha',    'Kapoor',   'sneha.kapoor@example.com',    '9876501234', 'Female', 'Teacher',           'Sneha@3456'),
    ('Vikram',   'Singh',    'vikram.singh@example.com',    '9812345678', 'Male',   'Student',           'Vikram@7890'),
    ('Ananya',   'Iyer',     'ananya.iyer@example.com',     '9845612379', 'Female', 'Doctor',            'Ananya@2468'),
    ('Rohan',    'Patel',    'rohan.patel@example.com',     '9700112233', 'Male',   'Student',           'Rohan@1357'),
    ('Kavya',    'Nair',     'kavya.nair@example.com',      '9622334455', 'Female', 'Designer',          'Kavya@8642'),
    ('Arjun',    'Reddy',    'arjun.reddy@example.com',     '9494949494', 'Male',   'Business Analyst',  'Arjun@4321'),
    ('Meera',    'Joshi',    'meera.joshi@example.com',     '9833445566', 'Other',  'Student',           'Meera@6543');

SELECT * FROM RegistrationData;

