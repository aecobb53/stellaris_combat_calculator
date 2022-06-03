import random

"""
Assumed fully upgraded due to MVP1
"""

class BaseWeaponClass:
    def __init__(self):
        is_point_defense = False
        is_missle = False
        is_strike_craft = False

# a = [
#     'Small',
#     'Medium',
#     'Large',
#     'ExtraLarge',
#     'Titan',
#     'Guided',
#     'PointDefense',
#     'Hanger',
# ]
# b = [
#     'Corvette',
#     'Destroyer',
#     'Cruiser',
#     'Battleship',
#     'Titan',
# ]

# for i in a:
#     print(f"    {i}:")
#     for j in b:
#         print(f"        {j}: 1")

    def fire(self, target):
        self.time_until_next_fire = self.cooldown
        shield_points = target.shield_points
        armor_points = target.armor_points
        hull_points = target.hull_points
        damage = random.randint(self.damage_per_hit[0], self.damage_per_hit[1])

        if self.shield_damage_multiplier is not None:
            shield_damage = damage * self.shield_damage_multiplier
            if shield_points >= shield_damage:
                shield_points -= shield_damage
                return shield_points, armor_points, hull_points
            else:
                damage -= int(shield_points / self.shield_damage_multiplier)
                shield_points = 0

        if self.armor_damage_multiplier is not None:
            armor_damage = damage * self.armor_damage_multiplier
            if armor_points >= armor_damage:
                armor_points -= armor_damage
                return shield_points, armor_points, hull_points
            else:
                damage -= int(armor_points / self.armor_damage_multiplier)
                armor_points = 0

        hull_damage = damage * self.hull_damage_multiplier
        if hull_points >= hull_damage:
            hull_points -= hull_damage
            return shield_points, armor_points, hull_points
        else:
            damage -= int(hull_points / self.hull_damage_multiplier)
            hull_points = 0
        return shield_points, armor_points, hull_points

    def reduce_cooldown(self, time):
        self.time_until_next_fire -= time


"""
    def small(self):
        self.cost_alloys = 
        self.cost_crystals = 
        self.power_required = 
        self.damage_per_hit = (, )
        self.range = 
        self.tracking = 

    def medium(self):
        self.cost_alloys = 
        self.cost_crystals = 
        self.power_required = 
        self.damage_per_hit = (, )
        self.range = 
        self.tracking = 

    def large(self):
        self.cost_alloys = 
        self.cost_crystals = 
        self.power_required = 
        self.damage_per_hit = (, )
        self.range = 
        self.tracking = 

    def __init__(self):
        self.cooldown = 
        self.accuracy = 
        self.shield_damage_multiplier =  # % or None for ignores
        self.armor_damage_multiplier =  # % or None for ignores
        self.hull_damage_multiplier =  # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0
"""

# Energy
## Anti-Armor
class Laser(BaseWeaponClass):
    def __init__(self):
        self.cooldown = 4.6
        self.accuracy = 90
        self.shield_damage_multiplier = 0.5 # % or None for ignores
        self.armor_damage_multiplier = 1.5 # % or None for ignores
        self.hull_damage_multiplier = 1.0 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def small(self):
        self.cost_alloys = 22
        self.cost_crystals = 0.33
        self.power_required = 17
        self.damage_per_hit = (17, 46)
        self.range = 40
        self.tracking = 0.50

    def medium(self):
        self.cost_alloys = 44
        self.cost_crystals = 0.65
        self.power_required = 30
        self.damage_per_hit = (43, 115)
        self.range = 60
        self.tracking = 0.30

    def large(self):
        self.cost_alloys = 88
        self.cost_crystals = 1.30
        self.power_required = 59
        self.damage_per_hit = (102, 276)
        self.range = 80
        self.tracking = .05

class PlasmaLauncher(BaseWeaponClass):
    def __init__(self):
        self.cooldown = 5.1
        self.accuracy = 80
        self.shield_damage_multiplier = 0.25 # % or None for ignores
        self.armor_damage_multiplier = 2.0 # % or None for ignores
        self.hull_damage_multiplier = 1.5 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def small(self):
        self.cost_alloys = 22
        self.cost_gasses = 0.33
        self.power_required = 17
        self.damage_per_hit = (20, 42)
        self.range = 30
        self.tracking = 0.4

    def medium(self):
        self.cost_alloys = 44
        self.cost_gasses = 0.65
        self.power_required = 30
        self.damage_per_hit = (50, 105)
        self.range = 30
        self.tracking = 0.2

    def large(self):
        self.cost_alloys = 88
        self.cost_gasses = 1.3
        self.power_required = 59
        self.damage_per_hit = (120, 252)
        self.range = 70
        self.tracking = 0.05

class Lance(BaseWeaponClass):
    def __init__(self):
        self.cooldown = 8
        self.accuracy = 85
        self.shield_damage_multiplier = 0.5 # % or None for ignores
        self.armor_damage_multiplier = 2.0 # % or None for ignores
        self.hull_damage_multiplier = 1.5 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def extra_large(self):
        self.cost_alloys = 229
        self.cost_crystals = 3.38
        self.power_required = 250
        self.damage_per_hit = (800, 2000)
        self.range = 150
        self.tracking = 0.0

## Anti-Hull
class MiningLaser(BaseWeaponClass):
    def __init__(self):
        self.cooldown = 4
        self.accuracy = 70
        self.shield_damage_multiplier = 0.5 # % or None for ignores
        self.armor_damage_multiplier = 1.25 # % or None for ignores
        self.hull_damage_multiplier = 1.75 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def small(self):
        self.cost_alloys = 13
        self.power_required = 7
        self.damage_per_hit = (9, 22)
        self.range = 30
        self.tracking = 0.75

    def medium(self):
        self.cost_alloys = 26
        self.power_required = 13
        self.damage_per_hit = (23, 55)
        self.range = 60
        self.tracking = 0.7

class ParticleLauncher(BaseWeaponClass):
    def __init__(self):
        self.cooldown = 16
        self.accuracy = 90
        self.shield_damage_multiplier = 0.5 # % or None for ignores
        self.armor_damage_multiplier = 1.5 # % or None for ignores
        self.hull_damage_multiplier = 1.75 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def large(self):
        self.cost_alloys = 114
        self.cost_crystals = 1.69
        self.power_required = 90
        self.damage_per_hit = (468, 1040)
        self.range = 130
        self.tracking = 0.0

class MatterDisintegrator(BaseWeaponClass):
    def __init__(self):
        self.cooldown = 4.5
        self.accuracy = 90
        self.shield_damage_multiplier = 0.5 # % or None for ignores
        self.armor_damage_multiplier = 1.5 # % or None for ignores
        self.hull_damage_multiplier = 2.0 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def small(self):
        self.cost_alloys = 29
        self.cost_crystals = 0.43
        self.power_required = 25
        self.damage_per_hit = (20, 49)
        self.range = 60
        self.tracking = 0.6

    def medium(self):
        self.cost_alloys = 57
        self.cost_crystals = 0.85
        self.power_required = 50
        self.damage_per_hit = (50, 123)
        self.range = 90
        self.tracking = 0.3

    def large(self):
        self.cost_alloys = 114
        self.cost_crystals = 1.69
        self.power_required = 100
        self.damage_per_hit = (120, 294)
        self.range = 120
        self.tracking = 0.05

## Penetrating
class Disruptor(BaseWeaponClass):
    def __init__(self):
        self.cooldown = 6.1
        self.accuracy = 100
        self.shield_damage_multiplier = None # % or None for ignores
        self.armor_damage_multiplier = None # % or None for ignores
        self.hull_damage_multiplier = 1.0 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def small(self):
        self.cost_alloys = 22
        self.cost_crystals = 0.33
        self.power_required = 17
        self.damage_per_hit = (1, 30)
        self.range = 30
        self.tracking = 0.6

    def medium(self):
        self.cost_alloys = 44
        self.cost_crystals = 0.65
        self.power_required = 30
        self.damage_per_hit = (1, 75)
        self.range = 50
        self.tracking = 0.35

class CloudLightning(BaseWeaponClass):
    def __init__(self):
        self.cooldown = 6
        self.accuracy = 100
        self.shield_damage_multiplier = None # % or None for ignores
        self.armor_damage_multiplier = None # % or None for ignores
        self.hull_damage_multiplier = 1.0 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def large(self):
        self.cost_alloys = 17
        self.power_required = 40
        self.damage_per_hit = (1, 136)
        self.range = 60
        self.tracking = 0.3

class ArcEmitter(BaseWeaponClass):
    def __init__(self):
        self.cooldown = 8.1
        self.accuracy = 100
        self.shield_damage_multiplier = None # % or None for ignores
        self.armor_damage_multiplier = None # % or None for ignores
        self.hull_damage_multiplier = 1.0 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def extra_large(self):
        self.cost_alloys = 229
        self.cost_crystals = 3.38
        self.power_required = 250
        self.damage_per_hit = (1, 1700)
        self.range = 150
        self.tracking = 0.0

## Anti_Shield
class EnergySiphon(BaseWeaponClass):
    def __init__(self):
        self.cooldown = 4
        self.accuracy = 75
        self.shield_damage_multiplier = 2.0 # % or None for ignores
        self.armor_damage_multiplier = 0.25 # % or None for ignores
        self.hull_damage_multiplier = 1.0 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def small(self):
        self.cost_alloys = 15
        self.power_required = 10
        self.damage_per_hit = (10, 27)
        self.range = 50
        self.tracking = 0.5

class NullVoidBeam(BaseWeaponClass):
    def __init__(self):
        self.cooldown = 4.4
        self.accuracy = 90
        self.shield_damage_multiplier = 4.0 # % or None for ignores
        self.armor_damage_multiplier = 0.25 # % or None for ignores
        self.hull_damage_multiplier = 0.25 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def small(self):
        self.cost_alloys = 13
        self.power_required = 7
        self.damage_per_hit = (6, 16)
        self.range = 60
        self.tracking = 0.6

    def medium(self):
        self.cost_alloys = 26
        self.power_required = 13
        self.damage_per_hit = (15, 40)
        self.range = 90
        self.tracking = 0.3

    def large(self):
        self.cost_alloys = 52
        self.power_required = 26
        self.damage_per_hit = (36, 95)
        self.range = 120
        self.tracking = 0.05

# Kenetic
class MassDriver(BaseWeaponClass):
    def __init__(self):
        self.cooldown = 3.45
        self.accuracy = 75
        self.shield_damage_multiplier = 1.5 # % or None for ignores
        self.armor_damage_multiplier = 0.5 # % or None for ignores
        self.hull_damage_multiplier = 1.0 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def small(self):
        self.cost_alloys = 22
        self.cost_motes = 0.33
        self.power_required = 17
        self.damage_per_hit = (14, 46)
        self.range = 50
        self.tracking = 0.5

    def medium(self):
        self.cost_alloys = 44
        self.cost_motes = 0.65
        self.power_required = 30
        self.damage_per_hit = (35, 115)
        self.range = 75
        self.tracking = 0.3

    def large(self):
        self.cost_alloys = 88
        self.cost_motes = 1.3
        self.power_required = 59
        self.damage_per_hit = (84, 276)
        self.range = 100
        self.tracking = 0.05


# autocannon
# kinetic_launcher
# mega_cannon

# Explosive
class NormalMissiles(BaseWeaponClass):
    def __init__(self):
        self.is_missle = True
        self.cooldown = 6.8
        self.accuracy = 100
        self.shield_damage_multiplier = None # % or None for ignores
        self.armor_damage_multiplier = 1.0 # % or None for ignores
        self.hull_damage_multiplier = 1.25 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def guided(self):
        self.cost_alloys = 44
        self.cost_motes = 0.65
        self.power_required = 26
        self.damage_per_hit = (86, 114)
        self.range = 100
        self.tracking = 0.25

# scourge_missiles
# swarmer_missiles
# torpedoes

# Strike Craft
class RegularStrikeCraft(BaseWeaponClass):
    def __init__(self):
        self.is_strike_craft = True
        self.cooldown = 2.3
        self.accuracy = 100
        self.shield_damage_multiplier = None # % or None for ignores
        self.armor_damage_multiplier = 1.5 # % or None for ignores
        self.hull_damage_multiplier = 1.0 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def hanger(self):
        self.cost_alloys = 88
        self.power_required = 59
        self.damage_per_hit = (6, 17)
        self.range = None # It has no range limit
        self.tracking = 1.0

# amoeba

# Point Defense
class FlakGun(BaseWeaponClass):
    def __init__(self):
        self.is_point_defense = True
        self.cooldown = 0.5
        self.accuracy = 75
        self.shield_damage_multiplier = 1.0 # % or None for ignores
        self.armor_damage_multiplier = 0.25 # % or None for ignores
        self.hull_damage_multiplier = 1.0 # % or None for ignores

        self.cost_alloys = None
        self.cost_crystals = None
        self.cost_motes = None
        self.cost_gasses = None
        self.power_required = None
        self.damage_per_hit = None
        self.range = None
        self.tracking = None # %

        self.time_until_next_fire = 0

    def point_defense(self):
        self.cost_alloys = 13
        self.power_required = 10
        self.damage_per_hit = (2, 6)
        self.range = 30
        self.tracking = 0.7

# point_defense

# # Titanic
# perdition_beam
# ion_cannon






























# lst = [
#     'plasma_launcher',
#     'lance',
#     'mining_laser',
#     'particle_launcher',
#     'matter_disintegrator',
#     'disruptor',
#     'cloud_lightning',
#     'arc_emitter',
#     'energy_siphon',
#     'null_void_beam',
#     'mass_driver',
#     'autocannon',
#     'kinetic_launcher',
#     'mega_cannon',
#     'normal_missiles',
#     'scourge_missiles',
#     'swarmer_missiles',
#     'torpedoes',
#     'regular_strike_craft',
#     'amoeba',
#     'flak_gun',
#     'point_defense',
#     'perdition_beam',
#     'ion_cannon',
# ]
# PlasmaLauncher
# Lance
# MiningLaser
# ParticleLauncher
# MatterDisintegrator
# Disruptor
# CloudLightning
# ArcEmitter
# EnergySiphon
# NullVoidBeam
# MassDriver
# Autocannon
# KineticLauncher
# MegaCannon
# NormalMissiles
# ScourgeMissiles
# SwarmerMissiles
# Torpedoes
# RegularStrikeCraft
# Amoeba
# FlakGun
# PointDefense
# PerditionBeam
# IonCannon