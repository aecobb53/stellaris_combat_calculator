import json
import re
import uuid
import copy

from turrets import (
    Small,
    Medium,
    Large,
    ExtraLarge,
    Titan,
    Guided,
    PointDefense,
    Hanger,
)

turret_name_map = {
    'small': 'Small',
    'medium': 'Medium',
    'large': 'Large',
    'extra_large': 'ExtraLarge',
    'titan': 'Titan',
    'guided': 'Guided',
    'point': 'PointDefense',
    'hanger': 'Hanger',
}


class BaseShipClass:
    def __init__(self):
        self.command_points = None
        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.build_time = None
        self.evasion = None
        self.speed = None
        self.hull_points = None
        self.armor_points = None
        self.shield_points = None

        self.resting_range = None
        self.position = None
        self.next_position = None

        self.turrets = []
        self.defenses = []
        self.computer_system = None

        self.countdown_until_ready_to_shoot = 0
        self.max_range = None

        # IDs
        self._my_id = None
        self.target_id = None
        self.targeted_by_ids = []

    @property
    def my_id(self):
        return self._my_id

    @my_id.setter
    def my_id(self, new_id):
        if self._my_id is not None:
            raise ValueError('This ship already has a UUID!!')
        self._my_id = new_id

    def build(self):
        self.my_id = uuid.uuid4()
        self.max_range = max([
            t.weapon.range for t in self.turrets if t.weapon is not None and t.weapon.range is not None
        ])
        self.resting_range = self.max_range # This depends on the computer not the range but i needed it to be set somehow

        self.default_hull_points = self.hull_points
        self.default_armor_points = self.armor_points
        self.default_shield_points = self.shield_points

    def add_turret(self, turret_type):
        print(f"Adding turret type {turret_type}")
        self.turrets.append(copy.deepcopy(globals()[turret_name_map[turret_type]]()))

    def calculate_resting_range(self):
        if not self.resting_range:
            resting_range = 0
            for turret in self.turrets:
                resting_range = max([resting_range, turret.weapon.range])
            self.resting_range = resting_range
        return self.resting_range

    # def calculate_gun_availability(self):
    #     for turret in self.turrets:
    #         print(turret.countdown_until_ready_to_shoot)

    def move_ship(self):
        if self.next_position:
            self.position = self.next_position
            self.next_position = None


class Corvette(BaseShipClass):
    def __init__(self):
        super().__init__()
        self.command_points = 1
        self.cost_alloys = 30
        self.build_time = 60
        self.evasion = 0.60
        self.speed = 160
        self.hull_points = 300
        self.armor_points = 0
        self.shield_points = 0
        self.core = None

    def set_core(self, name):
        print(f'setting core to {name}')
        getattr(self, f"core_{name}")()

    def core_interceptor(self):
        print('adding interceptor core')
        self.core = 'interceptor'
        self.add_turret('small')
        self.add_turret('small')
        self.add_turret('small')

    def core_missile_boat(self):
        print('adding missile_boat core')
        self.add_turret('small')
        self.add_turret('guided')

    def core_picket_ship(self):
        print('adding picket_ship core')
        self.add_turret('small')
        self.add_turret('small')
        self.add_turret('point')

    def ship_overview(self):
        pass


class Destroyer(BaseShipClass):
    def __init__(self):
        super().__init__()
        self.command_points = 2
        self.cost_alloys = 60
        self.build_time = 120
        self.evasion = 0.35
        self.speed = 140
        self.hull_points = 800
        self.armor_points = 0
        self.shield_points = 0
        self.bow = None
        self.stern = None

    def set_bow(self, name):
        print(f'setting bow to {name}')
        getattr(self, f"bow_{name}")()

    def set_stern(self, name):
        print(f'setting stern to {name}')
        getattr(self, f"stern_{name}")()

    # Bow
    def bow_artillery(self):
        print('adding artillery bow')
        self.bow = 'artillery'
        self.add_turret('large')

    def bow_gunship(self):
        print('adding gunship bow')
        self.bow = 'gunship'
        self.add_turret('small')
        self.add_turret('small')
        self.add_turret('medium')

    def bow_picket(self):
        print('adding picket bow')
        self.bow = 'picket'
        self.add_turret('small')
        self.add_turret('small')
        self.add_turret('point')

    # Stern
    def stern_gunship(self):
        print('adding gunship stern')
        self.stern = 'gunship'
        self.add_turret('medium')

    def stern_interceptor(self):
        print('adding interceptor stern')
        self.stern = 'interceptor'
        self.add_turret('small')
        self.add_turret('small')

    def stern_picket(self):
        print('adding picket stern')
        self.stern = 'picket'
        self.add_turret('point')
        self.add_turret('point')

    def ship_overview(self):
        pass

class Cruiser(BaseShipClass):
    def __init__(self):
        super().__init__()
        self.command_points = 4
        self.cost_alloys = 120
        self.build_time = 240
        self.evasion = 0.10
        self.speed = 120
        self.hull_points = 1800
        self.armor_points = 0
        self.shield_points = 0
        self.bow = None
        self.core = None
        self.stern = None

    def set_bow(self, name):
        print(f'setting bow to {name}')
        getattr(self, f"bow_{name}")()

    def set_core(self, name):
        print(f'setting core to {name}')
        getattr(self, f"core_{name}")()

    def set_stern(self, name):
        print(f'setting stern to {name}')
        getattr(self, f"stern_{name}")()

    # Bow
    def bow_artillery(self):
        print('adding artillery bow')
        self.bow = 'artillery'
        self.add_turret('large')

    def bow_broadside(self):
        print('adding broadside bow')
        self.bow = 'broadside'
        self.add_turret('medium')
        self.add_turret('medium')

    def bow_torpedo(self):
        print('adding torpedo bow')
        self.bow = 'torpedo'
        self.add_turret('small')
        self.add_turret('guided')
        self.add_turret('guided')

    # Core
    def core_artillery(self):
        print('adding artillery core')
        self.core = 'artillery'
        self.add_turret('medium')
        self.add_turret('large')

    def core_broadside(self):
        print('adding broadside core')
        self.core = 'broadside'
        self.add_turret('medium')
        self.add_turret('medium')
        self.add_turret('medium')

    def core_hangar(self):
        print('adding hangar core')
        self.core = 'hangar'
        self.add_turret('point')
        self.add_turret('point')
        self.add_turret('hanger')

    def core_torpedo(self):
        print('adding torpedo core')
        self.core = 'torpedo'
        self.add_turret('small')
        self.add_turret('small')
        self.add_turret('guided')
        self.add_turret('guided')

    # Stern
    def stern_broadside(self):
        print('adding broadside stern')
        self.stern = 'broadside'
        self.add_turret('medium')

    def stern_gunship(self):
        print('adding gunship stern')
        self.stern = 'gunship'
        self.add_turret('small')
        self.add_turret('small')

    def ship_overview(self):
        pass


class Battleship(BaseShipClass):
    def __init__(self):
        super().__init__()
        self.command_points = 8
        self.cost_alloys = 240
        self.build_time = 480
        self.evasion = 0.05
        self.speed = 100
        self.hull_points = 3000
        self.armor_points = 0
        self.shield_points = 0
        self.bow = None
        self.core = None
        self.stern = None

    def set_bow(self, name):
        print(f'setting bow to {name}')
        getattr(self, f"bow_{name}")()

    def set_core(self, name):
        print(f'setting core to {name}')
        getattr(self, f"core_{name}")()

    def set_stern(self, name):
        print(f'setting stern to {name}')
        getattr(self, f"stern_{name}")()

    # Bow
    def bow_artillery(self):
        print(f"adding artillery to bow")
        self.bow = 'Artillery'
        self.add_turret('large')
        self.add_turret('large')

    def bow_broadside(self):
        print(f"adding broadside to bow")
        self.bow = 'Broadside'
        self.add_turret('small')
        self.add_turret('small')
        self.add_turret('medium')
        self.add_turret('large')

    def bow_hangar(self):
        print(f"adding hangar to bow")
        self.bow = 'Hangar'
        self.add_turret('medium')
        self.add_turret('point')
        self.add_turret('point')
        self.add_turret('hanger')

    def bow_spinal(self):
        print(f"adding spinal to bow")
        self.bow = 'Spinal'
        self.add_turret('extra_large')

    # Core
    def core_artillery(self):
        print(f"adding artillery to core")
        self.core = 'Artillery'
        self.add_turret('large')
        self.add_turret('large')
        self.add_turret('large')

    def core_broadside(self):
        print(f"adding broadside to core")
        self.core = 'Broadside'
        self.add_turret('medium')
        self.add_turret('medium')
        self.add_turret('large')
        self.add_turret('large')

    def core_carrier(self):
        print(f"adding carrier to core")
        self.core = 'Carrier'
        self.add_turret('small')
        self.add_turret('small')
        self.add_turret('point')
        self.add_turret('point')
        self.add_turret('hanger')
        self.add_turret('hanger')

    def core_hangar(self):
        print(f"adding hangar to core")
        self.core = 'Hangar'
        self.add_turret('medium')
        self.add_turret('medium')
        self.add_turret('medium')
        self.add_turret('medium')
        self.add_turret('hanger')

    # Stern
    def stern_artillery(self):
        print(f"adding artillery to stern")
        self.stern = 'Artillery'
        self.add_turret('large')

    def stern_broadside(self):
        print(f"adding broadside to stern")
        self.stern = 'Broadside'
        self.add_turret('medium')
        self.add_turret('medium')

    def ship_overview(self):
        pass


class Titan(BaseShipClass):
    def __init__(self):
        super().__init__()
        self.command_points = 16
        self.cost_alloys = 480
        self.build_time = 3600
        self.evasion = 0.05
        self.speed = 100
        self.hull_points = 10000
        self.armor_points = 0
        self.shield_points = 0
        self.bow = None
        self.core = None
        self.stern = None

    def set_bow(self, name):
        print(f'setting bow to {name}')
        getattr(self, f"bow_{name}")()

    def set_core(self, name):
        print(f'setting core to {name}')
        getattr(self, f"core_{name}")()

    def set_stern(self, name):
        print(f'setting stern to {name}')
        getattr(self, f"stern_{name}")()

    # bow
    def bow_titan(self):
        print(f"adding titan to bow")
        self.bow = 'Titan'
        self.add_turret('titan')

    # core
    def core_titan(self):
        print(f"adding titan to core")
        self.core = 'Titan'
        self.add_turret('large')
        self.add_turret('large')
        self.add_turret('large')
        self.add_turret('large')

    # stern
    def stern_titan(self):
        print(f"adding titan to stern")
        self.stern = 'Titan'
        self.add_turret('large')
        self.add_turret('large')

    def ship_overview(self):
        pass


if __name__ == '__main__':
    # cov = Corvette()
    # cov.set_core('interceptor')
    # cov.turrets[0].set_weapon('laser')
    # cov.turrets[1].set_weapon('laser')
    # cov.turrets[2].set_weapon('laser')
    # for turret in cov.turrets:
    #     if turret.weapon:
    #         weapon = turret.weapon
    #         print(weapon)
    #         print(weapon.cooldown)
    #         print(weapon.cost_alloys)
    # # print(cov.__dict__)

    cruiser = Cruiser()
    cruiser.set_bow('artillery')
    cruiser.set_core('artillery')
    cruiser.turrets[0].set_weapon('laser')
    cruiser.turrets[1].set_weapon('laser')
    cruiser.turrets[2].set_weapon('laser')
    for turret in cruiser.turrets:
        print('')
        print(turret)
        if turret.weapon:
            weapon = turret.weapon
            print(weapon)

