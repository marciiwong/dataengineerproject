with unique_nationality as (
    select
        distinct nationality
    from {{ ref('staging_users') }}
)

select 
    row_number() over(order by nationality) as nationality_id
    ,nationality
from unique_nationality

