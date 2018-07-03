import access_matlab.matlab_service as mls
import access_presentation_data.input_presentation_parser as ip
import access_presentation_data.output_presentation_data as op
import access_presentation_data.flow_logic as fl
import logic.relationship_logic as rl
import logic.process_logic as pl

def simulate(processes_dict, relationships_dict):
    relationships = rl.get_relationships_from_input(relationships_dict)
    processes = pl.get_processes_from_input(processes_dict, relationships)
    simulation_rounds = [[processes, relationships]]
    boolean = True
    while(True):
        simulation_rounds.append(run_simulation_round(simulation_rounds[-1]))
        boolean = False
    
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
    op.set_output_results(process.output, flow_results)
    op.set_model_results(process.model.results, model_results)