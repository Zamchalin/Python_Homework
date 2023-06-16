import os

def show_conracts(file_name) :
    os.system('CLS')
    with open(file_name,'r' ) as file:
        file = file.readlines()

        for contact in file :
            print(contact, end='')

    input('\nPress any key')

def add_contact(file_name) :
    os.system('CLS')
    with open(file_name,'a') as file :
        res = ''
        res += input('Input a surname of contact: ') + ' '
        res += input('Input a name of contact: ') + ' '
        res += input('Input a phonenumber of contact: ')

        file.write('\n' + res)
    
    input('Contact was added!Press any key for retutn.')

def search_contact(file_name) :
    os.system('CLS')
    target = input('Input name of contact for searching: ')

    with open(file_name, 'r') as file :
        file = file.readlines()

        for contact in file :
                if target in contact :
                    print(contact)
                    break
        else :
                print('There is not contacts with this name.')
    input('Press any key')

def drawing() :
    os.system('CLS')
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - seach contact')
    print('4 - edit contact')
    print('5 - delete contact ')
    print('6 - exit ')

def main(file_name) :
    while True :
        os.system('CLS')
        drawing()
        user_choice = int(input('Inpur a number from 1 to 6:'))

        if user_choice == 1 :
            show_conracts(file_name)
        elif user_choice == 2 :
            add_contact(file_name)
        elif user_choice == 3 :
            search_contact(file_name)
        elif user_choice == 4 :
            edit_contact(file_name) 
        elif user_choice == 5 :
            delete_contact(file_name) 
        elif user_choice == 6 :
            print('Have a nice day')
            return
        

def edit_contact(file_name):
    os.system('CLS')
    with open(file_name, "r") as data:
        contacts = data.read()
    print(contacts)
    print("")
    index_contact_edit = int(input("Input number line for edit: ")) - 1
    contacts_lines = contacts.split("\n")
    res = input('Input a new surname of contact: ') + ' '
    res += input('Input a new name of contact: ') + ' '
    res += input('Input a new phonenumber of contact: ')
    contacts_lines[index_contact_edit] = res
    print(contacts_lines)
    with open(file_name, "r+") as file:
        file.write("\n".join(contacts_lines))
    print('Contact changed')

def delete_contact(file_name) :
    os.system('CLS')
    with open(file_name, "r") as data:
        contacts = data.read()
    print(contacts)
    print("")
    index_contact_delete = int(input("Input number line for delete: ")) - 1
    contacts_lines = contacts.split("\n")
    contacts_lines.pop(index_contact_delete)
    with open(file_name, "r+") as file:
        file.write("\n".join(contacts_lines))
    print('Contact deleted')

