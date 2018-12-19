v1.0
=
## Build
```bash
git clone https://github.com/la9ran9e/2gis_spyder.git && \
cd 2gis_spyder && \
make build
```

## Use Example
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
