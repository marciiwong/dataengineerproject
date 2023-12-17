
  
    

  create  table "warehouse"."analytics"."dim_age__dbt_tmp"
  
  
    as
  
  (
    with unique_age as (
    select
        distinct age
    from "warehouse"."analytics"."staging_users"
)

select 
    row_number() over(order by age) as age_id
    ,age
from unique_age
  );
  