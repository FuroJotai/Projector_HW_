import configparser

def get_database_connection_string():
    config = configparser.ConfigParser()
    config.read(r'C:\WellDee\Py\X\DB.ini')

    

    username = config['database']['username']
    password = config['database']['password']
    host = config['database']['host']
    port = config['database']['port']
    database = config['database']['database_name']

    return f'postgresql://{username}:{password}@{host}:{port}/{database}'


