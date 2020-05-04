import os
import csv
import re

class AddressBook:
    def __init__(self):
        self.contact_list = []
        self._load()

    def add_contact(self, name, address, bday, phone, email, profession, interests):
        contact_item = [ name, address, bday, phone, email, profession, interests ]
        self.contact_list.append(contact_item)
        self._save()

    def update_contact(self, id, name, address, bday, phone, email, profession, interests):
        self.contact_list[id][0] = name
        self.contact_list[id][1] = address
        self.contact_list[id][2] = bday
        self.contact_list[id][3] = phone
        self.contact_list[id][4] = email
        self.contact_list[id][5] = profession
        self.contact_list[id][6] = interests
        self._save()

    def delete_contact(self, id):
        del self.contact_list[id]
        self._save()

    def get_contacts(self):
        self._load()
        return self.contact_list
    
    def search_contacts(self, regex):
        found = []
        for contact in self.contact_list:
            for attr in contact:
                if re.search(regex, attr):
                    found.append(contact)
                    break
        return found


    def help(self):
        print('Commands: add, remove, update, list, exit')

    def _save(self):
        os.remove("./contacts.csv")
        with open('./contacts.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows(self.contact_list)
        self._load()

    def _load(self):
        with open('./contacts.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            data = []
            for row in csv_reader:
                data.append(row)
            self.contact_list = data

"""
AB = AddressBook()
command = ''

while command != 'exit':
    AB._load()
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
    AB._save()
"""