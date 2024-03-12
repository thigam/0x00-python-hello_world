-- Lists the number of records with the same score in the table secondTable
SELECT score, COUNT(*)
FROM second_table
GROUP BY score;
