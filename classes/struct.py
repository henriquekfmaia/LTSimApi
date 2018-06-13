import json

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def get_structs(raw_object):
    if type(raw_object) is list:
        ret = []
        for item in raw_object:
            ret.append(get_structs(item))
        return ret
    elif type(raw_object) is dict:
        ret = Struct(**raw_object)
        for item in raw_object:
            setattr(ret, item, get_structs(raw_object[item]))
        if('value' in raw_object):
            write_to_output(raw_object, ret)
        return ret

    else:
        return raw_object

def convert_to_dict(struct):
    s_dict = struct.__dict__
    for element in s_dict:
        element = convert_to_dict(element)

    return s_dict

def write_to_output(raw_object, ret):
    a = str(raw_object)
    b = str(ret.value)
    c = str(ret)
    f = open('output.txt', 'a')
    f.write(a)
    f.write('\n')
    f.write(b)
    f.write('\n')
    f.write(c)
    f.write('\n')
    f.write('\n')
    f.close()