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
    elif(type(python_variable) is str):
        try:
            return float(python_variable)
        except:
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
    elif(type(python_variable) is str):
        try:
            return float(python_variable)
        except:
            return python_variable
    return matlab_array
    
def convert_to_matlab(python_variable):
    matlab_array = []
    if(type(python_variable) is list):
        for v in python_variable:
            matlab_array.append(convert_to_matlab(v))
        if all(((type(v) is int or type(v) is float) and v is not list) for v in python_variable):
            return matlab.double(matlab_array)

    elif(type(python_variable) is int):
        return python_variable
    elif(type(python_variable) is float):
        return python_variable
    elif(type(python_variable) is str):
        try:
            return float(python_variable)
        except:
            return python_variable

    return matlab_array

def force_list(matlab_variables):
    t = type(matlab_variables)
    if(t is list):
        return matlab_variables
    elif(t is matlab.double):
      return []
    else:
        return [matlab_variables]

def convert_to_python(matlab_variables):
    if(type(matlab_variables) is list) or ('mlarray' in str(type(matlab_variables))):
        ret = []
        for item in matlab_variables:
            ret.append(convert_to_python(item))
        #if(len(ret) == 1):
            #ret = ret[0]
        return ret
    else:
        return matlab_variables