create table non_parents as
  with 
    grand_parents(grandparent, grandchild) as (
      select a.parent as grandparent, b.child as grandchild 
        from parents as a, parents as b
        where a.child = b.parent
    ),
    grand_relationship(grand_first, grand_second) as(
      select grandparent, grandchild from grand_parents union
      select grandchild, grandparent from grand_parents
    )

    select a.grand_first as ancestor, b.grand_second as descendent 
      from grand_relationship as a, grand_relationship as b, 
           parents as c, dogs as d, dogs as e
      where a.grand_first <> c.parent and b.grand_second <> c.child or 
            a.grand_first <> c.child and b.grand_second <> c.parent and 
            d.name = a.grand_first and e.name = b.grand_second
      group by b.grand_second, a.grand_first
      order by d.height - e.height
      ;