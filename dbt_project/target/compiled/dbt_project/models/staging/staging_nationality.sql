with unique_nationality as (
    select
        distinct nat as nationality
    from "warehouse"."raw"."users"
)

select 
    row_number() over(order by nationality) as nationality_id
    ,nationality
from unique_nationality