select 
    user_id
    ,name -> 'first' as first_name
    ,name -> 'last' as last_name
    ,seed as seed
    ,dob -> 'date' as dob
    ,sa.age_id
    ,sg.gender_id
    ,sn.nationality_id
from {{ source('raw', 'users') }} ru
inner join {{ ref('staging_age') }} sa
on ru.dob -> 'age' = sa.age
inner join {{ ref('staging_gender') }} sg
on ru.gender = sg.gender
inner join {{ ref('staging_nationality') }} sn
on ru.nat = sn.nationality