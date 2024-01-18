Filepath:/c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/programa_de_afiliados/Analytics.py
class AffiliateAnalytics:
    def __init__(self):
        self.referral_rewards = {}

    def track_referral(self, user_id, referral_type):
        if user_id not in self.referral_rewards:
            self.referral_rewards[user_id] = 0

        if referral_type == 'registration':
            self.referral_rewards[user_id] += 10  # Reward 10 credits for registration
        elif referral_type == 'purchase':
            self.referral_rewards[user_id] += 20  # Reward 20 credits for purchase

    def get_reward_balance(self, user_id):
        return self.referral_rewards.get(user_id, 0)
