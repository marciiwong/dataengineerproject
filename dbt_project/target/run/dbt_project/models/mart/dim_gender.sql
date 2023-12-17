
  
    

  create  table "warehouse"."analytics"."dim_gender__dbt_tmp"
  
  
    as
  
  (
    with unique_gender as (
    select
        distinct gender
    from "warehouse"."analytics"."staging_users"
)

select 
    row_number() over(order by gender) as gender_id
    ,gender
from unique_gender
  );
  