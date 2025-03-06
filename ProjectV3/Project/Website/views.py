from flask import Blueprint, render_template
from flask_login import login_required, current_user
views = Blueprint('views', __name__)

@views.route('/') # innit to here
@login_required
def home():
    return render_template("home.html", user=current_user) # it will render the template of home.html this is the design



