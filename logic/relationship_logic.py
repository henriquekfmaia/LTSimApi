import access_matlab.matlab_service as mls
import access_presentation_data.flow_logic as fl
import classes.struct as s

def get_relationships_from_input(relationships_dict):
    relationships = s.get_structs(relationships_dict)
    relationships_to_feed = run_ciclor_relationships(relationships)
    relationships = feed_relationships(relationships, relationships_to_feed)
    return relationships

def run_ciclor_relationships(relationships):
    ciclor_input = []
    for rel in relationships:
        data = [rel.stageId, rel.sourceId, rel.destinationId, 0]
        ciclor_input.append(data)
    result = mls.run_ciclor(ciclor_input)
    return result

def feed_relationships(relationships, relationships_to_feed):
    for r in relationships_to_feed:
        rel = get_relationship_by_id(relationships, int(r))
        rel.flow = fl.restart_flow(rel.flow)
    return relationships

def get_known_relationships(relationships):
    out = []
    for r in relationships:
        if(fl.is_flow_known(r.flow)):
            out.append(r)
    return out

def get_relationship_by_id(relationship_list, stage_id):
    for r in relationship_list:
        if(r.stageId == stage_id):
            return r
    return None