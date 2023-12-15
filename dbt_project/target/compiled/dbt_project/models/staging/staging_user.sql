select 
    user_id
    ,name -> 'first' as first_name
    ,name -> 'last' as last_name
    ,seed as seed
    ,dob -> 'date' as dob
    ,sa.age_id
    ,sg.gender_id
    ,sn.nationality_id
from "warehouse"."raw"."users" ru
inner join "warehouse"."analytics"."staging_age" sa
on ru.dob -> 'age' = sa.age
inner join "warehouse"."analytics"."staging_gender" sg
on ru.gender = sg.gender
inner join "warehouse"."analytics"."staging_nationality" sn
on ru.nat = sn.nationality