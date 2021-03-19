from  SQLite_Tool import *
from Para import *

def SQLite_DB_actions():
    

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    sqlQuery = """ select * from projects """
    # create a database connection
    conn = create_connection(DBFileName)
    # create tables
    if conn is not None:
        # create projects table
        create_table(conn,sql_create_projects_table)
        # create tasks table
        create_table(conn, sql_create_tasks_table)

        run_query(conn,sqlQuery)

        conn.close()
    else:
        print("Error! cannot create the database connection.")

    conn = create_connection(DBFileName)
    with conn:
        insert_sql = ''' INSERT INTO projects
        (name, begin_date, end_date)
        VALUES(?,?,?)'''
        values = ('stan','2020-10-10','2021-1-28')
        print(run_insert(conn, insert_sql,values))

if __name__ == '__main__':
    SQLite_DB_actions()



