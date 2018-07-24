import access_database.sqlite_wrapper as sqlite_wrapper

query_select =    """
                SELECT
                    Id,
                    ModelId,
                    Name,
                    WaterFlowId,
                    MassFlowId,
                    DistributionId,
                    PositionX,
                    PositionY
                FROM TB_OUTPUT_FLOW
                """

query_insert =  """
                INSERT INTO TB_OUTPUT_FLOW
                (
                    ModelId,
                    Name,
                    WaterFlowId,
                    MassFlowId,
                    DistributionId,
                    PositionX,
                    PositionY
                )

                """

query_update =  """
                UPDATE TB_OUTPUT_FLOW SET

                """

def save_output_flow(output_flow, model, conn):
    if('id' in output_flow.__dict__ and output_flow.id > 0):
        return update_output_flow(output_flow, model, conn)
    else:
        return insert_output_flow(output_flow, model, conn)

def insert_output_flow(output_flow, model, conn):
    params = []
    query_values =  """
                    VALUES
                    (
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?
                    )
                    """
    query = query_insert + query_values
    params = [model.id, output_flow.name, output_flow.waterFlowId, output_flow.massFlowId, output_flow.distributionId, output_flow.positionX, output_flow.positionY]
    inserted_id = 0
    result = sqlite_wrapper.run_query(conn, query, params, True)
    inserted_id = result[1].lastrowid
    return inserted_id

def update_output_flow(output_flow, model, conn):
    params = []
    query_set = """
                    ModelId =?,
                    Name =?,
                    WaterFlowId =?,
                    MassFlowId =?,
                    DistributionFlowId =?,
                    PositionX =?,
                    PositionY =?

                WHERE
                     Id=?
                """

    query = query_update + query_set
    params = [model.id, output_flow.name, output_flow.waterFlowId, output_flow.massFlowId, output_flow.distributionId, output_flow.positionX, output_flow.positionY]
    for p in params:
        if (p == None):
            p = 'NULL'
    sqlite_wrapper.run_query(conn, query, params)
    return output_flow.id

def delete_output_flows_not_saved(output_flows_saved, model, conn):
    params = []
    query = """
            DELETE FROM TB_OUTPUT_FLOW
            WHERE Id NOT IN
            (
                {id}
            )
            AND ModelId =?
            """
    query = query.replace('{id}', sqlite_wrapper.get_params_by_size(len(output_flows_saved)))
    for p in output_flows_saved:
        params.append(p)
    params.append(model.id)
    sqlite_wrapper.run_query(conn, query, params)

class OutputFlow:
    def __init__(self, row):
        self.id = row[0]
        self.modelId = row[1]
        self.name = row[2]
        self.waterFlowId = row[3]
        self.massFlowId = row[4]
        self.distributionId = row[5]
        self.positionX = row[6]
        self.positionY = row[7]
