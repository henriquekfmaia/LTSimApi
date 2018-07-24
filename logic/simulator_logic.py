import access_matlab.matlab_service as mls
import access_presentation_data.input_presentation_parser as ip
import access_presentation_data.output_presentation_data as op
import access_presentation_data.flow_logic as fl
import logic.relationship_logic as rl
import logic.process_logic as pl
import logic.comparer as co

def simulate(processes_dict, relationships_dict):
    relationships = rl.get_relationships_from_input(relationships_dict)
    processes = pl.get_processes_from_input(processes_dict, relationships)
    simulation_rounds = [[processes, relationships]]
    error = 10
    max_error = 1
    count = 0
    count_max = 500
    while(error > max_error):
        simulation_rounds.append(run_simulation_round(simulation_rounds[-1]))
        if(len(simulation_rounds) > 1):
            error = get_max_error(simulation_rounds[-2], simulation_rounds[-1])
        if(count > count_max):
            raise Exception('Convergence not reached after {0} cicles. Simulation aborted'.format(count_max))
        count = count + 1
    return simulation_rounds[-1]

def run_simulation_round(input_array):
    processes_in = input_array[0]
    relationships = input_array[1]
    processes_out = []

    for p in processes_in:
        process = pl.set_process_flows(p, relationships)
        simulation_result = simulate_process(process)
        set_simulation_result(process, simulation_result)
        processes_out.append(process)
        relationships = pl.set_outputs(process, relationships)

    output_array = [processes_out, relationships]
    return output_array

def simulate_process(process):
    model_input = ip.get_model_input(process)
    script = ip.get_model_script(process.model)
    ret = mls.run_generated_code(model_input, script)
    return ret

def set_simulation_result(process, simulation_result):
    flow_results = simulation_result[0]
    model_results = simulation_result[1]
    process.output = op.set_output_results(process.output, flow_results)
    op.set_model_results(process.model.results, model_results)

def get_max_error(before, after):
    errors = get_errors(before, after)
    return max(errors)

def get_errors(before, after):
    process_errors = compare_processes(before[0], after[0])
    relationship_errors = compare_relationships(before[1], after[1])
    errors = process_errors + relationship_errors
    return errors

def compare_processes(processes_before, processes_after):
    errors = []
    for i in range(0, len(processes_before)):
        for j in range(0, len(processes_before[i].input)):
            errors.append(fl.get_flow_errors(processes_before[i].input[j].flow, processes_after[i].input[j].flow))

        for j in range(0, len(processes_before[i].output)):
            errors.append(fl.get_flow_errors(processes_before[i].output[j].flow, processes_after[i].output[j].flow))

        for j in range(0, len(processes_before[i].model.results)):
            errors.append(compare_parameters(processes_before[i].model.results[j], processes_after[i].model.results[j]))

    return errors

def compare_relationships(relationships_before, relationships_after):
    errors = []
    for i in range(0, len(relationships_before)):
        errors.append(fl.get_flow_errors(relationships_before[i].flow, relationships_after[i].flow))

    return errors

def compare_parameters(paramA, paramB):
    if(paramA.type == 4):
        return co.get_errors_distribution(paramA, paramB)
    else:
        return co.get_errors_number(paramA.value, paramB.value)
