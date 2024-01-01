El filepath es: /c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/blog/seo.py
class Blog:
    def __init__(self):
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def get_articles(self):
        return self.articles

    def search_articles(self, keyword):
        matching_articles = []
        for article in self.articles:
            if keyword.lower() in article.lower():
                matching_articles.append(article)
        return matching_articles

    def get_article_count(self):
        return len(self.articles)


blog = Blog()

# Example usage:
blog.add_article("Introduction to Agriculture")
blog.add_article("Benefits of Organic Farming")
blog.add_article("Livestock Management Techniques")

articles = blog.get_articles()
print("All Articles:")
for article in articles:
    print(article)

keyword = "organic"
matching_articles = blog.search_articles(keyword)
print(f"\nArticles containing '{keyword}':")
for article in matching_articles:
    print(article)

article_count = blog.get_article_count()
print(f"\nTotal Articles: {article_count}")
