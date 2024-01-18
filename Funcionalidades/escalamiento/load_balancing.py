El filepath es: /c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/escalamiento/load_balancing.py
class LoadBalancer:
    def __init__(self):
        self.servers = []

    def add_server(self, server):
        self.servers.append(server)

    def remove_server(self, server):
        self.servers.remove(server)

    def get_next_server(self):
        # Implement your load balancing logic here
        # For example, you can use round-robin or random selection
        pass

# Example usage
lb = LoadBalancer()
lb.add_server("Server 1")
lb.add_server("Server 2")
lb.add_server("Server 3")

next_server = lb.get_next_server()
print(f"Next server: {next_server}")
