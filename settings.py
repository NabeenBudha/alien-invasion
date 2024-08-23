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

