class Article:
    all_articles = []

    def __init__(self, author, title, description, urlToImage):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage

    def save_article(self):
        Article.all_articles.append(self)
        
