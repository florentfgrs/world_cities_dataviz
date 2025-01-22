INSTALL spatial ; LOAD spatial ;

CREATE TABLE raw_data as SELECT * FROM read_parquet("geonames-all-cities-with-a-population-1000.parquet");