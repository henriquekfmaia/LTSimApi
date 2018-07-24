import string
import random
import os
import matlab.engine

eng = matlab.engine.start_matlab()
temp_file_name = 'temp_script.m'

def generate_matlab_script_random_name(script):
    file_name = '{0}.m'.format(id_generator())
    f = open(file_name, 'w')
    f.write(script)
    f.close()
    return file_name

def generate_temp_matlab_script(script):
    file_name = temp_file_name
    f = open(file_name, 'w')
    f.write(script)
    f.close()
    return file_name

def delete_temp_file():
    fileName = temp_file_name
    if os.path.isfile(fileName):
        os.remove(fileName)

def delete_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)

def run_generated_code(matlab_input, script):
    file_name = generate_matlab_script_random_name(script)
    script_name = file_name.replace('.m', '')
    execute_code = 'eng.{0}(matlab_input)'.format(script_name)
    matlab_result = eval(execute_code)
    #matlab_result = eng.temp_script(matlab_input)
    delete_file(file_name)
    return matlab_result

def run_ciclor(matlab_input):
    matlab_result = eng.ciclor(matlab_input)
    return matlab_result

def run_test_code(matlab_input):
    matlab_result = eng.test_code(matlab_input)
    return matlab_result

def id_generator(size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    random_string = ''.join(random.choice(chars) for _ in range(size))
    return 'R' + random_string