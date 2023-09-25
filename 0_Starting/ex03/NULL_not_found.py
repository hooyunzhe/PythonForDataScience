import math as Math


def NULL_not_found(object: any) -> int:
    # get the type of null
    null_type = type(object)

    # print the name, value and type of NULL
    # for checking NaN values, object != object would work
    # as the convention of NaN is that it isn't equal to anything
    # but it's not robust or explicit enough
    # given that operator overloading exists
    if object is None:
        print(f"Nothing: {object} {null_type}")
    elif null_type is float and Math.isnan(object):
        print(f"Cheese: {object} {null_type}")
    elif null_type is int and object == 0:
        print(f"Zero: {object} {null_type}")
    elif object is False:
        print(f"Fake: {object} {null_type}")
    elif object == "":
        print(f"Empty: {null_type}")
    else:
        print("Type not Found")
        return 1

    # return 0 on success
    return 0
