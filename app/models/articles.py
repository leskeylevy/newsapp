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

    # def save_article(self):
    #     Article.all_articles.append(self)
    #
    # @classmethod
    # def clear_article(cls):
    #     Article.all_articles.clear()
