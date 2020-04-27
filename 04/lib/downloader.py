from subprocess import call
import os
if __name__ == "__main__":
    pass

class downloader():
    def menu(self):
        choice = int(input("1. Download Movie\n 2. Download playlist (Movie)\n3. Exit\n====>>>"))
        return choice

    def download_single_mowie(self):
        movie_url = input("Enter mouve url =>")
        movie_info = "youtube-dl " + movie_url +" -F"
        call(movie_info, shell=False)
        format = input("enter Format code:")
        os.chdir('down')
        download_command = "youtube-dl -f " + format + " " + movie_url + " -c"
        call(download_command, shell=False)
        
        