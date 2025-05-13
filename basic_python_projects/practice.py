contact={}
def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t{}".format(key,contact.get(key)))

while True:
    choice=int(input("1: Add contact\n2: search contact"
    "\n3: display contact\n4: Edit Contact\n5: Delete contact"
    "\n6 Exit\nEter Your choice"))
    if choice==1:
        name = input("Enter the Name:")
        phone= int(input("Enter the number: "))
        contact[name]=phone
    elif choice==2:
        search_contact=input("Enter the contact number for search!")
        if search_contact in contact:
            print(search_contact,"s number is",contact[search_contact])
        else:
            print("Name is not found!")
    elif choice==3:
        if not contact:
            print("Contact Book is empity")
        else:
            display_contact()       

