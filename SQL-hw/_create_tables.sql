CREATE TABLE departments (
    dept_no varchar(200) NOT NULL primary key,
    dept_name varchar(200) NOT NULL
);

CREATE TABLE employees (
    emp_no int NOT NULL primary key,
    birth_date date NOT NULL,
    first_name varchar(200) NOT NULL,
    last_name varchar(200) NOT NULL,
    gender varchar(1) NOT NULL,
    hire_date date NOT NULL
);

CREATE TABLE dept_emp (
    emp_no int NOT NULL, foreign key (emp_no) references employees(emp_no),
    dept_no varchar(200) NOT NULL, foreign key (dept_no) references departments(dept_no),
    from_date date   NOT NULL,
    to_date date   NOT NULL
);

CREATE TABLE dept_manager (
    dept_no varchar(200) NOT NULL, foreign key (dept_no) references departments(dept_no),
    emp_no int not null, foreign key (emp_no) references employees(emp_no),
    from_date date   NOT NULL,
    to_date date   NOT NULL
);

CREATE TABLE salaries (
    emp_no int not null, foreign key (emp_no) references employees(emp_no),
    salary money NOT NULL,
    from_date date NOT NULL,
    to_date date NOT NULL
);

CREATE TABLE titles (
    emp_no int not null, foreign key (emp_no) references employees(emp_no),
    title varchar(200) NOT NULL,
    from_date date NOT NULL,
    to_date date NOT NULL
);

