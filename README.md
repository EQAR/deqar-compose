# deqar-compose

## Docker Compose setup for DEQAR backend

Getting started:

- Run `git submodule update` to clone the submodules [eqar_backend](https://github.com/EQAR/eqar_backend) and [deqar_solr](https://github.com/EQAR/deqar_solr)
- Place required Solr modules into `solr/lib/`
- Create `settings_local.py` from `settings_local.example.py`
- Create `.env` with at least the following variables:
   - `DJANGO_SECRET_KEY`: Django secret key
   - `DEQAR_DB_NAME`: PostgreSQL database name
   - `DEQAR_DB_PASS`: PostgreSQL password
   - `DEQAR_API_PORT`: port on which to expose DEQAR API
   - `DEQAR_DB_PORT`: port on which to expore PostgreSQL
- Optionally: place database dump in `initdb.d/`
- Run `docker-compose up`

