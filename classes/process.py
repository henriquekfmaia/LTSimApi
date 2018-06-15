import access_database.sqlite_wrapper as sqlite_wrapper

query_select =    """
                SELECT
                    Id,
                    Name,
                    ProcessType,
                    ImagePath,
                    InputLimit,
                    OutputLimit,
                    Image
                FROM TB_PROCESS
                """


def get_processes(conn):
    processes = []
    rows = sqlite_wrapper.run_query(conn, query_select)
    for row in rows:
        processes.append(Process(row))
    return processes

def get_processes_by_type(type_id, conn):
    processes = []
    query_where =   """
                    WHERE ProcessType =?
                    """
    query = query_select + query_where
    param = [type_id]
    rows = sqlite_wrapper.run_query(conn, query, param)
    for row in rows:
        processes.append(Process(row))
    return processes

def get_process_by_id(id, conn):
    query_where =   """
                    WHERE Id =?
                    """
    query = query_select + query_where
    param = [id]
    rows = sqlite_wrapper.run_query(conn, query, param)
    if(len(rows) == 0):
        return '-1'
    for row in rows:
        pass
    ret_process = Process(row)
    return ret_process

def get_process_by_id_old(id, conn):
    processes = []
    query_where =   """
                    WHERE Id =?
                    """
    query = query_select + query_where
    param = [id]
    rows = sqlite_wrapper.run_query(conn, query, param)
    for row in rows:
        processes.append(Process(row))
    return processes

class Process:
    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.processTypeId = row[2]
        self.imagePath = row[3]
        self.inputLimit = row[4]
        self.outputLimit = row[5]
        self.models = []
        # self.imageHex = row[4].hex()
