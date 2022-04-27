import logging

cursor = -1
connection = -1


class DatabaseManager:
    """
    This class wraps MySql database methods for easy use
    """

    def __init__(self):
        logging.info('------ Connecting to DB -------')
        # You need to write the code that will create a connection to DB
        # self.connection = db2.connect(constants.DBConnect.SERVER)
        self.cursor = self.connection.cursor()
        logging.info('-----------Successfully Connected to DB----------')

    def query_fetch_all(self, query):
        """ Executes a DB query, gets all the values """
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def query_fetch_one(self, query):
        """ Executes a db query, gets first value """
        self.cursor.execute(query)
        record = self.cursor.fetchone()
        return record[0]

    def execute_query(self,query):
        """ Executes a query in the db """
        self.cursor.execute(query)

    def generate_dynamic_query(self, tableName, columnValueA, param):
        query = f'SELECT {param} FROM {tableName} WHERE RUN_ID = {columnValueA}'
        return query

    def close_db(self):
        """ Closed db connection """
        self.cursor.close()
        self.connection.close()
