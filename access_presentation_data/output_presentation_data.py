

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
    new_output = []
    for i in range(0, len(process_output)):
        flow = process_output[i]
        flow.waterFlow.value = simulation_result[i][0]
        flow.massFlow.value = simulation_result[i][1]
        flow.sizeDistribution.value = set_array_to_distribution(flow.sizeDistribution.value, simulation_result[i][2])
        new_output.append(flow)
    return new_output