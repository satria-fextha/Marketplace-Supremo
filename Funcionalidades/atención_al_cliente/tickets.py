Filepath:/c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/atención_al_cliente/tickets.py
class Ticket:
    def __init__(self, user, issue):
        self.user = user
        self.issue = issue
        self.status = "Open"

class KnowledgeBase:
    def __init__(self):
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def search(self, query):
        results = []
        for article in self.articles:
            if query.lower() in article.lower():
                results.append(article)
        return results

class Support:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, user, issue):
        ticket = Ticket(user, issue)
        self.tickets.append(ticket)
        return ticket

    def close_ticket(self, ticket):
        ticket.status = "Closed"

    def prioritize_tickets(self):
        # Logic to prioritize tickets based on urgency or other criteria
        pass

    def respond_to_ticket(self, ticket, response):
        # Logic to respond to a ticket and handle user satisfaction
        pass

# Usage example
knowledge_base = KnowledgeBase()
knowledge_base.add_article("How to reset password")
knowledge_base.add_article("How to update profile")

support = Support()

# User searches for articles in the knowledge base
results = knowledge_base.search("password")
print(results)  # Output: ['How to reset password']

# User creates a ticket
ticket = support.create_ticket("John Doe", "I'm having trouble accessing my account")

# Support responds to the ticket
support.respond_to_ticket(ticket, "Please try resetting your password")

# Support closes the ticket
support.close_ticket(ticket)
