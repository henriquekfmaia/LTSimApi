import sqlite_wrapper

query_select =    """
                SELECT
                    Id,
                    Name,
                    ProcessId,
                    ScriptHead,
                    ScriptBody,
                    ScriptTail
                FROM TB_MODEL
                """

query_insert =  """
                INSERT INTO TB_MODEL
                (
                    Name,
                    ProcessId,
                    ScriptHead,
                    ScriptBody,
                    ScriptTail
                )

                """

query_update =  """
                UPDATE TB_MODEL SET

                """

def get_models_by_process_id(id, conn):
    models = []
    query_where =   """
                    WHERE ProcessId =?
                    """
    query = query_select + query_where
    param = [id]
    rows = sqlite_wrapper.run_query(conn, query, param)
    for row in rows:
        models.append(Model(row))
    
    return models

def save_model(model, processId, conn):
    if('id' in model.__dict__ and model.id > 0):
        return update_model(model, conn)
    else:
        return insert_model(model, processId, conn)

def insert_model(model, processId, conn):
    params = []
    query_values =  """
                    VALUES
                    (
                        ?,
                        ?,
                        ?,
                        ?,
                        ?
                    )
                    """
    query = query_insert + query_values
    params = [model.name, processId, model.scriptHead, model.scriptBody, model.scriptTail]
    result = sqlite_wrapper.run_query(conn, query, params, True)
    inserted_id = result[1].lastrowid
    return inserted_id

def update_model(model, conn):
    params = []
    query_set = """
                    Name =?,
                    ScriptHead =?,
                    ScriptBody =?,
                    ScriptTail =?
                WHERE
                     Id=?
                """

    query = query_update + query_set
    params = [model.name, model.scriptHead, model.scriptBody, model.scriptTail, model.id]
    for p in params:
        if (p == None):
            p = 'NULL'
    sqlite_wrapper.run_query(conn, query, params)
    return model.id

class Model:
    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.processId = row[2]
        self.scriptHead = row[3]
        self.scriptBody = row[4]
        self.scriptTail = row[5]
        self.parameters = []
        self.results = []
        self.output_flows = []
