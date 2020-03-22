class Contact:
  def __init__(self, name, address, birth_day, phone_number, email, profession, interests):
    self.name = name
    self.address = address
    self.birth_day = birth_day
    self.phone_number = phone_number
    self.email = email
    self.profession = profession
    self.interests = interests

  def update(self):
    print("Change Name: 1, Address: 2, Birth day: 3, Phone: 4, Email: 5, Profession: 6, Interests: 7")
    option = int(input("Choose an parameter: "))
    if option == 1:
      self.name = input()
    elif option == 2:
      self.birth_day = input()
    elif option == 3:
      self.phone_number = input()
    elif option == 4:
      self.email = input()
    elif option == 5:
      self.profession = input()
    elif option == 6:
      self.interests = input()
    else:
      print("Invalid parameter")
      return

  def show(self):
    print("name:", self.name, ", address:", self.address, ", Phone:", self.phone_number, ", email:", self.email, ", profession:", self.profession, ", interests:", self.interests)


class AddressBook:
    def __init__(self):
        self.contact_list = []
    def add_contact(self):
        contact_item = Contact(
            input("Contact name: "),
            input("Contact address: "),
            input("Contact byrth day: "),
            input("Contact phone number: "),
            input("Contact email: "),
            input("Contact profession: "),
            input("Contact interests: ")
        )
        self.contact_list.append(contact_item)
    def update_contact(self, id):
      self.contact_list[id].update()

    def delete_contact(self, id):
      del self.contact_list[id]

    def show_contacts(self):
      for i in range(len(self.contact_list)):
        print("ID: ", i, end = ', ')
        self.contact_list[i].show()
        
    def help(self):
      print('Commands: add, remove, update, list, exit')

AB = AddressBook()
command = ''

while command != 'exit':
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
  else:
    print("Invalid command, type \"help\" to view the commands.")


