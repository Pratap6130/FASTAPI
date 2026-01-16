# Complete MySQL Commands Reference

## 1. DATABASE MANAGEMENT

```sql
show databases;              -- List all databases

create database data;        -- Create a new database

use data;                    -- Switch to the database
```

## 2. TABLE MANAGEMENT

```sql
show tables;                 -- List all tables in current database

describe products;           -- Show table structure
-- Alternative: DESC products; or EXPLAIN products;

create table products(
    id int, 
    name varchar(50), 
    description varchar(100), 
    price float, 
    quantity int
);
```

## 3. INSERT COMMANDS (Adding Data)

```sql
insert into products values(1, 'laptop', 'HP Victus', 70000, 5);
insert into products values(2, 'Mobile', 'Samsung S21', 60000, 4);
insert into products values(3, 'Tablate', 'Samsung A11', 60000, 4);
insert into products values(4, 'Keyboard', 'Radragon', 4000, 200);
insert into products values(5, 'Mouse', 'Hp', 5500, 150);
insert into products values(6, 'Headphones', 'Sony WH-1000XM4', 25000.0, 30);
insert into products values(7, 'Monitor', 'Dell 27"', 15000.0, 12);
insert into products values(8, 'Keyboard', 'Mechanical RGB', 5000.0, 50);
insert into products values(9, 'Mouse', 'Wireless Logitech', 2000.0, 40);
insert into products values(10, 'Printer', 'HP LaserJet', 12000.0, 8);
```

## 4. SELECT COMMANDS (Basic)

```sql
select * from products;     -- Select all columns and rows

select id, name, quantity from products;
                            -- Select specific columns only
```

## 5. SELECT WITH WHERE CLAUSE (Filtering)

```sql
select * from products where price >= 1000;
                            -- Comparison operators: >=, <=, >, <, =, !=

select * from products where quantity >= 100 and quantity <= 50;
                            -- Logical operators: AND, OR, NOT
                            -- Note: Returns empty (no quantity between 100 and 50)
```

## 6. SELECT WITH LIKE OPERATOR (Pattern Matching)

**LIKE Syntax:**
- `%` = matches any number of characters (0 or more)
- `_` = matches exactly 1 character

```sql
select * from products where name like 'm_____';
-- 6 letters starting with 'm' → Results: Mobile, mobile

select * from products where name like '_____e';
-- 6 letters ending with 'e' → Results: Mobile, mobile

select * from products where name like '____e';
-- 5 letters ending with 'e' → Results: Mouse

select * from products where name like '%e';
-- Any length, ending with 'e' → Results: Mobile, Tablate, Mouse, mobile

select * from products where name like 'e%';
-- Any length, starting with 'e' → Results: Empty set

select * from products where name like '%a%';
-- Contains 'a' anywhere → Results: laptop, Tablate, Keyboard, Headphones
```

## 7. SELECT WITH IN OPERATOR (Multiple Values)

```sql
select * from products where id in(5,7,10,15,8,2,6);
-- Selects rows where id matches any value in the list
-- Returns 8 rows
```

## 8. SELECT WITH BETWEEN OPERATOR (Range)

```sql
select * from products where id between 2 and 50;
-- Selects rows where id >= 2 AND id <= 50
-- Returns 12 rows (all except id=1)
```

## 9. ORDER BY (Sorting)

```sql
select * from products ORDER BY price ASC;   -- Ascending order
select * from products ORDER BY price DESC;  -- Descending order
select * from products ORDER BY name ASC;    -- Sort by name A-Z
```

## 10. LIMIT (Restrict Results)

```sql
select * from products LIMIT 5;              -- First 5 rows

select * from products LIMIT 5 OFFSET 5;     -- Skip first 5, show next 5
```

## 11. GROUP BY (Aggregate)

```sql
select name, COUNT(*) from products GROUP BY name;
-- Count how many products have the same name

select price, COUNT(*) from products GROUP BY price;
-- Count products with same price
```

---

## Quick Reference Tables

### Comparison Operators
| Operator | Meaning |
|----------|---------|
| `=` | Equal to |
| `!=` | Not equal to |
| `<>` | Not equal to (alternative) |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### Logical Operators
| Operator | Meaning |
|----------|---------|
| `AND` | Both conditions must be true |
| `OR` | At least one condition must be true |
| `NOT` | Negates a condition |

### Aggregate Functions
| Function | Purpose |
|----------|---------|
| `COUNT()` | Count number of rows |
| `SUM()` | Sum all values in column |
| `AVG()` | Calculate average |
| `MAX()` | Get maximum value |
| `MIN()` | Get minimum value |

### LIKE Pattern Symbols
| Symbol | Matches |
|--------|---------|
| `%` | Any number of characters (0 or more) |
| `_` | Exactly 1 character |
| `[ABC]` | Any character in brackets |
| `[^ABC]` | Any character NOT in brackets |

---

## Useful Query Patterns

```sql
-- Get total products
SELECT COUNT(*) FROM products;

-- Get average price
SELECT AVG(price) FROM products;

-- Get total quantity in stock
SELECT SUM(quantity) FROM products;

-- Most expensive product
SELECT * FROM products ORDER BY price DESC LIMIT 1;

-- Least expensive product
SELECT * FROM products ORDER BY price ASC LIMIT 1;

-- Count products by name
SELECT name, COUNT(*) FROM products GROUP BY name;

-- Products in specific price range
SELECT * FROM products WHERE price BETWEEN 5000 AND 50000;

-- Get expensive products with low quantity
SELECT * FROM products WHERE price > 50000 AND quantity < 10;

-- Get products that don't start with 'M'
SELECT * FROM products WHERE name NOT LIKE 'm%';


```


alter-> add new column 
alter table products add column MFDate date
