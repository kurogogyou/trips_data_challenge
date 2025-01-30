-- Weekly average for region
select 
    AVG(total_trips) weekly_average
from (
    SELECT 
        DATE_TRUNC('week', t."datetime")::DATE as week_start
        ,COUNT(*) as total_trips
    from trips t
    where t.region = {region}
    group by week_start
    ) as average
;
