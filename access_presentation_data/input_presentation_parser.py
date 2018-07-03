


def get_model_input(process):
    input_flow = get_flow(process.inputFlow)
    process_parameters = get_parameters(process.model.parameters)
    model_input = [input_flow, process_parameters]
    return model_input

def get_flow(flow):
    flow_array = [ flow.waterFlow.value, flow.massFlow.value, get_distribution(flow.sizeDistribution) ]
    return flow_array

def get_parameters(parameters):
    return_parameters = []
    for p in parameters:
        if(p.type == 4):
            return_parameters.append(get_distribution(p))
        else:
            return_parameters.append(p.value)
    return return_parameters    

def get_distribution(distribution_parameter):
    distribution = []
    for i in distribution_parameter.value.array:
        distribution.append(i.value)
    return distribution

def get_model_script(model):
    script = model.scriptHead + model.scriptBody + model.scriptTail
    return script