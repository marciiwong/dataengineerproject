
  
    

  create  table "warehouse"."analytics"."fact_users__dbt_tmp"
  
  
    as
  
  (
    select 
    user_id::varchar(255) as user_id
    ,first_name::varchar(255) as first_name
    ,last_name::varchar(255) as last_name
    ,seed::varchar(255) as seed
    ,dob::date as dob
    ,sg.gender_id::int as gender_id
    ,sn.nationality_id::int as nationality_id
    ,ru.reg_date::date as reg_date
from "warehouse"."analytics"."staging_users" ru
inner join "warehouse"."analytics"."dim_date" dd
on ru.dob::date = dd.date::date 
inner join "warehouse"."analytics"."dim_gender" sg
on ru.gender = sg.gender
inner join "warehouse"."analytics"."dim_nationality" sn
on ru.nationality = sn.nationality
  );
  