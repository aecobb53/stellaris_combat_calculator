from asyncio import shield
import random

"""
Assumed fully upgraded due to MVP1
"""

# Energy
## Anti-Armor
class Laser:
    def __init__(self):

        self.cooldown = 4.6
        self.accuracy = 90
        self.shield_damage_multiplier = 0.5 # %
        self.armor_damage_multiplier = 1.5 # %
        self.hull_damage_multiplier = 1.0 # %

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

    def fire(self, target):
        self.time_until_next_fire = self.cooldown
        shield_points = target.shield_points
        armor_points = target.armor_points
        hull_points = target.hull_points
        damage = random.randint(self.damage_per_hit[0], self.damage_per_hit[1])

        shield_damage = damage * self.shield_damage_multiplier
        if shield_points >= shield_damage:
            shield_points -= shield_damage
            return shield_points, armor_points, hull_points
        else:
            damage -= int(shield_points / self.shield_damage_multiplier)
            shield_points = 0

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

# plasma_launcher
# lance

# ## Anti-Hull
# mining_laser
# particle_launcher
# matter_disintegrator

# ## Penetrating
# disruptor
# cloud_lightning
# arc_emitter

# ## Anti_Shield
# energy_siphon
# null_void_beam


# # Kenetic
# mass_driver
# autocannon
# kinetic_launcher
# mega_cannon

# # Explosive
# normal_missiles
# scourge_missiles
# swarmer_missiles
# torpedoes

# # Strike Craft
# regular_strike_craft
# amoeba

# # Point Defense
# flak_gun
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