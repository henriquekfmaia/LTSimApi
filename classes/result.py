import sqlite_wrapper

query_select =    """
                SELECT
                    Id,
                    Key,
                    Name,
                    Unit,
                    Type,
                    ModelId
                FROM TB_RESULT
                """

query_insert =  """
                INSERT INTO TB_RESULT
                (
                    Key,
                    Name,
                    Unit,
                    Type,
                    ModelId
                )

                """

query_update =  """
                UPDATE TB_RESULT SET

                """

def get_results_from_model(model_id, conn):
    results = []
    query_where =   """
                    WHERE
                        ModelId =?
                    """
    query = query_select + query_where
    param = [model_id]
    rows = sqlite_wrapper.run_query(conn, query, param)
    for row in rows:
        results.append(Result(row))
    return results

def save_result(result, model, conn):
    if('id' in result.__dict__ and result.id > 0):
        return update_result(result, model, conn)
    else:
        return insert_result(result, model, conn)

def insert_result(result, model, conn):
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
    params = [result.key, result.name, result.unit, result.type, model.id]
    inserted_id = 0
    result = sqlite_wrapper.run_query(conn, query, params, True)
    inserted_id = result[1].lastrowid
    return inserted_id


def update_result(result, model, conn):
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
    params = [result.key, result.name, result.unit, result.type, model.id, result.id]
    for p in params:
        if (p == None):
            p = 'NULL'
    sqlite_wrapper.run_query(conn, query, params)
    return result.id

def delete_results_not_saved(results_saved, model, conn):
    params = []
    query = """
            DELETE FROM TB_RESULT
            WHERE Id NOT IN
            (
                {id}
            )
            AND ModelId =?
            """
    query = query.replace('{id}', sqlite_wrapper.get_params_by_size(len(results_saved)))
    for p in results_saved:
        params.append(p)
    params.append(model.id)
    sqlite_wrapper.run_query(conn, query, params)

class Result:
    def __init__(self, row):
        self.id = row[0]
        self.key = row[1]
        self.name = row[2]
        self.unit = row[3]
        self.type = row[4]
