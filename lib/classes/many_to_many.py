class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = None
        self._magazine = None
        self._title = None
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    def get_title(self):
        return self._title

    def set_title(self, title):
        if not isinstance(title, str) or len(title) == 0:
            return None
        self._title = title

    title = property(get_title, set_title)

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author
    
    author = property(get_author, set_author)

    def get_magazine(self):
        return self._magazine

    def set_magazine(self, magazine):
        self._magazine = magazine

    magazine = property(get_magazine, set_magazine)

 
    
class Author:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self._name
    
    def set_name(self,name):
        if not isinstance(name, str) or len(name) == 0:
            return None
        if hasattr(self, '_name'):
            return None
        self._name = name
        
    name=property(get_name, set_name)

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
         return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self,magazine,title)

    def topic_areas(self):
        articles = self.articles()
        if not articles:
            return None
        return list(set(article.magazine.category for article in articles))

class Magazine:
    all_magazines=[]
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    name = property(get_name, set_name)

    def get_category(self):
        return self._category

    def set_category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category

    category = property(get_category, set_category)

    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        
    def contributors(self):
        authors = [article.author for article in self.articles()]
        return list(set(authors))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        count_author = {}
        for article in self.articles():
            author = article.author
            if author in count_author:
                count_author[author] += 1
            else:
                count_author[author] = 1

        contributing_authors = [author for author, count in count_author.items() if count > 2]

        if contributing_authors:
            return contributing_authors
        else:
            return None
    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        most_articles_magazine = max(cls.all_magazines, key=lambda mag: len(mag.articles()), default=None)
        if most_articles_magazine and len(most_articles_magazine.articles()) == 0:
            return None
        return most_articles_magazine