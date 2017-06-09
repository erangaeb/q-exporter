# q-exporter

export csv file data into insert query

## query to filter sendconfigs

```
with senz as (select * from t_serviceinfo_t_sendconfig where t_serviceinfo_id in ( select id from t_serviceinfo where service_id = 4))
select 
    t_serviceprovider_t_serviceinfo.t_serviceprovider_id, 
    t_serviceprovider.intermediatorid,
    senz.sendconfigs_id,
    t_sendconfig.validatelegalattachments,
    t_sendconfig_supporteddigsigtypes.digsigtype
from 
    senz,
    t_serviceprovider_t_serviceinfo,
    t_sendconfig,
    t_serviceprovider,
    t_sendconfig_supporteddigsigtypes
where
    t_serviceprovider_t_serviceinfo.serviceinfos_id = senz.t_serviceinfo_id and 
    t_sendconfig.id = senz.sendconfigs_id and
    t_sendconfig_supporteddigsigtypes.t_sendconfig_id = senz.sendconfigs_id and 
    t_serviceprovider_t_serviceinfo.t_serviceprovider_id = t_serviceprovider.id
```

## export insert queries

```
python q_exporter.py
```
