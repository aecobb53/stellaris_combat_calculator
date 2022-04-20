import uuid
import copy
import random
import json


from math import comb
from ships import (
    Corvette,
    Destroyer,
    Cruiser,
    Battleship,
    Titan,
)


def return_calculated_ship_range(ship):
    """
    Function to allow sorting by position (closest first)
    """
    # return ship.calculate_resting_range()
    return ship.position

class Combat:
    def __init__(self):
        self.starting_range = 1000
        # self.starting_range = 30
        self.day_elapsed = 0.0
        self.ally_ships = []
        self.axes_ships = []
        self.ally_ships_destroyed = []
        self.axes_ships_destroyed = []

    def _ship_distance(self, ship1, ship2):
        ranges = {ship1.position, ship2.position}
        return max(ranges) - min(ranges)

    def _ship_target_options(self, ship, targets):
        target = targets[0]
        distance = self._ship_distance(ship, target)
        if distance > ship.max_range:
            return None
        return target

    def _sort_ship_list(self, ship_list):
        ship_list.sort(key=return_calculated_ship_range)
        return ship_list

    def _find_ship_by_id(self, ship_id, ship_list):
        for ship in ship_list:
            if ship.my_id == ship_id:
                return ship

    def _ship_movement(self, ship, enemy_swarm, percent_of_day_progressed):
        target_position = None
        speed = ship.speed
        if ship.target_id:
            target = self._find_ship_by_id(ship.target_id, enemy_swarm)
            if target:
                target_position = target.position
        if target_position is None:
            positions = []
            for enemy in enemy_swarm:
                positions.append(enemy.position)
            target_position = sum(positions) / len(positions)
        if abs(target_position - ship.position) < ship.resting_range:
            speed = speed * .1
            # speed = abs(min([(target_position - ship.position) / 2, speed]))
        # print(target_position, ship.position, ship.resting_range, speed)
        if (ship.position - target_position) > 0:
            # Move to the right
            sign = -1
        else:
            # Move to the left
            sign = 1
        new_position = ship.position + (sign * ship.speed * percent_of_day_progressed)
        return new_position

    def start_fight(self):
        for ship in self.ally_ships:
            ship.position = -self.starting_range
        for ship in self.axes_ships:
            ship.position = self.starting_range

    def assign_targets(self):
        self.ally_ships.sort(key=return_calculated_ship_range)
        self.axes_ships.sort(key=return_calculated_ship_range)
        ally_list = []
        axes_list = []
        for ship in self.ally_ships:
            if not axes_list:
                axes_list = copy.deepcopy(self._sort_ship_list(self.axes_ships))
            if ship.target_id:
                target = self._find_ship_by_id(ship.target_id, self.axes_ships)
                if not target:
                    ship.target_id = None
            if not ship.target_id:
                target = self._ship_target_options(ship, axes_list)
                if not target:
                    ship.target_id = None
                    continue
                ship.target_id = target.my_id
                for target_ships in self.axes_ships:
                    if target_ships.my_id == target.my_id:
                        target_ships.targeted_by_ids.append(ship.my_id)
                axes_list.remove(target)

        for ship in self.axes_ships:
            if not ally_list:
                ally_list = copy.deepcopy(self._sort_ship_list(self.ally_ships))
            if ship.target_id:
                target = self._find_ship_by_id(ship.target_id, self.ally_ships)
                if not target:
                    ship.target_id = None
            if not ship.target_id:
                target = self._ship_target_options(ship, ally_list)
                if not target:
                    ship.target_id = None
                    continue
                ship.target_id = target.my_id
                for target_ships in self.ally_ships:
                    if target_ships.my_id == target.my_id:
                        target_ships.targeted_by_ids.append(ship.my_id)
                ally_list.remove(target)

    def exchange_blasts(self):
        self.ally_ships.sort(key=return_calculated_ship_range)
        self.axes_ships.sort(key=return_calculated_ship_range)
        for ship in self.ally_ships:
            target = self._find_ship_by_id(ship.target_id, self.axes_ships)
            if target:
                distance = self._ship_distance(ship, target)
                for turret in ship.turrets:
                    # print(turret.weapon.time_until_next_fire)
                    if turret.weapon.time_until_next_fire > 0:
                        continue
                    if turret.weapon.range >= distance:
                        shield, armor, hull = turret.weapon.fire(target)
                        target.shield_points = shield
                        target.armor_points = armor
                        target.hull_points = hull

        for ship in self.axes_ships:
            target = self._find_ship_by_id(ship.target_id, self.ally_ships)
            if target:
                distance = self._ship_distance(ship, target)
                for turret in ship.turrets:
                    # print(turret.weapon.time_until_next_fire)
                    if turret.weapon.time_until_next_fire > 0:
                        continue
                    if turret.weapon.range >= distance:
                        shield, armor, hull = turret.weapon.fire(target)
                        target.shield_points = shield
                        target.armor_points = armor
                        target.hull_points = hull

        for ally_ship in self.ally_ships.copy():
            if ally_ship.hull_points <= 0:
                self.ally_ships_destroyed.append(ally_ships)
                self.ally_ships.remove(ally_ship)

        for axes_ship in self.axes_ships.copy():
            if axes_ship.hull_points <= 0:
                self.axes_ships_destroyed.append(axes_ships)
                self.axes_ships.remove(axes_ship)

    def move_ships(self, percent_of_day_progressed=1):
        # print(f"Day percent progress {percent_of_day_progressed}")
        for ship in self.ally_ships:
            new_position = self._ship_movement(ship, self.axes_ships, percent_of_day_progressed)
            if new_position:
                ship.next_position = new_position

        for ship in self.axes_ships:
            new_position = self._ship_movement(ship, self.ally_ships, percent_of_day_progressed)
            if new_position:
                ship.next_position = new_position

        for ship in self.ally_ships:
            ship.move_ship()

        for ship in self.axes_ships:
            ship.move_ship()

    def update_weapons_cooldown(self, time):
        for ship in self.ally_ships:
            for turret in ship.turrets:
                turret.weapon.reduce_cooldown(time)

        for ship in self.axes_ships:
            for turret in ship.turrets:
                turret.weapon.reduce_cooldown(time)

    def retro(self):
        results = {
            'time': float(int(self.day_elapsed * 100) / 100),
            "living_ships": {
                'ally': [str(type(s)) for s in self.ally_ships],
                'axes': [str(type(s)) for s in self.axes_ships],
            },
        }
        return results

    def commence_combat(self, day_percent=0.1):
        self.start_fight()
        while self.ally_ships and self.axes_ships:
            if int(self.day_elapsed * 100) % 100 == 0:
                print(f"day: {int(self.day_elapsed * 100) / 100}")
            self.move_ships(percent_of_day_progressed=day_percent)
            self.update_weapons_cooldown(time=day_percent)
            self.day_elapsed += day_percent
            self.assign_targets()
            self.exchange_blasts()
            # print('')
            # print([s.position for s in self.ally_ships])
            # print([s.position for s in self.axes_ships])
        return self.retro()


ally_ships = []
axes_ships = []

def build_fleet(base_object, side, number):
    for i in range(number):
        side.append(copy.deepcopy(base_object))

co = Corvette()
co.set_core('interceptor')
co.turrets[0].set_weapon('laser')
co.turrets[1].set_weapon('laser')
co.turrets[2].set_weapon('laser')

ds = Destroyer()
ds.set_bow('artillery')
ds.set_stern('gunship')
ds.turrets[0].set_weapon('laser')
ds.turrets[1].set_weapon('laser')

# Ally composition
# build_fleet(co, ally_ships, 4)
build_fleet(ds, ally_ships, 4)

# Axes composition
build_fleet(co, axes_ships, 10)
build_fleet(ds, axes_ships, 1)

for ship in ally_ships:
    ship.build()
for ship in axes_ships:
    ship.build()

combat = Combat()
combat.ally_ships = ally_ships
combat.axes_ships = axes_ships

results = combat.commence_combat()
print(json.dumps(results, indent=2))
# print(results[0])
# print(results[1])
# print(combat.__dict__)

# print('')
# print('')
# print('')
# combat.start_fight()

# itterable = 5000000

# day_percent = 0.1

# while combat.ally_ships and combat.axes_ships:
#     if itterable <= 0:
#         break
#     print('')
#     print('---')
#     print([s.position for s in combat.ally_ships])
#     print([s.position for s in combat.axes_ships])

#     print([s.hull_points for s in combat.ally_ships])
#     print([s.hull_points for s in combat.axes_ships])
#     combat.move_ships(percent_of_day_progressed=0.1)
#     combat.day_elapsed += day_percent
#     combat.assign_targets()
#     combat.exchange_blasts()
#     itterable -= 1

# print(f"Time elapsed: {float(int(combat.day_elapsed * 100) / 100)} days")
# for ship in combat.ally_ships:
#     print('')
#     print(ship)
#     # print(ship.position)
#     # print(ship.hull_points)
#     # print(ship.armor_points)
#     # print(ship.shield_points)


# for ship in combat.axes_ships:
#     print('')
#     print(ship)
#     # print(ship.position)
#     # print(ship.hull_points)
#     # print(ship.armor_points)
#     # print(ship.shield_points)

