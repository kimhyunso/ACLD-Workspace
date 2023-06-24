import mariadb
import sys

class DataBase:
    def __init__(self, user_name, user_pwd, HOST, PORT, db_name):
        try:
            self.__conn = mariadb.connect(
                user=user_name,
                password=user_pwd,
                host=HOST,
                port=PORT,
                database=db_name
            )
        except Exception as e:
            print(f'Connection Error : {e}')
            sys.exit(1)

    def update_identify(self, IP, MAC, emp_no):
        sql = "UPDATE identify SET IP=?, MAC=? WHERE emp_no = ?"
        try:
            cursor = self.get_cursor()
            cursor.execute(sql,
                (IP, MAC, emp_no)
            )
        except Exception as e:
            print(f"Select Error : {e}")
            sys.exit(1)


    def select_identify(self, emp_no):
        sql = "SELECT agent_no FROM identify WHERE emp_no = ?"
        try:
            cursor = self.get_cursor()
            cursor.execute(sql,
                (emp_no, )
            )
            result = cursor.fetchone()
            return result[0]

        except Exception as e:
            print(f"Select Error : {e}")
            sys.exit(1)

    def update_agent(self, status, agent_no):
        sql = "UPDATE agent SET status=? WHERE agent_no=?"
        try:
            cursor = self.get_cursor()
            cursor.execute(sql,
                (status, agent_no)
            )
            self.get_connection().commit()
        except Exception as e:
            print(f"Update Error : {e}")
            sys.exit(1)

    def insert_dection(self, emp_no, cam_path, screen_path):
        sql = "INSERT INTO dection(emp_no, CAM_path, screen_path) VALUES(?, ?, ?)"
        try:
            cursor = self.get_cursor()
            cursor.execute(sql,
                (emp_no, cam_path, screen_path)
            )
            self.get_connection().commit()
        except Exception as e:
            print(f"Insert Error : {e}")
            sys.exit(1)

    def get_cursor(self):
        try:
            cur = self.get_connection().cursor()
        except Exception as e:
            print(f'get cursor Error : {e}')
        return cur

    def close(self):
        self.get_cursor().close()
        self.get_connection().close()


    def get_connection(self):
        return self.__conn