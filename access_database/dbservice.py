import access_database.sqlite_wrapper as sqlite_wrapper
import classes.struct as s
import classes.process as process
import classes.process_type as process_type
import classes.model as model
import classes.parameter as parameter
import classes.result as result
import classes.output_flow as output_flow

database_file = 'ltsim_db.db'


def get_process_types():
    # create a database connection
    conn = sqlite_wrapper.create_connection(database_file)
    ret = process_type.get_process_types(conn)
    conn.close()
    return ret

def get_process_type_by_id(id):
    # create a database connection
    conn = sqlite_wrapper.create_connection(database_file)
    ret = process_type.get_process_type_by_id(id, conn)
    conn.close()
    return ret
            
def get_processes():
    # create a database connection
    conn = sqlite_wrapper.create_connection(database_file)
    ret = process.get_processes(conn)
    conn.close()
    return ret

def get_process_by_id_old(id):
    # create a database connection
    conn = sqlite_wrapper.create_connection(database_file)
    ret = process.get_process_by_id_old(id, conn)
    conn.close()
    return ret

def get_processes_by_type(type_id):
    # create a database connection
    conn = sqlite_wrapper.create_connection(database_file)
    ret = process.get_processes_by_type(type_id, conn)
    conn.close()
    return ret


def get_process_by_id(id):
    # create a database connection
    conn = sqlite_wrapper.create_connection(database_file)
    ret = process.get_process_by_id(id, conn)
    conn.close()
    return ret


def get_models_by_process_id(id):
    # create a database connection
    conn = sqlite_wrapper.create_connection(database_file)
    ret = model.get_models_by_process_id(id, conn)
    conn.close()
    return ret

def get_parameters_from_model(model_id):
    # create a database connection
    conn = sqlite_wrapper.create_connection(database_file)
    ret = parameter.get_parameters_from_model(model_id, conn)
    conn.close()
    return ret

def get_results_from_model(model_id):
    # create a database connection
    conn = sqlite_wrapper.create_connection(database_file)
    ret = result.get_results_from_model(model_id, conn)
    conn.close()
    return ret

def get_output_flow_from_model(model_id):
    # create a database connection
    conn = sqlite_wrapper.create_connection(database_file)
    ret = output_flow.get_output_flow_from_model(model_id, conn)
    conn.close()
    return ret

def save_model(m, processId):
    # create a database connection
    conn = sqlite_wrapper.create_connection(database_file)
    model_to_save = s.Struct(**m)
    model_to_save.id = model.save_model(model_to_save, processId, conn)
    parameters_saved = []
    for param in model_to_save.parameters:
        parameters_saved.append(parameter.save_parameter(s.Struct(**param), model_to_save, conn))
    parameter.delete_parameters_not_saved(parameters_saved, model_to_save, conn)

    results_saved = []
    for res in model_to_save.results:
        results_saved.append(result.save_result(s.Struct(**res), model_to_save, conn))
    result.delete_results_not_saved(results_saved, model_to_save, conn)
    conn.commit()
    conn.close()