-- Lists all the cities contained in the database, including the state amemand ordered by cities id
SELECT cities.id,cities.name,states.name FROM cities JOIN states ON cities.state_id = states.id;
