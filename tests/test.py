import pytest

from union_find_easy import Item, Union

def test_union_find_2():
    item1 = Item(1)
    item2 = Item(2)
    item1.union(item2)
    assert item1.rep == item2.rep
    assert item1.find().weight == 2

def test_union_find_many():
    items = [ Item(1) for _ in range(5) ]
    Union(*items)
    assert all(( i1.find() == i2.find() for i1, i2 in zip(items, items[1:])))
    assert all(( i.member_count() == len(items) for i in items ))

def test_union_find_merge():
    items1 = [ Item(1) for _ in range(5) ]
    items2 = [ Item(1) for _ in range(5) ]
    items = items1 + items2
    Union(*items1)
    Union(*items2)
    items1[0].union(items2[0])
    assert all(( i1.find() == i2.find() for i1, i2 in zip(items, items[1:])))
