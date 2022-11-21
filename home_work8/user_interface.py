import view_result as vr
import logger as log
import db_tools as db
import db_reports as dbr
import os

def button_click():
    db_name = "students.db"
    table_name = "STUDENTS"
    marker = 1
    is_OK = True
    while is_OK:
        vr.view("Текущая база данных: ", db_name)
        marker = vr.input_data(
            " Press 1 - выбор базы данных \n press 2 - работа с базами данных \n press 3 - запросы \n press 4 -  выход\n: "
        )
        log.logger("User click", marker)

        match marker:
            case "1":
                for file in os.listdir():
                    if file.endswith(".db"):
                        print(os.path.join(" ", file))
                db_name = vr.input_data("Enter the filename: ")

            case "2":
                while is_OK:
                    vr.view("Текущая база данных: ", db_name)
                    vr.view("Текущая таблица в БД: ", table_name)
                    marker_db = vr.input_data(
                        " Press 1 - Создать таблицу \n press 2 - выбрать таблицу \n press 3 - посмотреть список таблиц в базе данных \n press 4 - добавить информацию \n press 5 - удалить информацию \n press 6 - создать новую базу данных \n press 7 - вернуться в предыдущее меню\n: "
                    )
                    match marker_db:
                        case "1":
                            table_name = db.create_table_db(db_name)
                            log.logger("User create table: ", table_name)
                        case "2":
                            table_name = db.select_table_in_bd(db_name)
                            log.logger("User select table: ", table_name)
                        case "3":
                            db.read_data(db_name, table_name)
                            log.logger("User watch: ", table_name)
                        case "4":
                            db.add_data_to_table(db_name, table_name)
                            log.logger("Create new name in", db_name)
                        case "5":
                            del_num = vr.input_data("Enter the id to delete: ")
                            db.delete_data(db_name, table_name, del_num)
                            log.logger(
                                f"Delete a record {del_num} from the database", db_name
                            )
                        case "6":
                            db_name = db.create_db()
                            log.logger("Create new db ", db_name)
                        case "7":
                            log.logger("Exit previous menu", "")
                            is_OK = False
                        case _:
                            print("Error")
                is_OK = True

            case "3":
                dbr.db_repotrs(db_name)

            case "4":
                log.logger("Programm close", "")
                is_OK = False
            case _:
                print("Error")