import json
def add_contact(naam,num):
    naam=naam.title()
    perm={}
    temp={}
    temp[naam]=num
    perm.update(temp)
    try:
           with open("Book.json",'r')as file:
                 data=json.load(file)
    except FileNotFoundError:
          print("File not found!")
    dic=dict(data)
    dic.update(perm)
    try:
           with open("Book.json",'w')as file:
                 json.dump(dic,file)
    except FileNotFoundError:
          print("File not found!")

def remove_contact(naam):
    naam=naam.title()
    try:
           with open("Book.json",'r')as file:
                 data=json.load(file)
    except FileNotFoundError:
          print("File not found!")
      
    dic=dict(data)
    if naam in  dic.keys():
          del dic[naam]
    else:
          print("Name not found!")
          
    
    try:
           with open("Book.json",'w')as file:
                 json.dump(dic,file)
    except FileNotFoundError:
          print("File not found!")

def search_contact(naam):
    naam=naam.title()

    try:
           with open("Book.json",'r')as file:
                 data=json.load(file)
    except FileNotFoundError:
          print("File not found!")
    dic=dict(data)
    if naam in dic.keys():
          print(f"{naam}:{dic[naam]}")
    else:
          print("Name not found!")   

def display_contact():
    key_list=[]
    value_list=[]
   
    try:
           with open("Book.json",'r')as file:
                 data=json.load(file)
    except FileNotFoundError:
          print("File not found!")
    dic=dict(data)
    for x in dic.keys():
          key_list.append(x)
          
    for y in dic.values():
          value_list.append(y)

    for x,y in zip(key_list,value_list):
          print(f"{x} : {y}")
    
while True:

      print("_"*20)
      print("Phone Book Menue")
      print("1.Add Contact")
      print("2.Remove Contact")
      print("3.Search Contact")
      print("4.Display Contact")
      print("5.Exit")
      print("_"*20)
      choice=input("Enter your choice: ")
      match choice:
            case"1":
                 
                 print("_"*20)
                 print("1.Add Contact")
                 name=input("Enter your name: ")
                 num=input("Enter your number: ")
                 add_contact(name,num)
                 print("_"*20)
                 
            case"2":
                print("_"*20)
                print("2.Remove Contact")
                name=input("Enter your name: ")
                remove_contact(name)
                print("_"*20)
            case"3":
                print("_"*20)
                print("3.Search Contact")
                name=input("Enter your name: ")
                search_contact(name)
                print("_"*20)
            case"4":
                  print("_"*20)
                  print("4.Display Contact")
                  display_contact()
                  print("_"*20)
            case"5":
                  print("Thanks for using Phone Book!......")
                  break
            case _:
                  print("Invalid Choice!")
      

