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
{"name": "Левша", "type": "Торговый комплекс", "phone": "+7 (495) 662–12–42"}
{"name": "Левша", "type": " ", "phone": "+7 (495) 913–84–00"}
{"name": "BizBeri", "type": "Бизнес-портал", "phone": "+7 (495) 913–84–00"}
{"name": "Юниджет", "type": "Компания", "phone": "+7 (495) 258–18–08"}
{"name": "Юниджет", "type": " ", "phone": "+7 (499) 390–20–55"}
{"name": "Юниджет", "type": " ", "phone": "+7 (495) 506–54–93"}
{"name": "Юниджет", "type": " ", "phone": "+7 (499) 390–20–55"}
{"name": "Юниджет", "type": " ", "phone": "+7 (499) 169–01–15"}
{"name": "Юниджет", "type": " ", "phone": "+7 (499) 169–01–15"}
{"name": "Бизнес Фокус, ООО", "type": "Компания", "phone": "+7 (499) 350–62–80"}
{"name": "Бизнес Фокус, ООО", "type": " ", "phone": "+7 (495) 966–41–48"}
{"name": "Бизнес Фокус, ООО", "type": " ", "phone": "+7 (495) 966–41–48"}
to be continued ...
```