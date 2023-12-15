with unique_age as (
    select
        distinct dob -> 'age' as age
    from {{ source('raw', 'users') }}
)

select 
    row_number() over(order by age) as age_id
    ,age
from unique_age

