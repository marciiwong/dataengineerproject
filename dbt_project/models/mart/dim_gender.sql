with unique_gender as (
    select
        distinct gender
    from {{ ref('staging_users') }}
)

select 
    row_number() over(order by gender) as gender_id
    ,gender
from unique_gender

