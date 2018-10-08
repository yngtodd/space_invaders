from settings import Settings


class WeaponSettings(Settings):
    """
    Stores values for ship weapons.
    """
    def __init__(self):
        super().__init__()
        self.speed_factor = 3
        self.width = 3
        self.height = 15
        self.color = (255, 215, 0)
        self.ammo_allowed = 5
