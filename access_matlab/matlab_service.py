import access_matlab.matlab_handler as mlh
import access_matlab.variable_parser as parser

def run_generated_code(parameter_list, script):
    matlab_input = parser.convert_to_matlab_cells(parameter_list)
    matlab_result = mlh.run_generated_code(matlab_input, script)
    result = parser.force_list(matlab_result)
    return result

def run_ciclor(parameter_list):
    matlab_input = parser.convert_to_matlab_mat(parameter_list)
    matlab_result = mlh.run_ciclor(matlab_input)
    result = parser.force_list(matlab_result)
    return result