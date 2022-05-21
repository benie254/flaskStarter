from flask import render_template,redirect,url_for,request,abort
from . import main
from flask_login import login_required,current_user
from .. import db,photos


# views
@main.route('/', methods=['GET', 'POST'])
def index():
    """
    :return: index page + data
    """

    title = 'Home- Welcome!'

    return render_template('index.html', title=title)