select * from (SELECT student, avg(score) sc from STUDENT GROUP BY student) a where a.sc > 80
select name from Persons group by name having count(name) = 2;