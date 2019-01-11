v1.0
=
## Build
```bash
git clone https://github.com/la9ran9e/2gis_spyder.git && \
cd 2gis_spyder && \
git checkout v1.0 && \
make build
```

## Use Example

### Find and grep objects
```bash
2gis_spyder$ touch filials
2gis_spyder$ ./obj_finder.py moscow filials https://2gis.ru/sitemap.xml > filials
2gis_spyder$ wc -l filials
693162 filials
2gis_spyder$ head -3 filials
https://2gis.ru/moscow/branches/70000001025953070
https://2gis.ru/moscow/firm/70000001033044306
https://2gis.ru/moscow/branches/4504136499348120
2gis_spyder$ head -10 filials | grep firm
https://2gis.ru/moscow/firm/70000001033044306
https://2gis.ru/moscow/firm/4504127915939078
https://2gis.ru/moscow/firm/70000001021522364
https://2gis.ru/moscow/firm/70000001030669439
https://2gis.ru/moscow/firm/70000001034331061
https://2gis.ru/moscow/firm/4504127908875013
2gis_spyder$
```
### Grep content
```bash
2gis_spyder$ cat filials | ./grep.py grep_config.json 
https://2gis.ru/moscow/branches/70000001025953070|{"name": "Левша", "type": "Торговый комплекс"}
https://2gis.ru/moscow/firm/70000001033044306|{"name": "Левша", "type": "Торговый комплекс", "phone": "+7 (495) 662–12–42"}
https://2gis.ru/moscow/branches/4504136499348120|{"name": "Левша", "type": "Салон красоты", "phone": "+7 (495) 662–12–42"}
to be continued ...
```

### Store data
* #### SQLite3
```bash
2gis_spyder$ cat filials | ./grep.py grep_config.json | ./store.sh test 'url TEXT, data TEXT'
... a few moments later
2gis_spyder$ sqlite3 store.db
SQLite version 3.19.3 2017-06-27 16:48:08
Enter ".help" for usage hints.
sqlite> select * from test limit 3;
https://2gis.ru/moscow/branches/70000001025953070|{"name": "Левша", "type": "Торговый комплекс"}
https://2gis.ru/moscow/firm/70000001033044306|{"name": "Левша", "type": "Торговый комплекс", "phone": "+7 (495) 662–12–42"}
https://2gis.ru/moscow/branches/4504136499348120|{"name": "Левша", "type": "Салон красоты", "phone": "+7 (495) 662–12–42"}
to be continued ...
```