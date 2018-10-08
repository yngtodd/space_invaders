from settings import Settings


class ShipSettings(Settings):
    """Stores settings for friendly ship."""
    def __init__(self):
        super().__init__()
        self.speed_factor = 2.5
        self.ship_limit = 3
        self.ships_left = self.ship_limit
