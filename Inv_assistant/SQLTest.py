from  SQLite_Tool import *

def SQLite_DB_actions():
    DBFileName = r'C:\Stan\Stan_Workspace\My_Projects\Testing\SQLiteTest\SQLiteTest.db'

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
        delete_sql = '''delete from projects where id = 1
        '''
        values = ('stan','2020-10-10','2021-1-28')
        # print(run_DML3(conn, insert_sql,values))
        print(run_DML2(conn, delete_sql))


if __name__ == '__main__':
    SQLite_DB_actions()



