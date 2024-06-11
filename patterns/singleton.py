class DatabaseConnector:
    __instance = None
    __initialized = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DatabaseConnector.__instance = None

    def __init__(self, connection_string, username, password):
        if not DatabaseConnector.__initialized:
            self.connection_string = connection_string
            self.username = username
            self.password = password
            DatabaseConnector.__initialized = True

    def __repr__(self):
        return f'DataBaseConnector(connection_string={self.connection_string}, username={self.username}, password={self.password})'

    def connect(self):
        print(f'Connect to {self.connection_string}')

    def close(self):
        print('Close connection')

    def execute_query(self, sql_query):
        print(f'Execute query {sql_query}')

conn = DatabaseConnector('jdbc://example.com', 'John Doe', '******')
print(conn)  # DataBaseConnector(connection_string=jdbc://example.com, username=John Doe, password=******)
conn = DatabaseConnector('jdbc://another.example.com', 'Jane Doe', '******')
print((conn))  # DataBaseConnector(connection_string=jdbc://example.com, username=John Doe, password=******)
