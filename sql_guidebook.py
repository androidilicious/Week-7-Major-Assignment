"""
SQL Guidebook - Comprehensive SQL Query Examples
Week 7 Major Assignment - IDS 706
Author: Diwas Puri
Date: October 2025

"""

import sqlite3
import pandas as pd
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect('company_database.db')
cursor = conn.cursor()

# Enforce foreign key constraints in SQLite
cursor.execute("PRAGMA foreign_keys = ON")

print("=" * 80)
print("SQL GUIDEBOOK - COMPREHENSIVE QUERY EXAMPLES")
print("=" * 80)
print(f"SQLite version: {sqlite3.sqlite_version}")
print(f"pandas version: {pd.__version__}")

# ============================================================================
# SECTION 1: TABLE CREATION & DATA SETUP
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 1: TABLE CREATION & POPULATION")
print("=" * 80)

# Drop existing tables if they exist
cursor.execute("DROP TABLE IF EXISTS salary_history")
cursor.execute("DROP TABLE IF EXISTS project_assignments")
cursor.execute("DROP TABLE IF EXISTS projects")
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS departments")

# Query 1: CREATE TABLE - Departments
print("\n--- Query 1: CREATE TABLE - Departments ---")
query1 = """
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    budget DECIMAL(12, 2),
    established_date DATE
)
"""
cursor.execute(query1)
print("✓ Departments table created")
print("Purpose: Store department information with budget tracking")

# Query 2: CREATE TABLE - Employees
print("\n--- Query 2: CREATE TABLE - Employees ---")
query2 = """
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    hire_date DATE NOT NULL,
    dept_id INTEGER,
    job_title VARCHAR(100),
    manager_id INTEGER,
    status VARCHAR(20) DEFAULT 'Active',
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
)
"""
cursor.execute(query2)
print("✓ Employees table created")
print("Purpose: Store employee information with department and manager relationships")

# Query 3: CREATE TABLE - Projects
print("\n--- Query 3: CREATE TABLE - Projects ---")
query3 = """
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    dept_id INTEGER,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12, 2),
    status VARCHAR(20),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
)
"""
cursor.execute(query3)
print("✓ Projects table created")
print("Purpose: Track projects by department with budget and timeline")

# Query 4: CREATE TABLE - Project Assignments
print("\n--- Query 4: CREATE TABLE - Project Assignments ---")
query4 = """
CREATE TABLE project_assignments (
    assignment_id INTEGER PRIMARY KEY,
    emp_id INTEGER,
    project_id INTEGER,
    role VARCHAR(50),
    hours_allocated DECIMAL(5, 2),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
)
"""
cursor.execute(query4)
print("✓ Project Assignments table created")
print("Purpose: Many-to-many relationship between employees and projects")

# Query 5: CREATE TABLE - Salary History
print("\n--- Query 5: CREATE TABLE - Salary History ---")
query5 = """
CREATE TABLE salary_history (
    salary_id INTEGER PRIMARY KEY,
    emp_id INTEGER,
    salary DECIMAL(10, 2),
    effective_date DATE,
    end_date DATE,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
)
"""
cursor.execute(query5)
print("✓ Salary History table created")
print("Purpose: Track salary changes over time for each employee")

conn.commit()

# INSERT data
print("\n--- Query 6: INSERT - Populate Departments ---")
departments_data = [
    (1, 'Engineering', 'San Francisco', 2500000.00, '2015-01-15'),
    (2, 'Marketing', 'New York', 1200000.00, '2015-03-20'),
    (3, 'Sales', 'Chicago', 1800000.00, '2015-02-10'),
    (4, 'Human Resources', 'San Francisco', 800000.00, '2015-01-15'),
    (5, 'Finance', 'New York', 1500000.00, '2015-04-01')
]

cursor.executemany("""
    INSERT INTO departments (dept_id, dept_name, location, budget, established_date)
    VALUES (?, ?, ?, ?, ?)
""", departments_data)
print(f"✓ Inserted {len(departments_data)} departments")

print("\n--- Query 7: INSERT - Populate Employees ---")
employees_data = [
    (1, 'John', 'Smith', 'john.smith@company.com', '2015-03-15', 1, 'Senior Engineer', None, 'Active'),
    (2, 'Sarah', 'Johnson', 'sarah.j@company.com', '2016-07-22', 1, 'Engineering Manager', 1, 'Active'),
    (3, 'Michael', 'Brown', 'michael.b@company.com', '2017-01-10', 2, 'Marketing Director', None, 'Active'),
    (4, 'Emily', 'Davis', 'emily.d@company.com', '2017-05-18', 2, 'Marketing Specialist', 3, 'Active'),
    (5, 'David', 'Wilson', 'david.w@company.com', '2018-02-14', 3, 'Sales Manager', None, 'Active'),
    (6, 'Jessica', 'Martinez', 'jessica.m@company.com', '2018-09-30', 3, 'Sales Representative', 5, 'Active'),
    (7, 'James', 'Taylor', 'james.t@company.com', '2019-03-12', 1, 'Junior Engineer', 2, 'Active'),
    (8, 'Lisa', 'Anderson', 'lisa.a@company.com', '2019-08-20', 4, 'HR Manager', None, 'Active'),
    (9, 'Robert', 'Thomas', 'robert.t@company.com', '2020-01-05', 5, 'Financial Analyst', None, 'Active'),
    (10, 'Jennifer', 'Lee', 'jennifer.l@company.com', '2020-06-15', 1, 'Senior Engineer', 2, 'Active'),
    (11, 'William', 'White', 'william.w@company.com', '2021-02-28', 3, 'Sales Representative', 5, 'Inactive'),
    (12, 'Amanda', 'Harris', 'amanda.h@company.com', '2021-09-10', 2, 'Marketing Coordinator', 3, 'Active')
]

cursor.executemany("""
    INSERT INTO employees (emp_id, first_name, last_name, email, hire_date, dept_id, job_title, manager_id, status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", employees_data)
print(f"✓ Inserted {len(employees_data)} employees")

print("\n--- Query 8: INSERT - Populate Projects ---")
projects_data = [
    (1, 'Cloud Migration', 1, '2023-01-01', '2024-06-30', 500000.00, 'In Progress'),
    (2, 'Brand Refresh', 2, '2023-03-15', '2023-12-31', 300000.00, 'Completed'),
    (3, 'Sales CRM Implementation', 3, '2023-06-01', '2024-03-31', 400000.00, 'In Progress'),
    (4, 'Employee Wellness Program', 4, '2023-02-01', '2023-11-30', 150000.00, 'Completed'),
    (5, 'Financial Reporting System', 5, '2023-09-01', '2024-08-31', 600000.00, 'In Progress'),
    (6, 'Mobile App Development', 1, '2024-01-15', '2024-12-31', 800000.00, 'In Progress')
]

cursor.executemany("""
    INSERT INTO projects (project_id, project_name, dept_id, start_date, end_date, budget, status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", projects_data)
print(f"✓ Inserted {len(projects_data)} projects")

print("\n--- Query 9: INSERT - Populate Project Assignments ---")
assignments_data = [
    (1, 1, 1, 'Lead Developer', 40.0),
    (2, 2, 1, 'Project Manager', 20.0),
    (3, 7, 1, 'Developer', 40.0),
    (4, 10, 1, 'Senior Developer', 40.0),
    (5, 3, 2, 'Project Lead', 30.0),
    (6, 4, 2, 'Marketing Specialist', 40.0),
    (7, 12, 2, 'Coordinator', 35.0),
    (8, 5, 3, 'Project Manager', 25.0),
    (9, 6, 3, 'Sales Analyst', 40.0),
    (10, 8, 4, 'HR Lead', 30.0),
    (11, 9, 5, 'Lead Analyst', 40.0),
    (12, 2, 6, 'Technical Advisor', 15.0),
    (13, 10, 6, 'Lead Developer', 40.0)
]

cursor.executemany("""
    INSERT INTO project_assignments (assignment_id, emp_id, project_id, role, hours_allocated)
    VALUES (?, ?, ?, ?, ?)
""", assignments_data)
print(f"✓ Inserted {len(assignments_data)} project assignments")

print("\n--- Query 10: INSERT - Populate Salary History ---")
salary_data = [
    (1, 1, 95000.00, '2015-03-15', '2017-03-14'),
    (2, 1, 110000.00, '2017-03-15', '2020-03-14'),
    (3, 1, 130000.00, '2020-03-15', None),
    (4, 2, 120000.00, '2016-07-22', '2019-07-21'),
    (5, 2, 145000.00, '2019-07-22', None),
    (6, 3, 130000.00, '2017-01-10', '2021-01-09'),
    (7, 3, 155000.00, '2021-01-10', None),
    (8, 4, 65000.00, '2017-05-18', '2020-05-17'),
    (9, 4, 75000.00, '2020-05-18', None),
    (10, 5, 110000.00, '2018-02-14', '2021-02-13'),
    (11, 5, 130000.00, '2021-02-14', None),
    (12, 6, 60000.00, '2018-09-30', '2021-09-29'),
    (13, 6, 70000.00, '2021-09-30', None),
    (14, 7, 75000.00, '2019-03-12', '2022-03-11'),
    (15, 7, 85000.00, '2022-03-12', None),
    (16, 8, 95000.00, '2019-08-20', '2022-08-19'),
    (17, 8, 110000.00, '2022-08-20', None),
    (18, 9, 80000.00, '2020-01-05', '2023-01-04'),
    (19, 9, 92000.00, '2023-01-05', None),
    (20, 10, 115000.00, '2020-06-15', '2023-06-14'),
    (21, 10, 135000.00, '2023-06-15', None),
    (22, 11, 58000.00, '2021-02-28', None),
    (23, 12, 55000.00, '2021-09-10', None)
]

cursor.executemany("""
    INSERT INTO salary_history (salary_id, emp_id, salary, effective_date, end_date)
    VALUES (?, ?, ?, ?, ?)
""", salary_data)
print(f"✓ Inserted {len(salary_data)} salary records")

conn.commit()

# ============================================================================
# SECTION 2: BASIC SQL QUERIES
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 2: BASIC SQL OPERATIONS")
print("=" * 80)

# Query 11: UPDATE - Modify existing records
print("\n--- Query 11: UPDATE - Give raises to Senior Engineers ---")
query11 = """
UPDATE salary_history
SET salary = salary * 1.10
WHERE emp_id IN (
    SELECT emp_id 
    FROM employees 
    WHERE job_title = 'Senior Engineer'
) AND end_date IS NULL
"""
cursor.execute(query11)
conn.commit()
print(f"✓ Updated {cursor.rowcount} salary records")
print("Purpose: Demonstrate UPDATE with subquery - Give 10% raise to all Senior Engineers")

# Query 12: SELECT with WHERE, ORDER BY, LIMIT
print("\n--- Query 12: SELECT - Top 5 Highest Paid Employees ---")
query12 = """
SELECT 
    e.emp_id,
    e.first_name || ' ' || e.last_name AS full_name,
    e.job_title,
    d.dept_name,
    s.salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
JOIN salary_history s ON e.emp_id = s.emp_id
WHERE s.end_date IS NULL
ORDER BY s.salary DESC
LIMIT 5
"""
df = pd.read_sql_query(query12, conn)
print(df.to_string(index=False))
print("\nPurpose: Find top 5 highest paid employees using SELECT, JOIN, WHERE, ORDER BY, LIMIT")

# ============================================================================
# SECTION 3: AGGREGATE FUNCTIONS & GROUP BY
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 3: AGGREGATE FUNCTIONS")
print("=" * 80)

# Query 13: GROUP BY with HAVING
print("\n--- Query 13: GROUP BY & HAVING - Department Statistics ---")
query13 = """
SELECT 
    d.dept_name,
    COUNT(e.emp_id) AS employee_count,
    ROUND(AVG(s.salary), 2) AS avg_salary,
    MAX(s.salary) AS max_salary,
    MIN(s.salary) AS min_salary,
    SUM(s.salary) AS total_payroll
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id AND e.status = 'Active'
LEFT JOIN salary_history s ON e.emp_id = s.emp_id AND s.end_date IS NULL
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 0
ORDER BY avg_salary DESC
"""
df = pd.read_sql_query(query13, conn)
print(df.to_string(index=False))
print("\nPurpose: Demonstrate GROUP BY, HAVING, and aggregate functions (COUNT, AVG, MAX, MIN, SUM)")

# ============================================================================
# SECTION 4: ADVANCED JOINS
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 4: ADVANCED JOIN OPERATIONS")
print("=" * 80)

# Query 14: Complex JOIN with multiple tables
print("\n--- Query 14: INNER JOIN - Employee Project Details ---")
query14 = """
SELECT 
    e.first_name || ' ' || e.last_name AS employee_name,
    e.job_title,
    d.dept_name,
    p.project_name,
    pa.role AS project_role,
    pa.hours_allocated,
    p.status AS project_status
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
INNER JOIN project_assignments pa ON e.emp_id = pa.emp_id
INNER JOIN projects p ON pa.project_id = p.project_id
WHERE e.status = 'Active'
ORDER BY e.last_name, p.project_name
"""
df = pd.read_sql_query(query14, conn)
print(df.to_string(index=False))
print("\nPurpose: Demonstrate INNER JOIN across 4 tables to show employee project assignments")

# Query 15: LEFT JOIN to find employees without projects
print("\n--- Query 15: LEFT JOIN - Employees Without Projects ---")
query15 = """
SELECT 
    e.emp_id,
    e.first_name || ' ' || e.last_name AS employee_name,
    e.job_title,
    d.dept_name,
    CASE 
        WHEN pa.assignment_id IS NULL THEN 'No Project'
        ELSE 'Assigned'
    END AS assignment_status
FROM employees e
LEFT JOIN project_assignments pa ON e.emp_id = pa.emp_id
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE e.status = 'Active' AND pa.assignment_id IS NULL
"""
df = pd.read_sql_query(query15, conn)
print(df.to_string(index=False))
print("\nPurpose: Use LEFT JOIN to identify employees not assigned to any project")

# ============================================================================
# SECTION 5: WINDOW FUNCTIONS
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 5: WINDOW FUNCTIONS")
print("=" * 80)

# Query 16: ROW_NUMBER and RANK
print("\n--- Query 16: Window Functions - Salary Ranking by Department ---")
query16 = """
SELECT 
    e.first_name || ' ' || e.last_name AS employee_name,
    d.dept_name,
    s.salary,
    ROW_NUMBER() OVER (PARTITION BY d.dept_id ORDER BY s.salary DESC) AS row_num,
    RANK() OVER (PARTITION BY d.dept_id ORDER BY s.salary DESC) AS salary_rank,
    ROUND(AVG(s.salary) OVER (PARTITION BY d.dept_id), 2) AS dept_avg_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
JOIN salary_history s ON e.emp_id = s.emp_id
WHERE s.end_date IS NULL AND e.status = 'Active'
ORDER BY d.dept_name, s.salary DESC
"""
df = pd.read_sql_query(query16, conn)
print(df.to_string(index=False))
print("\nPurpose: Use PARTITION BY, ROW_NUMBER, RANK, and window aggregate to analyze salaries")

# ============================================================================
# SECTION 6: COMMON TABLE EXPRESSIONS (CTEs)
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 6: COMMON TABLE EXPRESSIONS (CTEs)")
print("=" * 80)

# Query 17: CTE with WITH clause
print("\n--- Query 17: CTE - Project Budget Analysis ---")
query17 = """
WITH project_costs AS (
    SELECT 
        p.project_id,
        p.project_name,
        p.budget,
        p.status,
        d.dept_name,
        COUNT(pa.emp_id) AS team_size,
        SUM(pa.hours_allocated) AS total_hours
    FROM projects p
    JOIN departments d ON p.dept_id = d.dept_id
    LEFT JOIN project_assignments pa ON p.project_id = pa.project_id
    GROUP BY p.project_id, p.project_name, p.budget, p.status, d.dept_name
),
dept_totals AS (
    SELECT 
        dept_name,
        SUM(budget) AS total_dept_budget,
        AVG(budget) AS avg_project_budget
    FROM project_costs
    GROUP BY dept_name
)
SELECT 
    pc.project_name,
    pc.dept_name,
    pc.budget,
    pc.team_size,
    pc.total_hours,
    pc.status,
    dt.total_dept_budget,
    ROUND((pc.budget * 100.0 / dt.total_dept_budget), 2) AS pct_of_dept_budget
FROM project_costs pc
JOIN dept_totals dt ON pc.dept_name = dt.dept_name
ORDER BY pc.dept_name, pc.budget DESC
"""
df = pd.read_sql_query(query17, conn)
print(df.to_string(index=False))
print("\nPurpose: Use multiple CTEs with WITH clause for complex budget analysis")

# ============================================================================
# SECTION 7: ADVANCED FEATURES (Self-explored)
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 7: ADVANCED SQL FEATURES (Self-Explored)")
print("=" * 80)

# Query 18: String Functions - SUBSTR, LENGTH, UPPER, LOWER, ||
print("\n--- Query 18: String Functions - Email Domain Analysis ---")
query18 = """
SELECT 
    e.first_name || ' ' || e.last_name AS employee_name,
    e.email,
    SUBSTR(e.email, INSTR(e.email, '@') + 1) AS email_domain,
    LENGTH(e.email) AS email_length,
    UPPER(e.first_name) AS first_name_upper,
    LOWER(e.last_name) AS last_name_lower,
    SUBSTR(e.first_name, 1, 1) || '. ' || e.last_name AS abbreviated_name
FROM employees e
WHERE e.status = 'Active'
ORDER BY email_domain, e.last_name
"""
df = pd.read_sql_query(query18, conn)
print(df.to_string(index=False))
print("\nPurpose: Demonstrate string functions: SUBSTR, INSTR, LENGTH, UPPER, LOWER, ||")

# Query 19: Date Functions and JULIANDAY
print("\n--- Query 19: Date Functions - Employee Tenure Analysis ---")
query19 = """
SELECT 
    e.first_name || ' ' || e.last_name AS employee_name,
    e.hire_date,
    DATE('now') AS current_date,
    CAST((JULIANDAY('now') - JULIANDAY(e.hire_date)) / 365.25 AS INTEGER) AS years_employed,
    ROUND((JULIANDAY('now') - JULIANDAY(e.hire_date)) / 30.44, 1) AS months_employed,
    CAST(JULIANDAY('now') - JULIANDAY(e.hire_date) AS INTEGER) AS days_employed,
    CASE 
        WHEN JULIANDAY('now') - JULIANDAY(e.hire_date) < 365 THEN 'New Employee'
        WHEN JULIANDAY('now') - JULIANDAY(e.hire_date) < 1825 THEN 'Mid-level'
        ELSE 'Senior'
    END AS tenure_category
FROM employees e
WHERE e.status = 'Active'
ORDER BY years_employed DESC
"""
df = pd.read_sql_query(query19, conn)
print(df.to_string(index=False))
print("\nPurpose: Use DATE, JULIANDAY, and date arithmetic to calculate employee tenure")

# Query 20: COALESCE and CASE WHEN for data cleaning
print("\n--- Query 20: COALESCE & CASE - Manager Hierarchy ---")
query20 = """
SELECT 
    e.emp_id,
    e.first_name || ' ' || e.last_name AS employee_name,
    e.job_title,
    COALESCE(m.first_name || ' ' || m.last_name, 'No Manager') AS manager_name,
    CASE 
        WHEN e.manager_id IS NULL THEN 'Executive'
        WHEN e.job_title LIKE '%Manager%' OR e.job_title LIKE '%Director%' THEN 'Management'
        WHEN e.job_title LIKE '%Senior%' THEN 'Senior Level'
        WHEN e.job_title LIKE '%Junior%' THEN 'Junior Level'
        ELSE 'Mid Level'
    END AS employee_level,
    CASE 
        WHEN s.salary >= 130000 THEN 'High'
        WHEN s.salary >= 90000 THEN 'Medium'
        ELSE 'Entry'
    END AS salary_band
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id
LEFT JOIN salary_history s ON e.emp_id = s.emp_id AND s.end_date IS NULL
WHERE e.status = 'Active'
ORDER BY employee_level, e.last_name
"""
df = pd.read_sql_query(query20, conn)
print(df.to_string(index=False))
print("\nPurpose: Use COALESCE for NULL handling and nested CASE WHEN for categorization")

# Query 21: UNION to combine results from different queries
print("\n--- Query 21: UNION - Combined Active and Inactive Employees Summary ---")
query21 = """
SELECT 
    'Active' AS employee_status,
    COUNT(*) AS employee_count,
    ROUND(AVG(s.salary), 2) AS avg_salary,
    MAX(s.salary) AS max_salary
FROM employees e
JOIN salary_history s ON e.emp_id = s.emp_id AND s.end_date IS NULL
WHERE e.status = 'Active'

UNION ALL

SELECT 
    'Inactive' AS employee_status,
    COUNT(*) AS employee_count,
    ROUND(AVG(s.salary), 2) AS avg_salary,
    MAX(s.salary) AS max_salary
FROM employees e
JOIN salary_history s ON e.emp_id = s.emp_id AND s.end_date IS NULL
WHERE e.status = 'Inactive'

UNION ALL

SELECT 
    'Total' AS employee_status,
    COUNT(*) AS employee_count,
    ROUND(AVG(s.salary), 2) AS avg_salary,
    MAX(s.salary) AS max_salary
FROM employees e
JOIN salary_history s ON e.emp_id = s.emp_id AND s.end_date IS NULL
"""
df = pd.read_sql_query(query21, conn)
print(df.to_string(index=False))
print("\nPurpose: Use UNION ALL to combine multiple result sets for comparison")

# ============================================================================
# FINAL SUMMARY
# ============================================================================

print("\n" + "=" * 80)
print("SQL GUIDEBOOK COMPLETE!")
print("=" * 80)
print("\nSQL Features Demonstrated:")
print("✓ CREATE TABLE with constraints and foreign keys")
print("✓ INSERT data into multiple related tables")
print("✓ UPDATE with subqueries")
print("✓ SELECT with WHERE, ORDER BY, LIMIT")
print("✓ GROUP BY with HAVING clause")
print("✓ Aggregate functions: COUNT, AVG, MAX, MIN, SUM")
print("✓ INNER JOIN, LEFT JOIN across multiple tables")
print("✓ Window functions: ROW_NUMBER, RANK, PARTITION BY")
print("✓ Common Table Expressions (CTEs) with WITH")
print("✓ String functions: SUBSTR, INSTR, LENGTH, UPPER, LOWER")
print("✓ Date functions: DATE, JULIANDAY, date arithmetic")
print("✓ COALESCE for NULL handling")
print("✓ Complex CASE WHEN statements")
print("✓ UNION ALL for combining results")
print("\n" + "=" * 80)

# Close connection
conn.close()
print("\n✓ Database connection closed successfully")
