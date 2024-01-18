Filepath:/c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/programa_de_afiliados/referidos.py
class ReferralProgram:
    def __init__(self):
        self.referral_links = {}

    def generate_referral_link(self, user_id):
        referral_link = f"https://example.com/referral/{user_id}"
        self.referral_links[user_id] = referral_link
        return referral_link

    def process_referral(self, referral_link):
        user_id = referral_link.split("/")[-1]
        if user_id in self.referral_links:
            # Give reward to the user who referred
            reward = 10  # Example: 10 credits
            print(f"User {user_id} received a reward of {reward} credits!")
        else:
            print("Invalid referral link.")

# Usage example
referral_program = ReferralProgram()

# Generate referral link for user with ID 123
referral_link = referral_program.generate_referral_link(123)
print(f"Referral link for user 123: {referral_link}")

# Process a referral using the referral link
referral_program.process_referral(referral_link)
