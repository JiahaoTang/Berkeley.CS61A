.read lab12.sql

CREATE TABLE count_number AS 
  SELECT number, COUNT(*) AS count FROM sp16students GROUP BY number
    ORDER BY count DESC LIMIT 10;

CREATE TABLE sp16favnum AS
  SELECT number, max(count) AS fav_num FROM count_number;


CREATE TABLE sp16favpets AS
  SELECT pet, COUNT(*) AS count FROM sp16students GROUP BY pet
    ORDER BY count DESC LIMIT 10;


CREATE TABLE fa16favpets AS
  SELECT pet, COUNT(*) AS count FROM students GROUP BY pet
    ORDER BY count DESC LIMIT 10;


CREATE TABLE fa16dragon AS
  SELECT pet, COUNT(*) AS count FROM students WHERE pet = 'dragon';


CREATE TABLE fa16alldragons AS
  SELECT pet, COUNT(*) AS count FROM students WHERE pet LIKE '%dragon%';


CREATE TABLE obedienceimage AS
  SELECT seven, denero, COUNT(*) AS count FROM students WHERE seven = '7' GROUP BY denero ORDER BY denero;

CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) AS count FROM students WHERE smallest > 0 GROUP BY smallest;
