--1. List the following details of each employee: employee number, last name, first name, gender, and salary.
select e.emp_no as "Employee Number", e.last_name as "Last Name", e.first_name as "First Name", e.gender as "Gender", s.salary as "salaries"
from employees as e
full join salaries as s on e.emp_no = s.emp_no
order by e.emp_no asc 

--2. List employees who were hired in 1986.
select first_name as "First Name", last_name as "Last Name", hire_date as "Hire Date" 
from employees where extract(year from hire_date) = 1986
order by hire_date asc;

--3. List the manager of each department with the following information: department number, department name, 
--the manager's employee number, last name, first name, and start and end employment dates.
select d.dept_no as "Department Number", d.dept_name as "Department Name", e.emp_no as "Employee Number", 
e.last_name as "Last Name", e.first_name as "First Name", dm.from_date as "Start Date", dm.to_date as "End Date"
from departments as d
left join dept_manager as dm on d.dept_no = dm.dept_no
left join employees as e on dm.emp_no = e.emp_no
order by d.dept_no asc

--4. List the department of each employee with the following information: employee number, last name, first name, 
--and department name.
select e.emp_no as "Employee Number", e.last_name as "Last Name", e.first_name as "First Name", d.dept_name as "Department Name"
from employees as e
left join dept_emp as de on e.emp_no = de.emp_no
left join departments as d on de.dept_no = d.dept_no
order by e.emp_no asc

--5. List all employees whose first name is "Hercules" and last names begin with "B."
select first_name as "First Name", last_name as "Last Name" from employees where first_name = 'Hercules' 
and last_name LIKE 'B%'

--6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
--select * from departments --> sales = d007
--select * from dept_emp
select e.emp_no as "Employee Number", e.last_name as "Last Name", e.first_name as "First Name", d.dept_name as "Department Name"
from employees as e
left join dept_emp as de on e.emp_no = de.emp_no
left join departments as d on de.dept_no = d.dept_no
where de.dept_no = 'd007'
order by e.emp_no asc

--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
select e.emp_no as "Employee Number", e.last_name as "Last Name", e.first_name as "First Name", d.dept_name as "Department Name"
from employees as e
left join dept_emp as de on e.emp_no = de.emp_no
left join departments as d on de.dept_no = d.dept_no
where de.dept_no = 'd007' or de.dept_no = 'd005'
order by e.emp_no asc

--8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select last_name as "Last Name", COUNT(last_name) as "Total" 
from employees
group by last_name
order by Count(last_name) desc