import copy
import random

from utils import load_config

from weapons import (
    Laser,
    PlasmaLauncher,
    Lance,
    MiningLaser,
    ParticleLauncher,
    MatterDisintegrator,
    MatterDisintegrator,
    Disruptor,
    CloudLightning,
    ArcEmitter,
    EnergySiphon,
    NullVoidBeam,
    MassDriver,
    NormalMissiles,
    RegularStrikeCraft,
    FlakGun,
)

weapon_name_map = {
    'laser': 'Laser',
    'plasma_launcher': 'PlasmaLauncher',
    'lance': 'Lance',
    'mining_laser': 'MiningLaser',
    'particle_launcher': 'ParticleLauncher',
    'matter_disintegrator': 'MatterDisintegrator',
    'disruptor': 'Disruptor',
    'cloud_lightning': 'CloudLightning',
    'arc_emitter': 'ArcEmitter',
    'energy_siphon': 'EnergySiphon',
    'null_void_beam': 'NullVoidBeam',
    'mass_driver': 'MassDriver',

    'normal_missle': 'NormalMissiles',
    'regular_strike_craft': 'RegularStrikeCraft',
    'flak_gun': 'FlakGun',
}

class BaseTurretClass:
    def __init__(self):
        self.countdown_until_ready_to_shoot = 0
        self.config = load_config()

        self.target_id = None

    def select_target(self, targets):
        """
        Take a list of targets. Randomize the list. Associate the targets with how likely the turret is to select them
        Order the list based on the highest selection
        Return the most likely (knowing there are likely more than one ship of the same target value which is why we randomize it)
        """
        selection = []
        random.shuffle(targets)
        for target in targets:
            turret_class = type(self).__name__
            ship_class = type(target).__name__
            ship_class_constant = self.config['turret_targeting_class_modifiers'][turret_class][ship_class]
            selection.append((target, ship_class_constant))
        selection.sort(key=lambda i: i[1], reverse=True)
        return selection[0][0]


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
