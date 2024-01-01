Filepath:/c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/atención_al_cliente/Knowledge_base.py
class KnowledgeBase:
    def __init__(self):
        self.faq = {}  # Dictionary to store frequently asked questions and their answers

    def add_faq(self, question, answer):
        self.faq[question] = answer

    def search_faq(self, query):
        if query in self.faq:
            return self.faq[query]
        else:
            return "No matching FAQ found."

class CustomerSupport:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def search_solution(self, query):
        return self.knowledge_base.search_faq(query)

    def contact_support(self, query):
        # Logic to handle direct communication with support (e.g., chat, email, phone)
        return "Contacting support for query: " + query
