class Settings:
    # A clas to add all the settings for the Alien Invador game.
    def __init__(self):
        # Windowed Mode Screen
        self.window_width = 800
        self.window_height = 500
        
        #Full Screen Mode 
        self.screen_width = self.window_width
        self.screen_height = self.window_height

        # Background Color
        self.bg_color = (11, 12, 16)


        # Ship Settings
        self.ship_speed = 1.5
        self.ship_limit = 4

        # Setting Bullet 
        self.bullet_speed = 1.5
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = (50, 205, 50)
        
        self.bullets_allowed = 4

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        #  Game Speed up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 10

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale 

        self.alien_points = int (self.alien_points * self.score_scale)
        print(self.alien_points)
        

