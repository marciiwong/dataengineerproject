select 
    user_id
    ,first_name
    ,last_name
    ,seed as seed
    ,dob
    ,dd.dim_date_id
    ,sg.gender_id
    ,sn.nationality_id
from "warehouse"."analytics"."staging_users" ru
inner join "warehouse"."analytics"."dim_date" dd
on ru.dob::date = dd.date::date 
inner join "warehouse"."analytics"."dim_gender" sg
on ru.gender = sg.gender
inner join "warehouse"."analytics"."dim_nationality" sn
on ru.nationality = sn.nationality