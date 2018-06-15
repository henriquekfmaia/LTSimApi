import access_matlab.matlab_service as mls
import access_presentation_data.input_presentation_parser as ip
import access_presentation_data.output_presentation_data as op
import access_presentation_data.flow_logic as fl
import relationship_logic as rl
import process_logic as pl

def simulate(processes_dict, relationships_dict):
    relationships = rl.get_relationships_from_input(relationships_dict)
    processes = pl.get_processes_from_input(processes_dict, relationships)
    simulation_rounds = [[processes, relationships]]
    while(True):
        simulation_rounds.append(run_simulation_round(simulation_rounds[-1]))
    
    return simulation_rounds[-1]

def run_simulation_round(input_array):
    processes_in = input_array[0]
    relationships = input_array[1]
    processes_out = []

    for p in processes_in:
        process = pl.set_process_flows(p, relationships)
        process = simulate_process(process)
        processes_out.append(process)
        # relationships = rl.set_outputs(process, relationships)

    output_array = [processes_out, relationships]

def simulate_process(process):
    model_input = ip.get_model_input(process)
    script = ip.get_model_script(process.model)
    ret = mls.run_generated_code(model_input, script)
    return ret

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

