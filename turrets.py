import copy

from weapons import (
    Laser,
    MassDriver,
    NormalMissiles,
    RegularStrikeCraft,
    FlakGun,
)

weapon_name_map = {
    'laser': 'Laser',
    'mass_driver': 'MassDriver',
    'normal_missle': 'NormalMissiles',
    'regular_strike_craft': 'RegularStrikeCraft',
    'flak_gun': 'FlakGun',
}

class BaseTurretClass:
    def __init__(self):
        self.countdown_until_ready_to_shoot = 0

class Small(BaseTurretClass):
    def __init__(self):
        super().__init__()
        self.weapon = None

    def set_weapon(self, weapon):
        self.weapon = copy.deepcopy(globals()[weapon_name_map[weapon]]())
        self.weapon.small()

class Medium(BaseTurretClass):
    def __init__(self):
        super().__init__()
        self.weapon = None

    def set_weapon(self, weapon):
        self.weapon = copy.deepcopy(globals()[weapon_name_map[weapon]]())
        self.weapon.medium()

class Large(BaseTurretClass):
    def __init__(self):
        super().__init__()
        self.weapon = None

    def set_weapon(self, weapon):
        self.weapon = copy.deepcopy(globals()[weapon_name_map[weapon]]())
        self.weapon.large()

class ExtraLarge(BaseTurretClass):
    def __init__(self):
        super().__init__()
        self.weapon = None

    def set_weapon(self, weapon):
        self.weapon = copy.deepcopy(globals()[weapon_name_map[weapon]]())
        self.weapon.extra_large()

class Titan(BaseTurretClass):
    def __init__(self):
        super().__init__()
        self.weapon = None

    def set_weapon(self, weapon):
        self.weapon = copy.deepcopy(globals()[weapon_name_map[weapon]]())
        self.weapon.titan()


class Guided(BaseTurretClass):
    def __init__(self):
        super().__init__()
        self.weapon = None

    def set_weapon(self, weapon):
        self.weapon = copy.deepcopy(globals()[weapon_name_map[weapon]]())
        self.weapon.guided()


class PointDefense(BaseTurretClass):
    def __init__(self):
        super().__init__()
        self.weapon = None

    def set_weapon(self, weapon):
        self.weapon = copy.deepcopy(globals()[weapon_name_map[weapon]]())
        self.weapon.point_defense()


class Hanger(BaseTurretClass):
    def __init__(self):
        super().__init__()
        self.weapon = None

    def set_weapon(self, weapon):
        self.weapon = copy.deepcopy(globals()[weapon_name_map[weapon]]())
        self.weapon.hanger()
