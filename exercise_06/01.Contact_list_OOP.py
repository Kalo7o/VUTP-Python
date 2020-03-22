import numpy as np
import os

class AddressBook:
    def __init__(self):
        self.contact_list = []

    def add_contact(self):
        contact_item = [
            input("Contact name: "),
            input("Contact address: "),
            input("Contact byrth day: "),
            input("Contact phone number: "),
            input("Contact email: "),
            input("Contact profession: "),
            input("Contact interests: ")
        ]
        self.contact_list.append(contact_item)

    def update_contact(self, id):
        print("Change Name: 0, Address: 1, Birth day: 2, Phone: 3, Email: 4, Profession: 5, Interests: 6")
        option = int(input("Choose an parameter: "))
        if option >= 0 and option <= 6:
            self.contact_list[id][option] = input()
        else:
            print("Invalid parameter")
            return

    def delete_contact(self, id):
        del self.contact_list[id]

    def show_contacts(self):
        for i in range(len(self.contact_list)):
            print("ID: ", i, ", name:", self.contact_list[i][0], ", address:", self.contact_list[i][1], ", byrth day:", self.contact_list[i][2], ", phone:",
                  self.contact_list[i][3], ", email:", self.contact_list[i][4], ", profession:", self.contact_list[i][5], ", interests:", self.contact_list[i][6])

    def help(self):
        print('Commands: add, remove, update, list, exit')

    def save(self):
        np.save('./exercise_06/Database.npy', self.contact_list)
        np.savetxt('./exercise_06/2darray.csv', self.contact_list, delimiter=',', fmt='%s')

    def load(self):
        self.contact_list = np.load('./exercise_06/Database.npy')


AB = AddressBook()
command = ''

while command != 'exit':
    AB.load()
    command = input()
    if command == 'add':
        AB.add_contact()
    elif command == 'remove':
        AB.delete_contact(int(input('ID: ')))
    elif command == 'update':
        AB.update_contact(int(input('ID: ')))
    elif command == 'list':
        AB.show_contacts()
    elif command == 'help':
        AB.help()
    elif command != 'exit':
        print("Invalid command, type \"help\" to view the commands.")
    AB.save()
