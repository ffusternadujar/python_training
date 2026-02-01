user_name = input("Enter your name: ")
user_surname = input("Enter your surname: ")
message = "Hello %s %s!" % (user_name, user_surname)

greeting = f"Welcome, {user_name.capitalize()} {user_surname}!"
print(message)
print(greeting)

