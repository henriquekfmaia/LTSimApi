import logic.relationship_logic as rl
import access_presentation_data.flow_logic as fl
import classes.struct as s

def get_processes_from_input(processes_dict, relationships=None):
    processes = s.get_structs(processes_dict)
    if(relationships != None):
        processes = sort_proceesses(processes, relationships)
    return processes

def sort_proceesses(processes, relationships):
    processes_out = []
    known_relationships = rl.get_known_relationships(relationships)
    known_rel_ids = [r.stageId for r in known_relationships]
    while(len(processes_out) < len(processes)):
        for process in processes:
            if(has_valid_input(process, known_rel_ids) and get_process_by_id(processes_out, process.stageId) == None):
                processes_out.append(process)

    return processes_out

def get_process_by_id(process_list, stage_id):
    for p in process_list:
        if(p.stageId == stage_id):
            return p
    return None

def has_valid_input(process, known_rel_ids):
    for i in process.input:
        if(i.stageId not in known_rel_ids):
            return False
    return True

def set_process_flows(process, relationships):
    process.inputFlow = fl.restart_flow(process.inputFlow)
    for i in range(0, len(process.input)):
        process.input[i] = rl.get_relationship_by_id(relationships, process.input[i].stageId)
        process.inputFlow = fl.add_flows(process.inputFlow, process.input[i].flow)
    return process
    
def set_outputs(process, relationships):
    for rel in process.output:
        relationship_to_update = rl.get_relationship_by_id(relationships, rel.stageId)
        relationship_to_update.flow = rel.flow
    return relationships