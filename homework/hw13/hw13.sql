create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  SELECT name, size FROM dogs, sizes 
    WHERE dogs.height > sizes.min AND dogs.height <= sizes.max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  SELECT child FROM parents, dogs WHERE name = parent
    ORDER BY height desc
    ;

-- Sentences about siblings that are the same size
create table sentences as
with siblings(sibling1, sibling2) as (
    select a.child as sibling1, b.child as sibling2 from parents as a, parents as b
    where a.parent = b.parent and a.child <> b.child and a.child < b.child
  ) 
  select a.sibling1 || ' and ' || a.sibling2 || ' are ' || b.size || ' siblings'
    from siblings as a, size_of_dogs as b, size_of_dogs as c
    where b.name = a.sibling1 and c.name = a.sibling2 and b.size = c.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  select a.name || ', ' || b.name || ', ' || c.name || ', ' || d.name, 
         a.height + b.height + c.height + d.height
    from dogs as a, dogs as b, dogs as c, dogs as d
    where a.name <> b.name and a.name <> c.name and a.name <> d.name and
          b.name <> c.name and b.name <> d.name and c.name <> d.name and
          a.height < b.height and b.height < c.height and c.height < d.height and
          a.height + b.height + c.height + d.height >= 170
    order by a.height + b.height + c.height + d.height;

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
create table non_parents as
  with 
    grand_relationship1(grandparent, grandchild) as (
      select a.parent as grandparent, b.child as grandchild 
        from parents as a, parents as b
        where a.child = b.parent),
    grand_relationship2(grandchild, grandparent) as (
      select b.child as grandparent, a.parent as grandchild 
        from parents as a, parents as b
        where a.child = b.parent
      )
    
    select a.grandparent as ancestor, b.grandchild as descendent 
      from grand_relationship1 as a, grand_relationship1 as b, 
           parents as c, dogs as d, dogs as e
      where a.grandparent <> c.parent and b.grandchild <> c.child and 
            d.name = a.grandparent and e.name = b.grandchild
      group by b.grandchild, a.grandparent
      order by d.height - e.height --union
    
    --select a.grandchild as ancestor, b.grandparent as descendent 
      --from grand_relationship2 as a, grand_relationship2 as b, 
        --   parents as c, dogs as d, dogs as e
      --where b.grandparent <> c.parent and a.grandchild <> c.child and 
        --    d.name = b.grandparent and e.name = a.grandchild
      --group by a.grandchild, b.grandparent
      --order by d.height - e.height
      ;

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
  with
    merge(number, second) as (
      select a.n as number, b.n as second from ints as a, ints as b
      where b.n <= a.n
    )
    select number, count(*) as divisors_count from merge
      where number % second == 0
      group by number;

create table primes as
    select number from divisors where divisors_count = 2;
