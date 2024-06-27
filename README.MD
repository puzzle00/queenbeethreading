## 1 README
> ### 1.1 Overview
> > #### 1.1.1 Queen Bees {#qb-overview}
> > > Queen Bees (**`class QueenBee()`**) handle the creation of [Worker Bees](#wb-overview) and the storing of [Drones](#db-overview) (templates for workers.) You generally need one Queen Bee per app. To use a Queen Bee, create one (` q=QueenBee()` ) and call `q.makeBee(d.mate())` where `"d"` is a Drone Bee. 
> > #### 1.1.2 Drone Bees {#db-overview}
> > > Drone Bees (**`class DroneBee(func,**inf)`**) serve as templates to create Worker Bees. Their constructor is passed a callback to a function (func) and metadata, for example a label for the worker bee type it's representing. You usually have several drones per application. 
> > ####  1.1.3 Workers {#wb-overview}
> > > Worker Bees ( __`class WorkerBee()`__ ) handle the actual work defined by the [Drone Bees](#db-overview) they are linked to. They can be dispatched by a [Queen](#qb-overview)'s `begin()` method or [(advanced)](#qo) Queenless Operation.
> ### 1.2 In Detail
> > #### 1.2.1 Queen Bees {#qb}
> > >  _create()
> > > : Creates Workers. *DO NOT CALL YOURSELF UNLESS USING [QUEENLESS OP (ADVANCED)](#qo)*
> > >
> > > makeBee(DroneBee d)
> > > : Stores a [Drone](#db) in the drone repo.
> > >
> > >Begin(label=None)
> > >: Starts the [Worker Bees](#wb).
> > >If `label` param included: starts all the workers with label `label`.
> > >
> > #### 1.2.2 Drone Bees {#db}
> > > \__init\__(func,**inf)
> > > : Initializes the drone with task `func` and info (including label) `inf`.
> > > 
> > > mate()
> > > : clones the drone!
> > > Returns a copy of the drone.
> > > 
> > > process()
> > > : *Do not call yourself. Auto-called by the class.*
> > > Processes the meta-info `inf` dict.
> > >
> > > retask(func)
> > > : Gives the drone a new task to use.
> > > *__Some info__: This is why you always use mate().*
> > #### 1.2.3 Worker Bees {#wb}
> > > go()
> > > : *DO NOT CALL YOURSELF UNLESS USING [QUEENLESS OP (ADVANCED)](#qo)*
> > > *Do not call yourself. Auto-called by the Queen class.*
> > > Starts this Worker.
> > >
> > > apply(DroneBee d)
> > > : *DO NOT CALL YOURSELF UNLESS USING [QUEENLESS OP (ADVANCED)](#qo)*
> > > *Do not call yourself. Auto-called by the Queen class.*
> > > Set this worker to a certain [Drone](#db) type.
> > #### 1.2.4 Other Classes
> > > BeeBuffer
> > > : BeeBuffer is the class that queues the bees while waiting for a turn to run.
> ### 1.3 Queenless Op (Advanced) {#qo}
> *__note__: this is an __advanced topic__. Recommended for experienced people only.*
> > #### 1.3.1 Overview
> > > **Queenless Op is a way you can exert finer control over your [Worker Bees](#wb) by controlling the bees without a queen.**
> > > *__note__: you still need a queen, the queen just isn't controlling your bees.*
> > #### 1.3.2 In Detail
> > > Making Bees
> > > : Instead of letting the queen make worker bees, you create them yourself by using the [Queen](#qb)'s `_create()` method. This will create a blank bee, that you then *infuse* with a drone using the [worker](wb)'s `apply` method, like this:
```python
q=QueenBee()
def myFunc():
    print("Hello World!")
d=DroneBee(myFunc,label="Hello World",tag='test')
emptyBee=q._create()
emptyBee.apply(d)
emptyBee.go()
```
> > > 
> > > Go'ing Bees
> > > : To go (start) a bee, call its `go()` method.
> > > Usually, this method is called by the [Queen](#qb)'s `begin()` method, but in QO, it is called by the user.
> >
> >
>  ### 1.4 Examples {#ex}
>  [show basic Bee Hello World, two-bees, 3-bees]: #
> > #### 1.4.1 Bee Hello 
> > >A simple example of using queenbee to say hello world. (not something you would usually use qb for)
```python
import queenbee as qb

def hello():
    print("Hello World")
q=qb.QueenBee()
d=qb.DroneBee(hello,label="HelloMyBeesHello")
q.makeBee(d.mate())
q.begin()
#or: q.begin("HelloMyBeesHello")

###############
#Output:      #
# Hello World #
###############
```
> > #### 1.4.2 Two Bees
> > > Now something more useful: Two Bees.
```python
import queenbee as qb

def FirstBee():
    print(1,end='')
def SecondBee():
    print(2,end='')
q=qb.QueenBee()
fb=qb.DroneBee(FirstBee,label=1)
sb=qb.DroneBee(SecondBee,label=2)
q.makeBee(fb.mate())
q.makebee(sb.mate())
q.begin()
##############
#Output:     #
# 12 or 21   #
##############
```
> > #### 1.4.3 Three Bees
> > > you know now!
```py
import queenbee as qb
def b1():
    print(1, end='')
def b2():
    print(2,end='')
def b3():
    print(3,end='')
q=qb.QueenBee()
d1=qb.DroneBee(b1,label=1)
d2=qb.DroneBee(b2,label=2)
d3=qb.DroneBee(b3,label=3)
###################################
#Output:                          #
# 123, 132, 213, 231, 312, or 321 #
###################################
```
