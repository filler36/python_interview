class DataBaseConnector:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBaseConnector.__instance = None

    def __init__(self, connection_string, username, password):
        self.connection_string = connection_string
        self.username = username
        self.password = password

    def connect(self):
        print(f'Connect to {self.connection_string}')

    def close(self):
        print('Close connection')

    def execute_query(self, sql_query):
        print(f'Execute query {sql_query}')

conn = DataBaseConnector('jdbc://example.com', 'John Doe', '******')
print(conn)
conn = DataBaseConnector('jdbc://another.example.com', 'Jane Doe', '******')
print((conn))
