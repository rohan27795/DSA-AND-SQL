# Write your MySQL query statement below
 select department,employee,salary from
(select d.name as department,e.name as employee,e.salary as salary,
 DENSE_RANK() OVER (
  PARTITION BY d.name
  ORDER BY e.salary DESC
) AS ranks
from employee e
left join department d
on e.departmentId = d.id) as temp 
where ranks <=3

