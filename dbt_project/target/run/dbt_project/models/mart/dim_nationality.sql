
  
    

  create  table "warehouse"."analytics"."dim_nationality__dbt_tmp"
  
  
    as
  
  (
    with unique_nationality as (
    select
        distinct nationality
    from "warehouse"."analytics"."staging_users"
)

select 
    row_number() over(order by nationality) as nationality_id
    ,nationality
from unique_nationality
  );
  