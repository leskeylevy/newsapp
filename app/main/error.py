from flask import render_template
from . import main


@main.errorhandler(404)
def four_Ow_four(error):
    '''
    fxn to render the error page
    :param error:
    :return:
    '''
    return render_template('fourOwfour.html'), 404
