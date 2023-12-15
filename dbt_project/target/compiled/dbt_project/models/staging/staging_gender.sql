with unique_gender as (
    select
        distinct gender as gender
    from "warehouse"."raw"."users"
)

select 
    row_number() over(order by gender) as gender_id
    ,gender
from unique_gender