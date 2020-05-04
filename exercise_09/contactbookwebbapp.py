from flask import Flask, redirect, url_for, request, render_template
from AddressBook import AddressBook
app = Flask(__name__)
AB = AddressBook()


@app.route('/')
def mainpage():
    #- page
    #- menu
    #- creating, updating, searching and removing
    contacts = AB.get_contacts()
    return render_template('index.html', len=len(contacts), contacts=contacts)


@app.route('/create', methods=['POST'])
def create_record():
    if request.method == 'POST':
        AB.add_contact(
            request.form['name'],
            request.form['address'],
            request.form['bday'],
            request.form['phone'],
            request.form['email'],
            request.form['profession'],
            request.form['interests']
        )
        return redirect('/')
    else:
        return "Invalid reguest"


@app.route('/update/<int:id>')
def update_record(id):
    if request.method == 'GET':
        contacts = AB.get_contacts()
        return render_template('update.html', contact = contacts[id], id=id)
    else:
        return "Invalid reguest"


@app.route('/makeupdate', methods=['POST'])
def makeupdate_record():
    if request.method == 'POST':
        AB.update_contact(
            int(request.form['id']),
            request.form['name'],
            request.form['address'],
            request.form['bday'],
            request.form['phone'],
            request.form['email'],
            request.form['profession'],
            request.form['interests']
        )
        return redirect('/')
    else:
        return "Invalid request"


@app.route('/search', methods=['POST'])
def search_record():
    if request.method == 'POST':
        regex = request.form['regex']
        contacts = AB.search_contacts(regex)
        return render_template('index.html', len=len(contacts), contacts=contacts)


@app.route('/remove/<int:id>')
def remove_record(id):
    AB.delete_contact(id)
    return redirect('/')

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
# if request.method == 'POST':
#      user = request.form['nm']
 #     user += " POST"
 #     return redirect(url_for('success',name = user))
# else:
# return """
# """


if __name__ == '__main__':
    app.run(port=5010, debug=True)
