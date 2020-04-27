if __name__ == "__main__":
    pass


class Users:
    def __init__(self, first_name, last_name, username, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__email = email
        self.__password = password
    
    def show_user_info(self):
        print("first name: ", self.__first_name,"\nlast name: ", self.__last_name,"\nUsername: ", self.__username,"\npassword: *****")

    def save_user(self):
        f = open('db.txt', 'a')
        f.write(self.__first_name + "#" + self.__last_name + "#" + self.__username + "#" + self.__email + "#" + self.__password + "#\n")
        f.close()
    def show_all_users(self):
        users = []
        with open('db.txt') as db_file:
            for line in db_file:
                if len(line.strip())>0: #ігнорим пусті строки
                    item = line.strip()
                    items = item.split("#")
                    users.append(items)
        return users


    def register(self):
        all_users = self.show_all_users()
        user = self.__dict__.values()
        for item in all_users:
            if item[2] == self.__username:
                print("Username " + item[2] + " is registered")
                return
        with open('db.txt', 'a') as db_file:
            db_file.write("#".join(user)+"\n")
    
    
    def log(self, login, password):
        all_users = self.show_all_users()
        for item in all_users:
            if item[2] == login:
                return item[4] == password
        return False

    def delet(self, log):
        all_users = self.show_all_users()
        deleted = False
        with open('db.txt', 'w') as db_file:
            for item in all_users:
                if item[2] != log:
                    db_file.write("#".join(item)+"\n")
                else:
                    deleted = True
        return deleted


        