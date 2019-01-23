from flask import Blueprint

admin_panel = Blueprint('admin', __name__)

@admin_panel.route('/admin_panel')
def timeline():
    # Do some stuff
    return "admin"