import sqlite_wrapper

query_select =    """
                SELECT
                    Id,
                    Key,
                    Name,
                    Unit,
                    Type,
                    ModelId
                FROM TB_PARAMETER
                """

query_insert =  """
                INSERT INTO TB_PARAMETER
                (
                    Key,
                    Name,
                    Unit,
                    Type,
                    ModelId
                )

                """

query_update =  """
                UPDATE TB_PARAMETER SET

                """

def get_parameters_from_model(model_id, conn):
    parameters = []
    query_where =   """
                    WHERE
                        ModelId =?
                    """
    query = query_select + query_where
    param = [model_id]
    rows = sqlite_wrapper.run_query(conn, query, param)
    for row in rows:
        parameters.append(Parameter(row))
    return parameters

def save_parameter(parameter, model, conn):
    if('id' in parameter.__dict__ and parameter.id > 0):
        return update_parameter(parameter, model, conn)
    else:
        return insert_parameter(parameter, model, conn)

def insert_parameter(parameter, model, conn):
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
    params = [parameter.key, parameter.name, parameter.unit, parameter.type, model.id]
    inserted_id = 0
    result = sqlite_wrapper.run_query(conn, query, params, True)
    inserted_id = result[1].lastrowid
    return inserted_id


def update_parameter(parameter, model, conn):
    params = []
    query_set = """
                    Key =?,
                    Name =?,
                    Unit =?,
                    Type =?,
                    ModelId =?
                WHERE
                     Id=?
                """

    query = query_update + query_set
    params = [parameter.key, parameter.name, parameter.unit, parameter.type, model.id, parameter.id]
    for p in params:
        if (p == None):
            p = 'NULL'
    sqlite_wrapper.run_query(conn, query, params)
    return parameter.id

def delete_parameters_not_saved(parameters_saved, model, conn):
    params = []
    query = """
            DELETE FROM TB_PARAMETER
            WHERE Id NOT IN
            (
                {id}
            )
            AND ModelId =?
            """
    query = query.replace('{id}', sqlite_wrapper.get_params_by_size(len(parameters_saved)))
    for p in parameters_saved:
        params.append(p)
    params.append(model.id)
    sqlite_wrapper.run_query(conn, query, params)

class Parameter:
    def __init__(self, row):
        self.id = row[0]
        self.key = row[1]
        self.name = row[2]
        self.unit = row[3]
        self.type = row[4]
