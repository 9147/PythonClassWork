# countries={"CA":"Canada",
#            "US":"United States",
#            'MX':"Mexico",
#            "FR":"France"}
#
# print('''COMMAND MENU
# view - View an element
# add - Add a element
# del - Delete an element
# exit - exit from the shell
# ''')
# commands={'view':lambda:view(),'add':lambda:add(),'del':lambda:delete(),'exit':lambda :exit()}
# while True:
#     val=input("Command: ")
#     commands[val]
#
# def view():
#     print("Country codes",*list(countries.keys()))
#     a=input("Enter the country codes")
#     print("Country name:",countries[a])
#
# def add():
#     code=input("Enter the country code: ")
#     name=input("Enter the country name: ")
#     countries[code]=name
#     print(countries[code]," was added.")
#
# def delete():
#     code=input("Enter the country code: ")
#     print(countries[code]," was deleted. ")
#     del countries[code]

print(sum([12,14]))