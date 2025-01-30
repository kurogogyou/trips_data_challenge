-- Regions where "cheap_mobile" datasource appears
--explain
select distinct 
    t.region
from trips t 
join (
    select d.id from datasources d 
    where d.source_name = 'cheap_mobile'
    ) d on t.datasource_id = d.id
;