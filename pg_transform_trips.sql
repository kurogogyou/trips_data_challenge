-- Loading dimension table
merge into datasources 
using (select distinct datasource from raw_trips) as r
on datasources.source_name = r.datasource
--when matched then UPDATE set source_name = r.datasource
when not matched then INSERT values (r.datasource);

-- Loading facts table
merge into trips 
using (
    --explain
    select 
        r.region
        ,ST_GeomFromText(r.origin_coord, 4326) origin_coord
        ,ST_GeomFromText(r.destination_coord, 4326) destination_coord
        ,r."datetime"::TIMESTAMP "datetime"
        ,d.id datasource_id
        ,md5(concat(concat(r.region,r.origin_coord),concat(concat(r.destination_coord,r."datetime"),r.datasource))) trip_id
    from raw_trips r
    join datasources d on r.datasource = d.source_name
) as s
on trips.trip_id = s.trip_id
--when matched then UPDATE set trip_id = s.trip_id
when not matched then INSERT values (s.trip_id,s.region,s.origin_coord,s.destination_coord,s."datetime",s.datasource_id);
