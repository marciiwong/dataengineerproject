SELECT TO_CHAR(datum, 'yyyymmdd')::INT AS dim_date_id,
       datum::date AS date,
       TO_CHAR(datum, 'TMDay') AS day_name,
       EXTRACT(ISODOW FROM datum) AS day_of_week,
       EXTRACT(DAY FROM datum) AS day_of_month,
       EXTRACT(DOY FROM datum) AS day_of_year,
       TO_CHAR(datum, 'W')::INT AS week_of_month,
       EXTRACT(WEEK FROM datum) AS week_of_year,
       EXTRACT(ISOYEAR FROM datum) || TO_CHAR(datum, '"-W"IW-') || EXTRACT(ISODOW FROM datum) AS week_of_year_iso,
       EXTRACT(MONTH FROM datum) AS month_actual,
       TO_CHAR(datum, 'TMMonth') AS month_name,
       TO_CHAR(datum, 'Mon') AS month_name_abbreviated
FROM (
   select * 
      from 
      generate_series(
         (select min(dob)::date from "warehouse"."analytics"."staging_users"), 
         (select current_date::date),
         '1 day'
      ) as datum
) DQ
ORDER BY 1