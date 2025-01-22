import polars as pl
import duckdb
import requests
from pathlib import Path


def download_data():
    url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/geonames-all-cities-with-a-population-1000/exports/parquet?lang=fr&timezone=Europe%2FBerlin"
    local_filename = "geonames-all-cities-with-a-population-1000.parquet"

    if not Path(local_filename).exists():
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_filename, "wb") as file:
                file.write(response.content)


def prepare_data():
    con = duckdb.connect()

    with open("./sql/data.sql", "r") as file:
        query = file.read()
        con.sql(query)

    df_duckdb = con.execute(
        "SELECT name, cou_name_en, population, st_x(coordinates) as long, st_y(coordinates) as lat, population / 100 as size from raw_data"
    ).fetchdf()

    return pl.from_pandas(df_duckdb)


download_data()
