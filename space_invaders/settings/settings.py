class Settings:
    """Settings used by all sub-settings."""
    def __init__(self, speedup_scale=1.1):
        self.speedup_scale = speedup_scale
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed dynamics through gameplay."""
        self.speed_factor *= self.speedup_scale
