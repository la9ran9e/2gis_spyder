v1.0
=
## Build
```bash
git clone https://github.com/la9ran9e/2gis_spyder.git && \
cd 2gis_spyder && \
make build
```

## Use Example

### Find objects
```bash
2gis_spyder$ touch districts
2gis_spyder$ ./obj_finder.py moscow districts https://2gis.ru/sitemap.xml > districts
2gis_spyder$ wc -l districts
145 districts
2gis_spyder$ head -3 districts
https://2gis.ru/moscow/geo/4504209512726631
https://2gis.ru/moscow/geo/4504209512726572
https://2gis.ru/moscow/geo/4504209512726565
2gis_spyder$
```
### Grep raw data
```bash
2gis_spyder$ ./obj_finder.py moscow filials https://2gis.ru/sitemap.xml | ./grep.py grep_config.json 
{}
{"contact__phonesItem _type_phone": "+7 (495) 662\u201312\u201342"}
{"contact__phonesItem _type_phone": "+7 (495) 662\u201312\u201342"}
{"contact__phonesItem _type_phone": "+7 (495) 913\u201384\u201300"}
{"contact__phonesItem _type_phone": "+7 (495) 913\u201384\u201300"}
{"contact__phonesItem _type_phone": "+7 (495) 258\u201318\u201308"}
{"contact__phonesItem _type_phone": "+7 (495) 258\u201318\u201308"}
to be continued ...
```