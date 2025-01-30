drop TABLE if exists raw_trips;
create table raw_trips (
    region VARCHAR(20)
    ,origin_coord VARCHAR(50)
    ,destination_coord VARCHAR(50)
    ,datetime VARCHAR(30)
    ,datasource VARCHAR(50)
);
create index raw_trips_datasource on raw_trips(datasource);

drop table if exists processed_files;
create table processed_files (
    file_path VARCHAR(500)
    ,processed_at TIMESTAMP DEFAULT NOW()
);

-- Creating transformed schema
drop table if exists datasources;
create TABLE datasources (
    source_name VARCHAR(20)
    ,id bigserial primary key 
);
create index datasources_source on datasources(source_name);

drop TABLE if exists trips;
create TABLE trips (
    trip_id CHAR(32) primary key
    ,region VARCHAR(20)
    ,origin GEOMETRY(Point, 4326)
    ,destination GEOMETRY(Point, 4326)
    ,datetime TIMESTAMP
    ,datasource_id BIGINT
);
create index trips_re on trips(region);
create index trips_ds on trips(datasource_id);
create index trips_dt on trips(datetime);