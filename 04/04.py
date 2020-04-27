from lib.downloader import downloader

media_file = downloader()

exit = False
while not exit:
    choice = media_file.menu()
    if choice == 1:
        # print("user choise =>", choice)
        media_file.download_single_mowie()
    elif choice == 2:
        print("Enter mouve url =>", choice)
    elif choice == 0:
        exit = True
        print("Bye!")
    else:
        print("R.T.F.M")
