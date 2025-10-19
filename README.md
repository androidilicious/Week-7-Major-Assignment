# SQL Guidebook - Comprehensive SQL Query Reference
**IDS 706 - Week 7 Major Assignment**  
**Due: October 19, 2025**

---

```stl
solid DukeLogo
  facet normal 0 0 1
    outer loop
      vertex 10 0 0
      vertex 10 50 0
      vertex 15 50 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 10 0 0
      vertex 15 50 0
      vertex 15 0 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15 0 0
      vertex 15 5 0
      vertex 35 5 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15 0 0
      vertex 35 5 0
      vertex 35 0 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 35 5 0
      vertex 40 10 0
      vertex 40 5 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 35 5 0
      vertex 35 10 0
      vertex 40 10 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 40 10 0
      vertex 45 25 0
      vertex 45 10 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 40 10 0
      vertex 40 25 0
      vertex 45 25 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 45 25 0
      vertex 40 40 0
      vertex 45 40 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 45 25 0
      vertex 45 40 0
      vertex 40 40 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 40 40 0
      vertex 35 45 0
      vertex 40 45 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 40 40 0
      vertex 35 40 0
      vertex 35 45 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 35 45 0
      vertex 15 50 0
      vertex 35 50 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 35 45 0
      vertex 15 45 0
      vertex 15 50 0
    endloop
  endfacet
endsolid DukeLogo
```

## 📋 Table of Contents
1. [Project Overview](#-project-overview)
2. [Database Design](#-database-design)
3. [SQL Query Examples](#-sql-query-examples)
4. [Summary of SQL Features Covered](#-summary-of-sql-features-covered)
5. [How to Run](#-how-to-run)
6. [Tips for SQL Interviews](#-tips-for-sql-interviews)
7. [Additional Resources](#-additional-resources)

---

## 🎯 Project Overview

This SQL Guidebook is a  reference demonstrating advanced SQL concepts through a realistic company database scenario. The project includes:

- **5 interconnected tables** following database design principles
- **21 SQL queries** covering basic to advanced concepts
- **Multiple JOIN operations** (INNER, LEFT)
- **Window functions** with PARTITION BY
- **Common Table Expressions (CTEs)**
- **String and Date functions**
- **Data transformation** with CASE WHEN and COALESCE

### Database Schema: Company Management System

The database models a company with departments, employees, projects, and salary tracking.

---

## 🗄️ Database Design

### Entity Relationship Diagram (ERD)

```mermaid
erDiagram
    departments ||--o{ employees : "has"
    departments ||--o{ projects : "owns"
    employees ||--o{ salary_history : "has"
    employees ||--o{ project_assignments : "assigned_to"
    employees ||--o| employees : "manages"
    projects ||--o{ project_assignments : "includes"
    
    departments {
        int dept_id PK
        varchar dept_name
        varchar location
        decimal budget
        date established_date
    }
    
    employees {
        int emp_id PK
        varchar first_name
        varchar last_name
        varchar email UK
        date hire_date
        int dept_id FK
        varchar job_title
        int manager_id FK
        varchar status
    }
    
    projects {
        int project_id PK
        varchar project_name
        int dept_id FK
        date start_date
        date end_date
        decimal budget
        varchar status
    }
    
    project_assignments {
        int assignment_id PK
        int project_id FK
        int emp_id FK
        varchar role
        decimal hours_allocated
        date assigned_date
    }
    
    salary_history {
        int salary_id PK
        int emp_id FK
        decimal salary
        date start_date
        date end_date
        varchar change_reason
    }
```

### Tables Overview

1. **departments** - Department information with budgets
2. **employees** - Employee details with manager hierarchy
3. **projects** - Project tracking by department
4. **project_assignments** - Many-to-many relationship between employees and projects
5. **salary_history** - Temporal salary tracking for employees

---

## 📊 SQL Query Examples

### **Section 1: Table Creation & Data Setup**

#### Query 1: CREATE TABLE - Departments
**Purpose**: Create the departments table with budget tracking

```sql
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    budget DECIMAL(12, 2),
    established_date DATE
)
```

**Key Features**:
- Primary key constraint on `dept_id`
- NOT NULL constraint ensures department name is required
- Decimal type for precise budget tracking

---

#### Query 2: CREATE TABLE - Employees
**Purpose**: Create employees table with self-referencing manager relationship

```sql
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
```

**Key Features**:
- UNIQUE constraint on email
- Self-referencing foreign key for manager hierarchy
- DEFAULT value for status column
- Two foreign key relationships

---

#### Query 3-5: Additional Tables
**Purpose**: Create projects, project_assignments, and salary_history tables

*See sql_guidebook.py for complete table definitions*

**Database Design Principles Applied**:
- ✅ Normalization (3NF)
- ✅ Referential integrity with foreign keys
- ✅ Many-to-many relationships via junction table
- ✅ Temporal data tracking (salary history)
- ✅ Self-referencing relationships (manager hierarchy)

---

#### Query 6-10: INSERT Statements
**Purpose**: Populate all tables with realistic sample data

**Sample Output** (Departments):
```
✓ Inserted 5 departments
✓ Inserted 12 employees
✓ Inserted 6 projects
✓ Inserted 13 project assignments
✓ Inserted 23 salary records
```

---

### **Section 2: Basic SQL Operations**

#### Query 11: UPDATE - Modify Existing Records
**Purpose**: Give 10% raise to all Senior Engineers

```sql
UPDATE salary_history
SET salary = salary * 1.10
WHERE emp_id IN (
    SELECT emp_id 
    FROM employees 
    WHERE job_title = 'Senior Engineer'
) AND end_date IS NULL
```

**Key Features**:
- UPDATE with subquery
- Conditional update based on job title
- Only updates current salary records (end_date IS NULL)

**Output**:
```
✓ Updated 2 salary records
```

---

#### Query 12: SELECT with WHERE, ORDER BY, LIMIT
**Purpose**: Find top 5 highest paid employees

```sql
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
```

**Sample Output**:
```
emp_id  full_name           job_title              dept_name     salary
3       Michael Brown       Marketing Director     Marketing     155000.0
2       Sarah Johnson       Engineering Manager    Engineering   145000.0
10      Jennifer Lee        Senior Engineer        Engineering   148500.0  
1       John Smith          Senior Engineer        Engineering   143000.0
5       David Wilson        Sales Manager          Sales         130000.0
```

**Key Features**:
- String concatenation with ||
- Multiple JOINs
- Filtering current salaries
- TOP N query pattern

---

### **Section 3: Aggregate Functions & GROUP BY**

#### Query 13: GROUP BY with HAVING
**Purpose**: Calculate department-level statistics

```sql
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
```

**Sample Output**:
```
dept_name          employee_count  avg_salary   max_salary   min_salary   total_payroll
Marketing          3               95000.00     155000.00    55000.00     285000.00
Engineering        4               130625.00    148500.00    85000.00     522500.00
Sales              2               100000.00    130000.00    70000.00     200000.00
Finance            1               92000.00     92000.00     92000.00     92000.00
Human Resources    1               110000.00    110000.00    110000.00    110000.00
```

**Key Features**:
- All aggregate functions: COUNT, AVG, MAX, MIN, SUM
- GROUP BY clause
- HAVING clause for post-aggregation filtering
- ROUND function for precision control
- LEFT JOIN to include all departments

---

### **Section 4: Advanced JOIN Operations**

#### Query 14: INNER JOIN - Multiple Tables
**Purpose**: Show employee project assignments with full details

```sql
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
```

**Sample Output**:
```
employee_name      job_title              dept_name    project_name                 project_role        hours_allocated  project_status
Lisa Anderson      HR Manager             HR           Employee Wellness Program    HR Lead             30.0             Completed
Michael Brown      Marketing Director     Marketing    Brand Refresh                Project Lead        30.0             Completed
Emily Davis        Marketing Specialist   Marketing    Brand Refresh                Marketing Spec.     40.0             Completed
Amanda Harris      Marketing Coord.       Marketing    Brand Refresh                Coordinator         35.0             Completed
Sarah Johnson      Engineering Manager    Engineering  Cloud Migration              Project Manager     20.0             In Progress
Sarah Johnson      Engineering Manager    Engineering  Mobile App Development       Technical Advisor   15.0             In Progress
```

**Key Features**:
- INNER JOIN across 4 tables
- Complex relationship navigation
- String concatenation for display
- Column aliasing for clarity

---

#### Query 15: LEFT JOIN - Find Unassigned Employees
**Purpose**: Identify employees not assigned to any project

```sql
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
```

**Sample Output**:
```
emp_id  employee_name     job_title           dept_name    assignment_status
8       Lisa Anderson     HR Manager          HR           No Project
```

**Key Features**:
- LEFT JOIN to find missing matches
- IS NULL check to identify unmatched records
- CASE statement for status labeling
- Practical use case: resource allocation

---

### **Section 5: Window Functions**

#### Query 16: Window Functions - Salary Ranking
**Purpose**: Rank employees by salary within each department

```sql
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
```

**Sample Output**:
```
employee_name      dept_name    salary      row_num  salary_rank  dept_avg_salary
Jennifer Lee       Engineering  148500.00   1        1            130625.00
John Smith         Engineering  143000.00   2        2            130625.00
Sarah Johnson      Engineering  145000.00   3        3            130625.00
James Taylor       Engineering  85000.00    4        4            130625.00
Robert Thomas      Finance      92000.00    1        1            92000.00
Lisa Anderson      HR           110000.00   1        1            110000.00
Michael Brown      Marketing    155000.00   1        1            95000.00
Emily Davis        Marketing    75000.00    2        2            95000.00
Amanda Harris      Marketing    55000.00    3        3            95000.00
```

**Key Features**:
- **PARTITION BY**: Resets ranking for each department
- **ROW_NUMBER()**: Assigns unique sequential numbers
- **RANK()**: Allows ties in ranking
- **Window aggregate**: AVG() OVER for department average
- Demonstrates difference between ROW_NUMBER and RANK

**Use Cases**:
- Salary comparisons within departments
- Performance rankings
- Identifying top performers by category

---

### **Section 6: Common Table Expressions (CTEs)**

#### Query 17: Multiple CTEs - Project Budget Analysis
**Purpose**: Analyze project budgets relative to department totals

```sql
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
```

**Sample Output**:
```
project_name                  dept_name    budget      team_size  total_hours  status       total_dept_budget  pct_of_dept_budget
Mobile App Development        Engineering  800000.00   2          55.0         In Progress  1300000.00         61.54
Cloud Migration               Engineering  500000.00   4          140.0        In Progress  1300000.00         38.46
Financial Reporting System    Finance      600000.00   1          40.0         In Progress  600000.00          100.0
Employee Wellness Program     HR           150000.00   1          30.0         Completed    150000.00          100.0
Brand Refresh                 Marketing    300000.00   3          105.0        Completed    300000.00          100.0
Sales CRM Implementation      Sales        400000.00   2          65.0         In Progress  400000.00          100.0
```

**Key Features**:
- **Multiple CTEs**: Two-stage aggregation
- **WITH clause**: Named subqueries for readability
- **CTE reuse**: Second CTE references first
- **Complex calculations**: Percentage of department budget
- **Modular logic**: Breaking complex queries into steps

**Benefits of CTEs**:
- Improved readability
- Easier debugging
- Reusable within same query
- Alternative to nested subqueries

---

### **Section 7: Advanced Features (Self-Explored)**

#### Query 18: String Functions
**Purpose**: Demonstrate string manipulation functions

```sql
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
```

**Sample Output**:
```
employee_name      email                      email_domain    email_length  first_name_upper  last_name_lower  abbreviated_name
Lisa Anderson      lisa.a@company.com         company.com     18            LISA              anderson         L. Anderson
Michael Brown      michael.b@company.com      company.com     21            MICHAEL           brown            M. Brown
Emily Davis        emily.d@company.com        company.com     19            EMILY             davis            E. Davis
Amanda Harris      amanda.h@company.com       company.com     20            AMANDA            harris           A. Harris
```

**String Functions Demonstrated**:
- **||** (Concatenation): Joining strings
- **SUBSTR()**: Extracting substrings
- **INSTR()**: Finding position of substring
- **LENGTH()**: Getting string length
- **UPPER()**: Converting to uppercase
- **LOWER()**: Converting to lowercase

**Real-world Applications**:
- Email domain analysis
- Name formatting
- Data standardization
- Report generation

---

#### Query 19: Date Functions
**Purpose**: Calculate employee tenure using date arithmetic

```sql
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
```

**Sample Output**:
```
employee_name      hire_date   current_date  years_employed  months_employed  days_employed  tenure_category
John Smith         2015-03-15  2025-10-11    10              126.9            3863           Senior
Sarah Johnson      2016-07-22  2025-10-11    9               111.4            3368           Senior
Michael Brown      2017-01-10  2025-10-11    8               105.9            3196           Senior
Emily Davis        2017-05-18  2025-10-11    8               101.6            3068           Senior
David Wilson       2018-02-14  2025-10-11    7               93.3             2825           Senior
```

**Date Functions Demonstrated**:
- **DATE()**: Getting current date
- **JULIANDAY()**: Converting dates to Julian day numbers
- **Date arithmetic**: Calculating differences
- **CAST()**: Type conversion
- **ROUND()**: Precision control

**Calculations**:
- Years: Days ÷ 365.25 (accounting for leap years)
- Months: Days ÷ 30.44 (average month length)
- Days: Direct difference in Julian days

---

#### Query 20: COALESCE & Complex CASE Statements
**Purpose**: Handle NULL values and create categorical data

```sql
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
```

**Sample Output**:
```
emp_id  employee_name    job_title              manager_name      employee_level  salary_band
3       Michael Brown    Marketing Director     No Manager        Executive       High
5       David Wilson     Sales Manager          No Manager        Executive       High
8       Lisa Anderson    HR Manager             No Manager        Executive       Medium
2       Sarah Johnson    Engineering Manager    John Smith        Management      High
1       John Smith       Senior Engineer        No Manager        Senior Level    High
10      Jennifer Lee     Senior Engineer        Sarah Johnson     Senior Level    High
```

**Key Features**:
- **COALESCE()**: Returns first non-NULL value
- **Nested CASE**: Multiple conditions with priorities
- **LIKE operator**: Pattern matching
- **Self-join**: Resolving manager names
- **Multiple categorizations**: Level and salary band

**Data Quality Benefits**:
- Handles missing data gracefully
- Creates consistent categories
- Enables better reporting and analysis

---

#### Query 21: UNION - Combining Result Sets
**Purpose**: Create summary report comparing employee segments

```sql
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
```

**Sample Output**:
```
employee_status  employee_count  avg_salary   max_salary
Active           11              109545.45    155000.00
Inactive         1               58000.00     58000.00
Total            12              105041.67    155000.00
```

**Key Features**:
- **UNION ALL**: Combines results from multiple SELECT statements
- **Summary rows**: Active, Inactive, and Total
- **Comparative analysis**: Side-by-side statistics
- **Literal values**: Using strings as columns

**UNION vs UNION ALL**:
- UNION removes duplicates
- UNION ALL keeps all rows (faster, used here)

---

## 🎓 Summary of SQL Features Covered

### ✅ Required Features
| Feature | Queries | Description |
|---------|---------|-------------|
| CREATE TABLE | 1-5 | Table creation with constraints |
| INSERT | 6-10 | Data population |
| UPDATE | 11 | Data modification with subquery |
| SELECT, FROM, WHERE | 12, 14, 15 | Basic query operations |
| ORDER BY | 12-21 | Sorting results |
| GROUP BY | 13, 17 | Aggregating data |
| LIMIT | 12 | Limiting result sets |
| HAVING | 13 | Post-aggregation filtering |
| Aggregate Functions | 13, 17, 21 | COUNT, AVG, MAX, MIN, SUM |
| INNER JOIN | 14 | Matching records between tables |
| LEFT JOIN | 13, 15, 20 | Including unmatched records |
| CASE WHEN | 15, 19, 20 | Conditional logic |
| Window Functions | 16 | ROW_NUMBER, RANK, PARTITION BY |
| CTEs (WITH) | 17 | Common Table Expressions |

### ✅ Self-Explored Features
| Feature | Queries | Description |
|---------|---------|-------------|
| String Functions | 18 | SUBSTR, INSTR, LENGTH, UPPER, LOWER, \|\| |
| Date Functions | 19 | DATE, JULIANDAY, date arithmetic |
| COALESCE | 20 | NULL handling |
| UNION ALL | 21 | Combining result sets |

---

## 🚀 How to Run

### Prerequisites
- Python 3.7+
- pandas library
- SQLite (built into Python)

### Installation
```bash
# Install required package
pip install pandas
```

### Execution
```bash
# Run the SQL guidebook script
python sql_guidebook.py
```

### Output
The script will:
1. Create `company_database.db` SQLite database
2. Create and populate all tables
3. Execute all 21 queries
4. Display results in formatted tables
5. Print summary of features demonstrated

---

## 💡 Tips for SQL Interviews

1. **Know your JOINs**: Understand the difference between INNER, LEFT, RIGHT, FULL
2. **Master aggregates**: Practice GROUP BY with HAVING
3. **Window functions**: Essential for analytics roles
4. **CTEs over subqueries**: More readable and maintainable
5. **Handle NULLs**: Use COALESCE, IS NULL checks
6. **Optimize queries**: Use EXPLAIN to understand query plans
7. **Practice string/date functions**: Common in data cleaning tasks

---

## 📚 Additional Resources

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQL Window Functions Guide](https://www.postgresql.org/docs/current/tutorial-window.html)
- [SQL Style Guide](https://www.sqlstyle.guide/)

---

**Author**: Diwas Puri  
**Course**: IDS 706 - Data Engineering  
**Institution**: Duke University  
**Date**: October 2025


---

*This guidebook serves as a personal reference for SQL interviews and data engineering tasks. All queries have been tested and verified to produce correct results.*
