import mysql.connector
if __name__ == "__main__":
    db_manager


class db_manager:

    def __init__(self, host, user, passwd):
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )
        self.__cursor = self.__db.cursor()
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS pythonlogin")
        self.__cursor.execute("USE pythonlogin")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")

    def menu(self):
        exit = False
        while not exit:
            choice = int(input(
                "1. Register\n2. Login\n3. Edit\n4. Delete\n5. Show all users\n6. Search by username\n7. Search by email\n0. Exit\n====>> "))
            if choice == 1:
                answer = self.__register()
                print(answer)
            elif choice == 2:
                answer = self.__login()
                print(answer)
            elif choice == 3:
                answer = self.__edit()
                print(answer)
            elif choice == 4:
                answer = self.__delete()
                print(answer)
            elif choice == 5:
                answer = self.__show()
                print(answer)
            elif choice == 6:
                answer = self.__showUsername()
                print(answer)
            elif choice == 7:
                answer = self.__showEmail()
                print(answer)
            elif choice == 0:
                exit = True
                print("Bye!")
            else:
                print("Wrong choise")

    def __register(self):
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        re_password = input("Retype password: ")

        if password != re_password:
            return "Password dont match"

        self.__cursor.execute(
            "SELECT * FROM users WHERE username='" + username + "'")
        result = self.__cursor.fetchone()
        if result != None:
            return "User exists"
        else:
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s,%s)"
            val = (username, email, password)
            self.__cursor.execute(sql, val)
            self.__db.commit()
            return "User created"

    def __delete(self):
        username = input("Enter username: ")
        self.__cursor.execute(
            "SELECT * FROM users WHERE username='" + username + "'")
        result = self.__cursor.fetchone()
        print(result)
        if result == None:
            return "User none"
        else:
            sql = "DELETE FROM `users` WHERE username='" + username + "'"
            self.__cursor.execute(sql)
            self.__db.commit()
            return "User deleted"

    def __login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.__cursor.execute(
            "SELECT * FROM users WHERE username='" + username + "'")
        result = self.__cursor.fetchone()
        if result == None:
            return "User none"
        elif result[1] != username:
            return "Wrong login"
        elif result[3] != password:
            return "Wrong password"
        else:
            return "Login completed"

    def __edit(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.__cursor.execute(
            "SELECT * FROM users WHERE username='" + username + "'")
        result = self.__cursor.fetchone()
        if result == None:
            return "User none"
        elif result[1] != username:
            return "Wrong login"
        elif result[3] != password:
            return "Wrong password"
        else:
            exitEdit = False
            while not exitEdit:
                menuEdit = int(
                    input("1. username\n2. email\n3. password\n0. Exit\n====>> "))
                if menuEdit == 1:
                    usernameEdit = input("Enter username: ")
                    sql = "UPDATE users SET `username`='" + usernameEdit + "'"
                    self.__cursor.execute(sql)
                    self.__db.commit()
                elif menuEdit == 2:
                    emailEdit = input("Enter username: ")
                    sql = "UPDATE users SET `email`='" + emailEdit + "'"
                    self.__cursor.execute(sql)
                    self.__db.commit()
                elif menuEdit == 3:
                    passwordEdit = input("Enter username: ")
                    sql = "UPDATE users SET `password`='" + passwordEdit + "'"
                    self.__cursor.execute(sql)
                    self.__db.commit()
                elif menuEdit == 0:
                    exitEdit = True
                    print("Bye!")

    def __show(self):
        self.__cursor.execute("SELECT username, email FROM users")
        result = self.__cursor.fetchone()
        print(result)
        return"Users show"

    def __showUsername(self):
        usernameShow = input("Enter username: ")
        self.__cursor.execute(
            "SELECT username, email FROM users WHERE username ='"+usernameShow+"'")
        result = self.__cursor.fetchone()
        print(result)
        return"User show"

    def __showEmail(self):
        EmailShow = input("Enter username: ")
        self.__cursor.execute("SELECT username, email FROM users WHERE email ='"+EmailShow+"'")
        result = self.__cursor.fetchone()
        print(result)
        return"User show"
