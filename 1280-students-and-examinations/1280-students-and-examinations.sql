# Write your MySQL query statement below
select st.student_id,st.student_name,su.subject_name,count(e.student_id) as attended_exams
from students st
cross join subjects su
left join examinations e
on e.subject_name=su.subject_name
and st.student_id=e.student_id
group by st.student_id,st.student_name,su.subject_name
order by st.student_id,su.subject_name
