from settings import Settings


class AlienSettings(Settings):
    """Stores settings for alien ship."""
    def __init__(self):
        super().__init__()
        self.speed_factor = 1
        self.fleet_drop_speed = 15
        self.fleet_direction = 1
