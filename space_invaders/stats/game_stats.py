class GameStats:
    """Track statistics for Space Invaders."""
    def __init__(self, ship_settings):
        self.ship_settings = ship_settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics for the game."""
        self.ships_left = self.ship_settings.ship_limit
