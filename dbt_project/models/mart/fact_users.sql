select 
    user_id
    ,first_name
    ,last_name
    ,seed as seed
    ,dob
    ,dd.dim_date_id
    ,sg.gender_id
    ,sn.nationality_id
from {{ ref('staging_users') }} ru
inner join {{ ref('dim_date') }} dd
on ru.dob::date = dd.date::date 
inner join {{ ref('dim_gender') }} sg
on ru.gender = sg.gender
inner join {{ ref('dim_nationality') }} sn
on ru.nationality = sn.nationality