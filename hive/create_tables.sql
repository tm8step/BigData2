-- This is the SQL code used to create and load the table into Hive.  It is launched from inside Hive.

CREATE TABLE econdata_ilwi(
`case_id` INT,
`state_abv` STRING,
`county` STRING,
`housing` FLOAT,
`total_cost` FLOAT,
`min_wage` FLOAT,
`taxes` FLOAT,
`metro_level` INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/data'
tblproperties("skip.header.line.count"="1");
