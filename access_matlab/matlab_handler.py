import matlab.engine

eng = matlab.engine.start_matlab()

def generate_matlab_script(script):
    fileName = 'temp_script.m'
    f = open(fileName, 'w')
    f.write(script)
    f.close()
    return fileName

def run_generated_code(matlab_input, script):
    generate_matlab_script(script)
    matlab_result = eng.temp_script(matlab_input)
    return matlab_result

def run_ciclor(matlab_input):
    matlab_result = eng.ciclor(matlab_input)
    return matlab_result

def run_test_code(matlab_input):
    matlab_result = eng.test_code(matlab_input)
    return matlab_result