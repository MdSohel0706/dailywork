/*
LIKE CLAUSE : 
Symbol meanings:
% : any number of characters
_ : single character

Examples:
select * from table where first name like "b%" - returns all rows whose first
name start with b

like "b_y" - returns all rows where field starts with b and ends with y

REGULAR EXPRESSION : 
Symbol meanings:
^ : at the beginning of a string
$ : at the end of a string
| : used as or for multiple regexp
[] : used to give multiple characters or a range of values

Examples: where firstname regexp "^field" : first name beginning with field
regexp "field$" : ending with field
regexp "field|mac" : having field or mac in it
regexp "[gim]e" : having ge or ie or me
regexp "[a-p] : having alphabet in range from a to p

LIMIT CLAUSE:
select * from customers order by salary desc limit 10, 20 : 10 is offset 
and 20 is limit

INNER JOIN:
select order_d, order.customer_id, first_name, last_name 
from orders o
join customers c 
on o.customer_id = c.customer_id

JOINING ACCROSS DIFFERENT DATABASES:
just need to prefix table name with database name and use . to access table
of a database we are not currently using.

SELF JOIN:
select e.employee_id,
e.first_name,
m.first_name as manager
from employee e 
join employees m
on e.reports_to = m.employee_id

CROSS JOIN (normal join syntax without where or on clause):
select * from table1, table2

OUTER JOIN:
1. LEFT JOIN: Joins all rows of left table with matching rows of right table
2. RIGHT JOIN: Joins all rows of right table with matching rows of left table

SELF OUTER JOIN:
Joins like outer but same table used twice

USING CLAUSE:
select * from table1
join
table2 
using (common_field_name)

NATURAL JOIN (joins without any on clause, finds matching field names from
both tables if * is given, but explicitly fields can also be selected)

select 
o.order_id,
c.first_name
from orders o 
natural join customers c

CROSS JOIN(makes all possible combinations between specified fields):
Implicit syntax:
select * from table1, table2
Explicit syntax:
select
	c.first_name as customer,
    p.name as product
from customers c
cross join products p
order by c.first_name    

UNION:
select customer_id, first_name, points, "Silver" as type
from customers
where points between 2000 and 3000
union
select customer_id, first_name, points, "Gold" as type
from customers
where points > 3000
*/