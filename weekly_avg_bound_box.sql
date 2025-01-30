select 
    AVG(total_trips) weekly_average
from (
    SELECT 
        DATE_TRUNC('week', t."datetime")::DATE as week_start
        ,COUNT(*) as total_trips
    from trips t
    WHERE 
        ST_X(t.origin) BETWEEN {origin_min_x} AND {origin_max_x} -- origin latitude
        AND ST_Y(t.origin) BETWEEN {origin_min_y} AND {origin_max_y}-- origin longitude
        AND ST_X(t.destination) BETWEEN {dest_min_x} AND {dest_max_x} -- dest latitude
        AND ST_Y(t.destination) BETWEEN {dest_min_y} AND {dest_max_y} -- dest longitude
    group by week_start
    ) as average
;