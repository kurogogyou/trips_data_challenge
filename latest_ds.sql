with ranked_trips as (
    select t.region, --count(*) as region_count,
           rank() over (order by count(1) desc) as region_rank
    from trips t
    group by region
    limit 2
),
latest_trip AS (
    select d.source_name, 
           row_number() over (partition by t.region ORDER BY t.datetime DESC) as rn
    from trips t
    join datasources d on t.datasource_id = d.id
    JOIN ranked_trips r ON t.region = r.region
)
select l.source_name from latest_trip l
where rn = 1
limit 1;