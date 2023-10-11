import psycopg2
    
def server_saver(city_name, request_time):
    db_params = {
        "host": "localhost",
        "database": "Weather",
        "user": "postgres",
        "password": "sq8151ze"
    }
    connection = psycopg2.connect(**db_params)
    cursor_ = connection.cursor()
    query = """INSERT INTO request ("city_name", "request_time") VALUES (%s, %s)"""
    data_to_insert = (city_name, request_time)
    cursor_.execute(query, data_to_insert)
    connection.commit()
    connection.close()
    
def client_saver(city_name, city_temp, feels_like, last_updat):
    db_params = {
        "host": "localhost",
        "database": "Weather",
        "user": "postgres",
        "password": "sq8151ze"
    }
    connection = psycopg2.connect(**db_params)
    cursor_ = connection.cursor()
    query = """INSERT INTO response ("city_name", "city_temp", "feels_like", "last_updat") VALUES (%s, %s, %s, %s)"""
    data_to_insert = (city_name, city_temp, feels_like, last_updat)
    cursor_.execute(query, data_to_insert)
    connection.commit()
    connection.close()