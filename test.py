create table schedule as
  with trips(path, ending, flights, cost) as (
    select departure || ", " || arrival, arrival, 1, price from flights
      where departure = "sfo" union
    select path || ", " || arrival, arrival, flights + 1, cost + price
      from trips, flights
      where ending = departure
  )
  select path, cost from trips where ending = "pdx" order by cost;