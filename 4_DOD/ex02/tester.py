from callLimit import callLimit


# apply limiter to functions
@callLimit(3)
def f():
    print("f()")


@callLimit(2)
def g():
    print("g()")


@callLimit(1)
def h():
    print("h()")


# should call f() 3 times
# should call g() 2 times
# should call h() 1 time
for i in range(3):
    f()
    g()
    h()
