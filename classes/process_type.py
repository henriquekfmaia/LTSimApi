import access_database.sqlite_wrapper as sqlite_wrapper

query_select = """
        SELECT  ID,
                NAME
        FROM TB_PROCESS_TYPES
        """

def get_process_types(conn):
    types = []
    rows = sqlite_wrapper.run_query(conn, query_select)
    for row in rows:
        types.append(ProcessType(row))
    return types

def get_process_type_by_id(id, conn):
    types = []
    query_where =   """
                    WHERE Id =?
                    """
    query = query_select + query_where
    param = [id]
    rows = sqlite_wrapper.run_query(conn, query, param)
    for row in rows:
        types.append(ProcessType(row))
    return types

class ProcessType:
    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.processes = []