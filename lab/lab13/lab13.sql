.read data.sql

-- Q1
create table flight_costs as
  with
    ticket_cost(day, yesterday_cost, today_cost) as (
      select 1 as day, 0 as yesterday_cost, 20 as today_cost union
      select 2       , 20                 , 30               union
      select 3       , 30                 , 40               union
      select day + 1 , today_cost         , (today_cost + yesterday_cost) / 2 + ((day + 1) % 7) * 5
        from ticket_cost where day < 25 and day > 2
    )
    select day as day, today_cost as today_cost from ticket_cost;

-- Q2
create table schedule as
with SFO_to_PDX(route, price) as(
  select former.departure || ', ' || former.arrival || ', ' || latter.arrival as route,
         former.price + latter.price                          as price
    from flights as former, flights as latter
    where former.arrival = latter.departure and former.departure = 'SFO' and latter.arrival = 'PDX' union
  select departure || ', ' || arrival as route, price as price from flights where departure = 'SFO' and arrival = 'PDX'
  )
  select * from SFO_to_PDX order by price;
-- Q3
create table shopping_cart as
  with cart(items, last_price, left_buget) as (
    select item, price, 60 - price from supermarket 
    where price <= 60 union

    select items || ', ' || item, price, left_buget - price
    from cart, supermarket
    where price <= left_buget and price >= last_price
  )
  select items, left_buget from cart order by left_buget, items;

-- Q4
create table number_of_options as
  select count(distinct meat) from main_course;

-- Q5
create table calories as
  select count(*) from main_course, pies
  where main_course.calories + pies.calories < 2500;

-- Q6
create table healthiest_meats as
  select meat as meat, min(main_course.calories + pies.calories) as calories 
    from main_course, pies
    group by meat 
    having max(main_course.calories + pies.calories) < 3000;

-- Q7
create table average_prices as
  select category, avg(MSRP) from products group by category;

-- Q8
create table lowest_prices as
  select item, store, price from inventory
   group by item having price = min(price);

-- Q9
create table shopping_list as
  select name, store from products, lowest_prices
  where item = name group by category
  having min(MSRP/rating) = MSRP/rating;

-- Q10
create table total_bandwidth as
  select sum(stores.Mbs) from stores, shopping_list
  where stores.store = shopping_list.store;
