-- Query for question 1
-- What is the population count by age group in the increment of 10 up to 100?

with age_list as (
select * from generate_series(0,100,10) as age
),

age_bucket as (
select 
al2.age as lower_bucket_age,
al.age as upper_bucket_age
from age_list al
join age_list al2
on al.age = al2.age + 10
),

users_age as (
select dob, EXTRACT(YEAR FROM age(dob)) as age from analytics.fact_users
)

select concat(lower_bucket_age, '<', upper_bucket_age) as age_bucket, count(*) from users_age ua
left join age_bucket ab
on ua.age >= lower_bucket_age and ua.age < upper_bucket_age
group by concat(lower_bucket_age, '<', upper_bucket_age)
order by concat(lower_bucket_age, '<', upper_bucket_age)


-- Query for question 2
-- Is there any difference in the number of registrations over the week?
select dd.day_of_week as reg_month, count(*) from analytics.fact_users fu
left join analytics.dim_date dd
on fu.reg_date = dd.date
group by dd.day_of_week
order by dd.day_of_week


--Query for question 3
-- What are the top 5 nationalities of the users?
select nationality, count(*)
from analytics.fact_users fu
left join analytics.dim_nationality n
on fu.nationality_id = n.nationality_id
group by nationality
order by count(*) desc
limit 5