-- a SQL script that lists all bands with Glam rock as their main style

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;