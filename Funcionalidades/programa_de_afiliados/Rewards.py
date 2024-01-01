El filepath es: /c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/programa_de_afiliados/Rewards.py
class AffiliateProgram:
    def __init__(self):
        self.users = {}

    def generate_affiliate_link(self, user_id):
        link = f"www.marketplace.com/affiliate/{user_id}"
        return link

    def register_user(self, user_id):
        self.users[user_id] = 0

    def reward_user(self, user_id, reward):
        if user_id in self.users:
            self.users[user_id] += reward
        else:
            print("User not found.")

# Example usage:
program = AffiliateProgram()
user_id = "12345"
program.register_user(user_id)
affiliate_link = program.generate_affiliate_link(user_id)
print(f"Share this affiliate link: {affiliate_link}")
program.reward_user(user_id, 10)
print(f"User {user_id} has earned {program.users[user_id]} rewards.")
