from lib.person import Users

user = Users("John", "Snow", "j_snow", "js@gmail.com", "john's_secret")
# user.show_user_info()
# user.save_user()
user.show_all_users()
user.register()
user.log("j_snow", "john's_secre")
res_delt_users = user.delet("j_snow")
print("User deleted:", res_delt_users)

# user2 = Users("Bran","Stark","bs","stark@winter.com","passBran")
# user2.show_user_info()
# user2.save_user()
