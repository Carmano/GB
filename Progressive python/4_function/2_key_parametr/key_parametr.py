def create_dict_arg(**kwargs):
    arg_dict = {}
    for key, value in kwargs.items():
        if type(key) in (dict, tuple, list, set, bytearray):
            arg_dict[value] = key
        else:
            arg_dict[str(value)] = key
    return arg_dict


result = create_dict_arg(a=10, b=20, c='test', d=[1, 2, 3], e={'key': 'value'})

for key, value in result.items():
    print(f"{key}: {value}")
