def all_thing_is_obj(object: any) -> int:
    # get the type of the object
    object_type = type(object)

    # print the types
    # match case would work here with
    #
    # match object:
    #    case type():
    #    ...
    #    case _:
    #
    # but it's meant for structural pattern matching
    # rather than equality checks
    if object_type is list:
        print(f"List : {object_type}")
    elif object_type is tuple:
        print(f"Tuple : {object_type}")
    elif object_type is set:
        print(f"Set : {object_type}")
    elif object_type is dict:
        print(f"Dict : {object_type}")
    elif object_type is str:
        print(f"{object} is in the kitchen : {object_type}")
    else:
        print("Type not found")

    # return the answer to the
    # ultimate question of life,the universe and everything
    return 42
