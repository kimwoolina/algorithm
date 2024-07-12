from hashtable.structures import MyHashTable


def test_hashtable():
    ht = MyHashTable()

    ht.put(1, 1)
    ht.put(2, 2)
    assert ht.get(1) == 1
    assert ht.get(3) == -1

    ht.put(2, 1)
    assert ht.get(2) == 1

    ht.remove(2)
    assert ht.get(2) == -1
    


if __name__ == "__main__":
    test_hashtable()