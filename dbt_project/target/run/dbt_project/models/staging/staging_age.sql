
  
    

  create  table "warehouse"."analytics"."staging_age__dbt_tmp"
  
  
    as
  
  (
    with unique_age as (
    select
        distinct dob -> 'age' as age
    from "warehouse"."raw"."users"
)

select 
    row_number() over(order by age) as age_id
    ,age
from unique_age
  );
  