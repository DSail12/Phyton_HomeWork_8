import view_result as vr
import sqlite3 as sl


def create_db():
    db_name = vr.input_data("Input name of new database (example: 'new.db'): ")
    con = sl.connect(db_name)
    return db_name


def create_table_db(name_db):
    table_name = vr.input_data("Input name table in database: ").upper()

    db_col_list = []
    is_OK = True
    while is_OK:
        marker = vr.input_data(" press 1 - добавить столбец \n press 2 - создать таблицу\n: ")
        match marker:
            case "1":
                db_col_list.append(
                    vr.input_data(
                        "Input 'name' and 'data type' (example: 'NAME TEXT'): "
                    )
                )
            case "2":
                is_OK = False
            case _:
                print("Error")

    db_col = (
        "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT," + ",".join(db_col_list).upper()
    )

    con = sl.connect(name_db)
    with con:
        con.execute(f""" CREATE TABLE IF NOT EXISTS {table_name} ({db_col});""")

    return table_name


def select_table_in_bd(name_db):
    con = sl.connect(name_db)
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())
    table_name = vr.input_data("Input name of table in database: ").upper()
    return table_name


def add_data_to_table(db_name, table_name):
    list_col_name = get_col_names(db_name, table_name)
    list_col_name.remove("id")
    list_values = []
    for i in range(len(list_col_name)):
        list_values.append((vr.input_data(f"Input col {list_col_name[i]}: ")).upper())
    list_values = create_string(list_values)
    str_col_name = create_string(list_col_name)
    with sl.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO {table_name} ({str_col_name}) values({list_values})")
        con.commit()


def read_data(db_name, table_name):
    print(get_col_names("students.db", table_name))
    con = sl.connect(db_name)
    with con:
        data = con.execute(f"SELECT * FROM {table_name} ")
        for row in data:
            print(f"{row}")


def delete_data(db_name, table_name, del_num):

    con = sl.connect(db_name)
    con.execute(f"DELETE FROM {table_name} WHERE id={del_num};")
    con.commit()


def get_col_names(db_name, table_name):
    conn = sl.connect(db_name)
    c = conn.cursor()
    c.execute(f"select * from {table_name}")
    return [member[0] for member in c.description]


def create_string(input_list):
    output_string = ""
    for i in range(len(input_list)):
        output_string += "'" + str(input_list[i]) + "'"
        if i < len(input_list) - 1:
            output_string += ","
    return output_string


def print_str_db(name_db, input_str):
    con = sl.connect(name_db)
    cur = con.cursor()
    cur.execute("{}".format(input_str))
    for i in cur:
        print(i)