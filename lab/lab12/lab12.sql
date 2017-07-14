.read sp16data.sql
.read fa16data.sql

CREATE TABLE obedience AS
  select seven, denero from students;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 8 ORDER BY smallest LIMIT 20;

CREATE TABLE greatstudents AS
  SELECT this.date, this.number, this.pet, this.color, last.color FROM sp16students AS last, students AS this
    WHERE this.date = last.date AND this.number = last.number AND this.pet = last.pet;

CREATE TABLE sevens AS
  SELECT stu.seven FROM students AS stu, checkboxes AS boxes WHERE stu.number = 7 AND boxes.'7' = 'True' AND stu.time = boxes.time;

CREATE TABLE matchmaker AS
  SELECT first.pet, first.song, first.color, second.color FROM students AS first, students AS second
    WHERE first.pet = second.pet AND first.song = second.song AND first.time < second.time;
