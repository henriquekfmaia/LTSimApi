from flask import Flask, request, url_for
from flask_cors import CORS
import json
import access_database.dbservice as dbservice
import classes.struct as s
import logic.simulator_logic as sim

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World"

@app.route('/get_process_types', methods=['GET'])
def get_process_types():
    types = dbservice.get_process_types()
    json_response = []
    for t in types:
        processes = dbservice.get_processes_by_type(t.id)
        for p in processes:
            t.processes.append(p.__dict__)
        json_response.append(t.__dict__)

    ret = json.dumps(json_response)
    return ret

@app.route('/get_process_by_id/<id>', methods=['GET'])
def get_process_by_id(id):
    process = dbservice.get_process_by_id(id)
    models = dbservice.get_models_by_process_id(id)
    for m in models:
        parameters = dbservice.get_parameters_from_model(m.id)
        for par in parameters:
            m.parameters.append(par.__dict__)
        results = dbservice.get_results_from_model(m.id)
        for res in results:
            m.results.append(res.__dict__)
        output_flows = dbservice.get_output_flow_from_model(m.id)
        for flow in output_flows:
            m.output_flows.append(flow.__dict__)
        process.models.append(m.__dict__)
        
    ret = json.dumps(process.__dict__)
    return ret

@app.route('/post_model', methods=['POST'])
def post_model():
    req_data = request.get_json()
    model = req_data['model']
    processId = int(req_data['processId'])
    dbservice.save_model(model, processId)
    return json.dumps(req_data)

@app.route('/simulate', methods=['POST'])
def simulate():
    req_data = request.get_json()
    simulation_result = sim.simulate(req_data['processes'], req_data['relationships'])
    ret = {}
    ret['processes'] = simulation_result[0]
    ret['relationships'] = simulation_result[1]
    return json.dumps(ret)


app.run(debug=False, threaded=True)