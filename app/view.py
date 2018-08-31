from flask import render_template
from app import app
from .request import get_source


# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting source news
    news = get_source()
    title = 'Welcome to The best news site there is out here'
    return render_template('index.html', title=title, news=news)


@app.route('/source/<source_name>')
def source(source_name):
    '''
    source page fxn that returns the source details page and data
    :param source_name:
    :return:
    '''
    return render_template('source.html', name=source_name)
