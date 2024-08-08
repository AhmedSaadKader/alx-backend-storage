-- SQL script that ranks country origins of bands
-- ordered by the numbr of (non-unique) fans
SELECT origin AS origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY SUM(fans) DESC;
