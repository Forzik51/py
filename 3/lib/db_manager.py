import mysql.connector
import requests
from lib.settings import URL
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
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS COVID19")
        self.__cursor.execute("USE COVID19")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS Global (id INT AUTO_INCREMENT PRIMARY KEY, NewConfirmed INT(10), TotalConfirmed INT(10), NewDeaths INT(10), TotalDeaths INT(10), NewRecovered INT(10), TotalRecovered INT(10))")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS Countries (id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255), CountryCode VARCHAR(20), Slug VARCHAR(255), NewConfirmed INT(10), TotalConfirmed INT(10), NewDeaths INT(10), TotalDeaths INT(10), NewRecovered INT(10), TotalRecovered INT(10), Date DATE)")

    def menu(self):
        exit = False
        while not exit:
            choice = int(input(
                "1. Update data\n2. about Country\n3. Country code\n0. Exit\n====>> "))
            if choice == 1:
                answer = self.__update_covid_data()
                print(answer)
            elif choice == 2:
                answer = self.__Country()
                print(answer)
            elif choice == 3:
                answer = self.__Country_code()
                print(answer)
            elif choice == 0:
                exit = True
                print("Bye!")
            else:
                print("Wrong choise")

    def __update_covid_data(self):
        sql = "DELETE FROM `Countries` "
        self.__cursor.execute(sql)
        self.__db.commit()
        sql = "DELETE FROM `Global` "
        self.__cursor.execute(sql)
        self.__db.commit()

        covid_data = requests.get(URL)
        covid_data = covid_data.json()
        print(covid_data['Global']["NewConfirmed"], " ",
              covid_data['Global']["TotalConfirmed"], " ", covid_data['Global']["NewDeaths"], " ", covid_data['Global']["TotalDeaths"], " ", covid_data['Global']["NewRecovered"], " ", covid_data['Global']["TotalRecovered"])

        sql = "INSERT INTO Global (NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered) VALUES (%s, %s,%s, %s,%s, %s)"
        val = (covid_data['Global']["NewConfirmed"], covid_data['Global']["TotalConfirmed"], covid_data['Global']["NewDeaths"],
               covid_data['Global']["TotalDeaths"], covid_data['Global']["NewRecovered"], covid_data['Global']["TotalRecovered"])
        self.__cursor.execute(sql, val)
        self.__db.commit()

        for item in covid_data['Countries']:
            print(item['Country'], " ", item['CountryCode'], " ", item['Slug'], " ", item['NewConfirmed'], " ", item['TotalConfirmed'],
                  " ", item['NewDeaths'], " ", item['TotalDeaths'], " ", item['NewRecovered'], " ", item['TotalRecovered'], " ", item['Date'])

            sql = "INSERT INTO Countries (Country, CountryCode, Slug,NewConfirmed,TotalConfirmed,NewDeaths,TotalDeaths,NewRecovered,TotalRecovered,Date) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
            val = (item['Country'], item['CountryCode'], item['Slug'], item['NewConfirmed'], item['TotalConfirmed'],
                   item['NewDeaths'], item['TotalDeaths'], item['NewRecovered'], item['TotalRecovered'], item['Date'])
            self.__cursor.execute(sql, val)
            self.__db.commit()
        # print(covid_data['Countries'][0])
        return "Update covid database"

    def __Country(self):
        country = input("Enter country: ")
        self.__cursor.execute("SELECT `Country`,' нові випадки:', `NewConfirmed`,' кількість випадків:', `TotalConfirmed`,' нові смерті:', `NewDeaths`,' кількість смертей:', `TotalDeaths`,' нові одужання:', `NewRecovered`,' кількість одужаних:', `TotalRecovered`,' дата:', `Date` FROM Countries WHERE country ='" + country + "'")
        result = self.__cursor.fetchone()
        print(result)
        return"country show"

    def __Country_code(self):
        country = input("Enter country code: ")
        self.__cursor.execute("SELECT `Country`,' нові випадки:', `NewConfirmed`,' кількість випадків:', `TotalConfirmed`,' нові смерті:', `NewDeaths`,' кількість смертей:', `TotalDeaths`,' нові одужання:', `NewRecovered`,' кількість одужаних:', `TotalRecovered`,' дата:', `Date` FROM Countries WHERE CountryCode ='" + country + "'")
        result = self.__cursor.fetchone()
        print(result)
        return"country show"
