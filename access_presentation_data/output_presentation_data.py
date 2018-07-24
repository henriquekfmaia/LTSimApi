

def set_model_results(process_results, simulation_result):
    for i in range(0, len(process_results)):
        if(type(simulation_result[i]) is list):
            process_results[i].value = set_array_to_distribution(process_results[i].value, simulation_result[i])
        else:
            process_results[i].value = simulation_result[i]


def set_array_to_distribution(distribution, array):
    for i in range(0, len(distribution.array)):
        size = distribution.array[i]
        size.value = array[i]
    return distribution

def set_output_results(process_output, simulation_result):
    for i in range(0, len(process_output)):
        flow = process_output[i].flow
        flow.waterFlow.value = simulation_result[i][0]
        flow.massFlow.value = simulation_result[i][1]
        flow.sizeDistribution.value = set_array_to_distribution(flow.sizeDistribution.value, simulation_result[i][2])
    return process_output

def process_array_to_serializable(process_array):
    new_array = []
    for p in process_array:
        new_array.append(process_to_serializable(p))
    return new_array

def process_to_serializable(process):
    if(isinstance(process, dict)):
        return process
    process.model = model_to_serializable(process.model)
    process.models = model_array_to_serializable(process.models)
    process.input = relationship_array_to_serializable(process.input)
    process.inputFlow = flow_to_serializable(process.inputFlow)
    process.output = relationship_array_to_serializable(process.output)

    return get_dict(process)

def model_array_to_serializable(model_array):
    new_array = []
    for m in model_array:
        new_array.append(model_to_serializable(m))

    return new_array

def model_to_serializable(model):
    if(isinstance(model, dict)):
        return model
    model.results = parameter_array_to_serializable(model.results)
    model.parameters = parameter_array_to_serializable(model.parameters)
    return get_dict(model)

def parameter_array_to_serializable(parameter_array):
    new_array = []
    for p in parameter_array:
        new_array.append(parameter_to_serializable(p))

    return new_array

def parameter_to_serializable(parameter):
    if(isinstance(parameter, dict)):
        return parameter
    if(parameter.type == 4):
        return distribution_to_serializable(parameter)
    else:
        return get_dict(parameter)

def relationship_array_to_serializable(relationship_array):
    new_array = []
    for r in relationship_array:
        new_array.append(relationship_to_serializable(r))
    return new_array

def relationship_to_serializable(relationship):
    if(isinstance(relationship, dict)):
        return relationship
    relationship.flow = flow_to_serializable(relationship.flow)
    return get_dict(relationship)

def flow_to_serializable(flow):
    if(isinstance(flow, dict)):
        return flow
    flow.waterFlow = get_dict(flow.waterFlow)
    flow.massFlow = get_dict(flow.massFlow)
    flow.sizeDistribution = distribution_to_serializable(flow.sizeDistribution)
    return get_dict(flow)

def distribution_to_serializable(distribtion):
    if(isinstance(distribtion, dict)):
        return distribtion
    for i in range(0, len(distribtion.value.array)):
        distribtion.value.array[i] = get_dict(distribtion.value.array[i])
    distribtion.value = get_dict(distribtion.value)
    return get_dict(distribtion)

def get_dict(obj):
    if(isinstance(obj, dict)):
        return obj
    else:
        return obj.__dict__