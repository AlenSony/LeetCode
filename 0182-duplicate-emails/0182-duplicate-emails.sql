# Write your MySQL query statement be

select distinct p.email as Email from Person p group by p.email having count(*)>1;