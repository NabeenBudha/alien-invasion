class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in inactive stats
        self.game_active = False

        # High score should be reseted
        self.high_score = 0
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1