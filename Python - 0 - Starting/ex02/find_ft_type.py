def all_thing_is_obj(object: any) -> int:

    type_name = {
        list : "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str : "is at home"
    }

    if (type(object)) in type_name:
        if (type(object) == str):
            print(f"{object} is at kitchen : {type(object)}")
        else:
            print(f"{type_name[type(object)]} : {type(object)}")
    else:
        print(f"Type not found")
    return (42)