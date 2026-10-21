import queenbeethreading as qb

test1var=False
def test_one_bee():
    q=qb.QueenBee()
    def firstBee():
        global testonevar
        test1var=True
    d=qb.DroneBee(firstBee, label="one")
    q.makeBee(d.mate())
    q.uptask("one",1)
    q.begin()
    assert test1var


test2var1=False
test2var2=False
def test_two_bees():
    q=qb.QueenBee()
    def firstBee():
        global test2var1
        test2var1=True
    
    def secondBee():
        global test2var2
        test2var2=True

    d1=qb.DroneBee(firstBee, label="1")
    q.makeBee(d1.mate())
    d2=qb.DroneBee(secondBee, label="2")
    q.makeBee(d2.mate())

    q.uptask("1",1)
    q.uptask("2",1)
    q.begin()

    assert test2var1 and test2var2



test3var1=False
test3var2=False
test3var3=False
def test_three_bees():
    q=qb.QueenBee()
    def firstBee():
        global test3var1
        test3var1=True

    def secondBee():
        global test3var2
        test3var2=True
    
    def thirdBee():
        global test3var3
        test3var3=True

    d1=qb.DroneBee(firstBee, label="1")
    q.makeBee(d1.mate())
    d2=qb.DroneBee(secondBee, label="2")
    q.makeBee(d2.mate())
    d3=qb.DroneBee(thirdBee, label="3")
    q.makeBee(d3.mate())

    q.uptask("1",1)
    q.uptask("2",1)
    q.uptask("3",1)
    q.begin()
    
    assert test3var1 and test3var2 and test3var3

qovar=False
def test_queenless_op():
    # See that a QueenBee instance is not needed
    def job():
        global qovar
        qovar=True
    d=qb.DroneBee(job, label="j")

    empty=qb.QueenBee.create()
    empty.apply(d)
    empty.go()

