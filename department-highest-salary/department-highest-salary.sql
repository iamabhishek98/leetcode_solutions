# Write your MySQL query statement below
select D.Name as Department, E.Employee, E.Salary from
(select e.DepartmentId as DepartmentId,e.Name as Employee,e.Salary from Employee e inner join
(select DepartmentId, MAX(Salary) as max from Employee group by DepartmentId) m
on (e.DepartmentId = m.DepartmentId and e.Salary = m.MAX)) E, Department D
where E.DepartmentId = D.Id; 