import matlab.engine

def convert_to_matlab_mat(python_variable):
    matlab_array = []
    if(type(python_variable) is list):
        for v in python_variable:
            matlab_array.append(convert_to_matlab_mat(v))
    elif(type(python_variable) is int):
        return python_variable
    elif(type(python_variable) is float):
        return python_variable
    return matlab.double(matlab_array)

def convert_to_matlab_cells(python_variable):
    matlab_array = []
    if(type(python_variable) is list):
        for v in python_variable:
            matlab_array.append(convert_to_matlab_cells(v))
    elif(type(python_variable) is int):
        return python_variable
    elif(type(python_variable) is float):
        return python_variable
    return matlab_array
    

def force_list(matlab_variables):
    if(type(matlab_variables) is list):
        return matlab_variables
    else:
        return [matlab_variables]

def convert_to_python(matlab_variables):
    if(type(matlab_variables) is list) or ('mlarray' in str(type(matlab_variables))):
        ret = []
        for item in matlab_variables:
            ret.append(convert_to_python(item))
        if(len(ret) == 1):
            ret = ret[0]
        return ret
    else:
        return matlab_variables