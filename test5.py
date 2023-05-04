import psycopg2


try:
    # connect to exist database
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='lampa2004',
        database='database10'    
    )
    connection.autocommit = True
    
    # the cursor for perfoming database operations
    # cursor = connection.cursor()
    
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        
        print(f"Server version: {cursor.fetchone()}")
        
    # create a new table
    with connection.cursor() as cursor:
         cursor.execute(
             """CREATE TABLE some_data(
                 name varchar (50) NOT NULL,
                 surname varchar(50) NOT NULL,
                 tel varchar(50) NOT NULL);"""
         )
        
         # connection.commit()
         print("[INFO] Table created successfully")
        
    # insert data into a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO telephonespvrav (name, surname, tel) VALUES
    #         ('Robert', 'Mike', '1231');"""
    #     )
    #    
    #     print("[INFO] Data was succefully inserted")
        
    # get data from a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT name,surname,telephone FROM telephonespvrav;"""
    #     )
    #    
    #     print(cursor.fetchone())
        
    # delete a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE telephonespvrav;"""
    #     )
    #    
    #     print("[INFO] Table was deleted")
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")