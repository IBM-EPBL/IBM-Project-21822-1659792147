class Sources:
    def _init_(self, name, description, url):
        self.name=name,
        self.description=description
        self.url=url
        
class Articles:
    '''Define article model'''
    def _init_(self, source, author, title, description, url, urlToImage, publishedAt):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
