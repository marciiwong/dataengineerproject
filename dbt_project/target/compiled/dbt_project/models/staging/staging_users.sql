SELECT
    user_id::VARCHAR(255),
    name -> 'first' AS first_name,
    (name ->> 'last')::VARCHAR(255) AS last_name,
    seed::VARCHAR(255) AS seed,
    (dob ->> 'date')::VARCHAR(10) AS dob,
    (dob ->> 'age')::INT AS age,
    nat::VARCHAR(100) AS nationality,
    gender::VARCHAR(5) AS gender
FROM "warehouse"."raw"."users"