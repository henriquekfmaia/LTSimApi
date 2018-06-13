import classes.struct as s
import matlab.engine

eng = matlab.engine.start_matlab()
def simulate(processes_dict, relationships_dict):
    processes = s.get_structs(processes_dict)
    relationships = s.get_structs(relationships_dict)
    # eng = matlab.engine.start_matlab()
    relationships_to_feed = run_ciclor_relationships(relationships, eng)
    for relationship in relationships:
        simulate_relationship(processes, relationship, eng)
    # eng.quit()
    return [processes, relationships]

def simulate_relationship(processes, relationship, eng):
    destinationProcess = get_process_by_id(relationship.destinationId, processes)
    destinationProcess = set_input_parameters(destinationProcess)
    destinationResults = simulate_process(destinationProcess, eng)
    
    SetResults(destinationProcess.model.results, destinationResults)
    return processes

def simulate_process(process, eng):
    parameter_list = []
    for parameter in process.model.parameters:
        parameter_list.append(get_parameter(parameter))
    generate_matlab_script(process.model)
    # if(len(parameter_list) == 1):
    #     parameter_list = [parameter_list]
    print(parameter_list)
    eng.test_code(parameter_list)
    matlab_ret = eng.temp_script(parameter_list)
    print(matlab_ret)
    ret = get_matlab_return(matlab_ret)
    return ret

def get_matlab_return(matlab_ret):
    if(type(matlab_ret) is list) or ('mlarray' in str(type(matlab_ret))):
        ret = []
        for item in matlab_ret:
            ret.append(get_matlab_return(item))
        if(len(ret) == 1):
            ret = ret[0]
        return ret
    else:
        return matlab_ret
    
def get_parameter(parameter):
    if(parameter.type == 4):
        array = parameter.value.array
        matlab_array = []
        for element in array:
            matlab_array.append(float(element.value))
        return matlab.double(matlab_array)
    elif(parameter.type == 5):
        return parameter.value
    else:
        return float(parameter.value)

def set_input_parameters(process):
    process.inputFlow = restart_flow(process.inputFlow)
    for i in process.input:
        process.inputFlow = add_flows(process.inputFlow, i.flow)
    # count = 0
    # for parameter in process.model.parameters:
    #     if(parameter.type == 5 and count < len(inputParameters)):
    #         parameter.value = inputParameters[count]
    #         count += 1
    return process

def restart_flow(flow):
    flow.waterFlow.value = 0
    flow.massFlow.value = 0
    for i in flow.sizeDistribution.value.array:
        i.value = 0
    return flow

def add_flows(flowA, flowB):
    flowA.waterFlow.value += flowB.waterFlow.value
    flowA.massFlow.value += flowB.massFlow.value
    for i in range(0, len(flowA.sizeDistribution.value.array)):
        flowA.sizeDistribution.value.array[i].value += flowB.sizeDistribution.value.array[i].value
    return flowA

def get_process_by_id(id, processes):
    for process in processes:
        if(process.stageId == id):
            return process

def SetResults(processResults, simulationResults):
    length = min(len(processResults), len(simulationResults))
    for i in range(0, length):
        if('type' in vars(processResults[i]) and processResults[i].type == 4):
            SetResults(processResults[i].value.array, simulationResults[i])
        else:
            processResults[i].value = simulationResults[i]


def generate_matlab_script(model):
    scriptHead = model.scriptHead
    scriptBody = model.scriptBody
    scriptTail = model.scriptTail
    script = scriptHead + scriptBody + scriptTail
    fileName = 'temp_script.m'
    f = open(fileName, 'w')
    f.write(script)
    f.close()
    return fileName

def run_ciclor_relationships(relationships, eng):
    ciclor_input = []
    ciclor_input.append([3, 0, 1, 1])
    for rel in relationships:
        data = [rel.stageId, rel.sourceId, rel.destinationId, 0]
        ciclor_input.append(data)
    ciclor_input.append([4, 0, 2, 1])
    ciclor_input.append([5, 3, 0, 1])
    ciclor_input.append([6, 3, 2, 1])
    ciclor_input = matlab.int32(ciclor_input)
    # eng.test_code(ciclor_input)
    result = eng.ciclor(ciclor_input)
    return result