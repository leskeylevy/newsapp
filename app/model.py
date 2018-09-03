class Source:
    '''
    source clss definiton
    '''

    def __init__(self, name, url, description, rt):
        self.name = name
        self.url = url
        self.description = description
        self.rt = rt


class Article:
    all_articles = []

    def __init__(self, author, title, description, url, urlToImage):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage

    @classmethod
    def get_articles(cls, title):

        response = []

        for article in cls.all_articles:
            if article.source_name == name:
                response.append(article)

        return response
