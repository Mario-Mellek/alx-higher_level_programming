-- script that displays the average temperature by city ordered by temperature.
SELECT city, AVG(temp) as avg_temp FROM temperatures GROUP BY city
ORDER BY avg_temp DESC;
