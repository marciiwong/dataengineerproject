select 
    user_id::varchar(255) as user_id
    ,first_name::varchar(255) as first_name
    ,last_name::varchar(255) as last_name
    ,seed::varchar(255) as seed
    ,dob::date as dob
    ,sg.gender_id::int as gender_id
    ,sn.nationality_id::int as nationality_id
    ,ru.reg_date::date as reg_date
from {{ ref('staging_users') }} ru
inner join {{ ref('dim_date') }} dd
on ru.dob::date = dd.date::date 
inner join {{ ref('dim_gender') }} sg
on ru.gender = sg.gender
inner join {{ ref('dim_nationality') }} sn
on ru.nationality = sn.nationality