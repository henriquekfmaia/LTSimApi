import access_matlab.matlab_handler as mlh
import access_matlab.variable_parser as parser
import json
import requests

url = 'http://localhost:5001'

def run_generated_code(parameter_list, script):
    return run_generated_code_local(parameter_list, script)

def run_ciclor(parameter_list):
    return run_ciclor_local(parameter_list)

def run_generated_code_service(parameter_list, script):
    route = '/run_generated_code'
    full_url = url + route
    data = {}
    data['parameter_list'] = parameter_list
    data['script'] = script
    response = requests.post(full_url, json=data)
    result = json.loads(response.text)
    return result

def run_ciclor_service(parameter_list):
    route = '/run_ciclor'
    full_url = url + route
    data = {}
    data['parameter_list'] = parameter_list
    response = requests.post(full_url, json=data)
    result = json.loads(response.text)
    return result

def run_generated_code_local(parameter_list, script):
    matlab_input = parser.convert_to_matlab_cells(parameter_list)
    matlab_result = mlh.run_generated_code(matlab_input, script)
    result = parser.force_list(matlab_result)
    return result

def run_ciclor_local(parameter_list):
    matlab_input = parser.convert_to_matlab_mat(parameter_list)
    matlab_result = mlh.run_ciclor(matlab_input)
    result = parser.force_list(matlab_result)
    return result