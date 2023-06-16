from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.dojos_model import Dojo

# render a template to show all the dojos
@app.route('/')
def home():
    dojos = Dojo.get_all()
    return render_template('new_dojo.html', dojos=dojos)


# action --> redirect to the show all dojos
@app.route('/createdojo', methods=['POST'])
def show_all_dojos():
    Dojo.add_dojo(request.form)
    return redirect('/')


# show route to show the page of the ninajs in a specific dojo
@app.route('/onedojo/<int:id>')
def show_ninjas_in_dojo(id):
    one_dojos_ninjas = Dojo.get_one({'id': id})

    return render_template('ninja_in_dojo.html', one_dojos_ninjas=one_dojos_ninjas)
