CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    salary NUMERIC(10,2) NOT NULL,
    city VARCHAR(100) NOT NULL
);

TRUNCATE TABLE employees RESTART IDENTITY;

INSERT INTO employees (name, department, salary, city) VALUES
('Ravi',   'Engineering', 90000,  'Hyderabad'),
('Priya',  'Engineering', 110000, 'Bangalore'),
('Arun',   'HR',          70000,  'Chennai'),
('Meena',  'Finance',     95000,  'Hyderabad'),
('Kiran',  'Engineering', 120000, 'Pune'),
('Anjali', 'Finance',     105000, 'Bangalore'),
('Rahul',  'HR',          75000,  'Hyderabad'),
('Sneha',  'Engineering', 115000, 'Chennai'),
('Vikram', 'Sales',       85000,  'Bangalore'),
('Divya',  'Sales',       92000,  'Hyderabad');
