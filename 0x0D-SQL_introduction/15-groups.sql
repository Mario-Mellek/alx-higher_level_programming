-- A script that lists the number of records with the same score in the second_table.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score Order By number DESC;
