-- These were the Queries used to validate the Hive table

-- This query finds the average of the taxes column, rounded to  2 decimals.
SELECT ROUND(AVG(taxes), 2) FROM econdata_ilwi;

-- Result 7226.2

-- This query finds the maximum housing for each state, IL and WI
SELECT state_abv, MAX(housing) AS max_housing
FROM econdata_ilwi 
GROUP BY state_abv;

-- Result:  
-- IL      19431.04
-- WI      12422.97

--  This query counts the total number of data entries.
SELECT COUNT(*) FROM econdata_ilwi;

-- Result:  174
