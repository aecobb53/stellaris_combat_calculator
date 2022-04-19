import uuid
import copy
import random


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
        self.day = 0.0
        self.ally_ships = []
        self.axes_ships = []
        self.ally_ships_destroyed = []
        self.axes_ships_destroyed = []


    # def _sort_ships(self, ships_list):
    #     ships_list.sort(key=return_calculated_ship_range)
        

    def start_fight(self):
        iterable = 1
        for ship in self.ally_ships:
            ship.position = -self.starting_range + iterable
            iterable += 1
        for ship in self.axes_ships:
            ship.position = self.starting_range + iterable
            iterable += 1
        # max_range = 0
        # ships = []
        # ships.extend(self.ally_ships)
        # ships.extend(self.axes_ships)


        # self.ally_ships.sort(key=return_calculated_ship_range)
        # self.axes_ships.sort(key=return_calculated_ship_range)

        # # for ship in ships:
        # #     # print('')
        # #     # print(ship)
        # #     # print(ship.weapons)
        # #     for turret in ship.turrets:
        # #         weapon = turret.weapon
        # #         # print(turret, weapon)
        # #         if weapon:
        # #             # print(weapon.range)
        # #             max_range = max([max_range, weapon.range])
        # # print(self.ally_ships[-1].resting_range)
        # # print(self.axes_ships[-1].resting_range)
        # # print(max(self.ally_ships[-1].resting_range, self.axes_ships[-1].resting_range))
        # self.range = max(self.ally_ships[-1].resting_range, self.axes_ships[-1].resting_range)
        # self.day = 0.0

    def _ship_distance(self, ship1, ship2):
        print(ship1.position)
        print(ship2.position)
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

    def assign_targets(self):
        self.ally_ships.sort(key=return_calculated_ship_range)
        self.axes_ships.sort(key=return_calculated_ship_range)
        ally_list = []
        axes_list = []
        for ship in self.ally_ships:
            if not axes_list:
                axes_list = copy.deepcopy(self._sort_ship_list(self.axes_ships))
            if not ship.target_id:
                target = self._ship_target_options(ship, axes_list)
                if not target:
                    continue
                ship.target_id = target.my_id
                for target_ships in self.axes_ships:
                    if target_ships.my_id == target.my_id:
                        target_ships.targeted_by_ids.append(ship.my_id)
                axes_list.remove(target)

        for ship in self.axes_ships:
            if not ally_list:
                ally_list = copy.deepcopy(self._sort_ship_list(self.ally_ships))
            if not ship.target_id:
                target = self._ship_target_options(ship, ally_list)
                if not target:
                    continue
                ship.target_id = target.my_id
                for target_ships in self.ally_ships:
                    if target_ships.my_id == target.my_id:
                        target_ships.targeted_by_ids.append(ship.my_id)
                ally_list.remove(target)

    def exchange_blasts(self):
        self.ally_ships.sort(key=return_calculated_ship_range)
        self.axes_ships.sort(key=return_calculated_ship_range)
        ally_ships_in_round = []
        axes_ships_in_round = []
        for ship in self.ally_ships:
            target = self._find_ship_by_id(ship.target_id, self.axes_ships)
            if target:
                distance = self._ship_distance(ship, target)
                for turret in ship.turrets:
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
ds.turrets[0].set_weapon('laser')

build_fleet(co, ally_ships, 4)
build_fleet(ds, ally_ships, 2)
build_fleet(co, axes_ships, 1)
build_fleet(ds, axes_ships, 2)

for ship in ally_ships:
    ship.build()
for ship in axes_ships:
    ship.build()

combat = Combat()
combat.ally_ships = ally_ships
combat.axes_ships = axes_ships

# print('')
# print('')
# print(combat.ally_ships)
# # combat._sort_ships(combat.ally_ships)
# print(combat.ally_ships)
print('')
print('')
print('')
combat.start_fight()
combat.assign_targets()
# print(combat.range)
combat.exchange_blasts()

for ship in combat.ally_ships:
    print('')
    print(ship)
    print(ship.position)
    # print(ship.hull_points)
    # print(ship.armor_points)
    # print(ship.shield_points)


for ship in combat.axes_ships:
    print('')
    print(ship)
    print(ship.position)
    # print(ship.hull_points)
    # print(ship.armor_points)
    # print(ship.shield_points)

