# Generator Test
import sieve

def test1():
    sieveInstance = sieve.next()
    i = iter(sieveInstance)
    assert i.next() == 3
    print "Test 1 Passes"

def test2():
    sieveInstance = sieve.next()
    i = iter(sieveInstance)
    #i.next()
    assert i.next() == 5
    print "Test 2 Passes"

def test3():
    sieveInstance = sieve.next()
    i = iter(sieveInstance)
    assert i.next() == 7
    print "Test 3 Passes"


test1()
test2()
test3()
