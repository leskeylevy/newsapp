from flask import render_template
from . import main
from ..request import get_source,get_article


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting source news
    news = get_source()
    title = 'Welcome to The best news site there is out here'
    return render_template('index.html', title=title, news=news)


@main.route('/source/<name>')
def articles(name):
    '''
    source page fxn that returns the source details page and data
    :param name:
    :return:
    '''
    articles_display = get_article(name)

    return render_template('source.html',articles=articles_display)
