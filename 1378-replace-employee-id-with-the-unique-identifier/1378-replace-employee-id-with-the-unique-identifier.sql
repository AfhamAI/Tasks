# Write your MySQL query statement below
select unique_id , name from Employees em left join EmployeeUNI e on e.id = em.id;