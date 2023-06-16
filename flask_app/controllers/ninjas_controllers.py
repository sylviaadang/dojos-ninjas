from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.dojos_model import Dojo
from flask_app.models.ninjas_model import Ninja



# show route for the adding a new ninja
@app.route('/add_ninja')
def show_ninja_form():
# def add_ninja():
#     ninja = Dojo.get_one( {'id': dojo_id})
    return render_template('new_ninja.html', all_dojos=Dojo.get_all())


# action route for adding a new ninja
@app.route('/add_newninja', methods=['POST'])
def add_ninja():
    Ninja.add_ninja(request.form)
    return redirect('/')
