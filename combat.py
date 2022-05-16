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
        self.ally_ships_destroyed = None
        self.axes_ships_destroyed = None

        self.cost_limiter_combat_limit = None
        self.cost_limiter_build_time = None
        self.cost_limiter_cost_alloys = None
        self.cost_limiter_cost_crystals = None
        self.cost_limiter_cost_motes = None
        self.cost_limiter_cost_gasses = None
        self.cost_limiter_power_required = None

    def _ship_distance(self, ship1, ship2):
        """
        Calculate the distance between two ship objects
        """
        ranges = {ship1.position, ship2.position}
        return max(ranges) - min(ranges)

    def _ship_target_options(self, ship, targets):
        """
        From a ship's perspective of a list of ship objects, which ones are within range of the longest ranged gun?
        """
        target = targets[0]
        distance = self._ship_distance(ship, target)
        if distance > ship.max_range:
            return None
        return target

    def _sort_ship_list(self, ship_list):
        """
        Return a sorted list of ships based on closest to furthest in distance
        """
        ship_list.sort(key=return_calculated_ship_range)
        return ship_list

    def _find_ship_by_id(self, ship_id, ship_list):
        """
        Return a ship object based on the ship_id
        """
        for ship in ship_list:
            if ship.my_id == ship_id:
                return ship

    def _ship_movement(self, ship, enemy_swarm, percent_of_day_progressed):
        """
        Based on criteria, move the ship.
        If the ship does not have a target, set target to the average location of the enemy fleet
        If the target is further away than the resting distance, move based % of the day incremented
        If the target is closer than the resting distance, move a tenth of what it would have moved
        """
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

    def _string_width(self, value, length, fill=' '):
        """
        This is for display purposes. It sets a string to a lenght by filling it in
        """
        while len(value) < length:
            value += fill
        return value[0:length]

    def _float_sizer(self, number, sig_figs):
        num = str(number).split('.')
        num[1] = num[1][:sig_figs]
        return float('.'.join(num))

    def start_fight(self):
        """
        Reset starting positions and destroyed lists of ships
        """
        for ship in self.ally_ships:
            ship.position = -self.starting_range
        for ship in self.axes_ships:
            ship.position = self.starting_range
        self.ally_ships_destroyed = []
        self.axes_ships_destroyed = []

    def assign_targets(self):
        """
        Select a target based on criteria
        Select the closest ship that isnt targeted already
        If all are already targeted, reset the targets list and pick one
        If there are no targets in range, do nothing
        """
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
        """
        For every gun that can fire, fire at the target
        Then reset the gun reload timer
        """
        self.ally_ships.sort(key=return_calculated_ship_range)
        self.axes_ships.sort(key=return_calculated_ship_range)
        for ship in self.ally_ships:
            target = self._find_ship_by_id(ship.target_id, self.axes_ships)
            if target:
                distance = self._ship_distance(ship, target)
                for turret in ship.turrets:
                    if turret.weapon is None:
                        continue
                    # print(turret.weapon.time_until_next_fire)
                    if turret.weapon.time_until_next_fire > 0:
                        continue
                    if turret.weapon.range is None or turret.weapon.range >= distance:
                        shield, armor, hull = turret.weapon.fire(target)
                        target.shield_points = shield
                        target.armor_points = armor
                        target.hull_points = hull

        for ship in self.axes_ships:
            target = self._find_ship_by_id(ship.target_id, self.ally_ships)
            if target:
                distance = self._ship_distance(ship, target)
                for turret in ship.turrets:
                    if turret.weapon is None:
                        continue
                    # print(turret.weapon.time_until_next_fire)
                    if turret.weapon.time_until_next_fire > 0:
                        continue
                    if turret.weapon.range is None or turret.weapon.range >= distance:
                        shield, armor, hull = turret.weapon.fire(target)
                        target.shield_points = shield
                        target.armor_points = armor
                        target.hull_points = hull

        for ally_ship in self.ally_ships.copy():
            if ally_ship.hull_points <= 0:
                self.ally_ships_destroyed.append(ally_ship)
                self.ally_ships.remove(ally_ship)

        for axes_ship in self.axes_ships.copy():
            if axes_ship.hull_points <= 0:
                self.axes_ships_destroyed.append(axes_ship)
                self.axes_ships.remove(axes_ship)

    def move_ships(self, percent_of_day_progressed=1):
        """
        Orchestrate each ship in a fleet's movements
        """
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
        """
        For each wepon on every ship, update the timer
        """
        for ship in self.ally_ships:
            for turret in ship.turrets:
                if turret.weapon is None:
                    continue
                turret.weapon.reduce_cooldown(time)

        for ship in self.axes_ships:
            for turret in ship.turrets:
                if turret.weapon is None:
                    continue
                turret.weapon.reduce_cooldown(time)

    def retro(self):
        """
        Return results from a battle
        """
        results = {
            'time': float(int(self.day_elapsed * 100) / 100),
            'living_ships': {
                'ally': copy.deepcopy(self.ally_ships),
                'axes': copy.deepcopy(self.axes_ships),
            },
            'destroyed_ships': {
                'ally': copy.deepcopy(self.ally_ships_destroyed),
                'axes': copy.deepcopy(self.axes_ships_destroyed),
            },
            'hull': {
                'ally_starting': [],
                'ally_ending': [],
                'axes_starting': [],
                'axes_ending': [],
                'total_ally_starting': 0,
                'total_ally_ending': 0,
                'total_axes_starting': 0,
                'total_axes_ending': 0,
                'total_ally_loss': 0,
                'total_axes_loss': 0,
            }
        }

        # Ship hull damage
        results['hull']['ally_starting'].extend([s.default_hull_points for s in self.ally_ships])
        results['hull']['ally_starting'].extend([s.default_hull_points for s in self.ally_ships_destroyed])
        results['hull']['axes_starting'].extend([s.default_hull_points for s in self.axes_ships])
        results['hull']['axes_starting'].extend([s.default_hull_points for s in self.axes_ships_destroyed])
        results['hull']['ally_ending'].extend([s.hull_points for s in self.ally_ships])
        results['hull']['ally_ending'].extend([s.hull_points for s in self.ally_ships_destroyed])
        results['hull']['axes_ending'].extend([s.hull_points for s in self.axes_ships])
        results['hull']['axes_ending'].extend([s.hull_points for s in self.axes_ships_destroyed])

        results['hull']['total_ally_starting'] = sum(results['hull']['ally_starting'])
        results['hull']['total_ally_ending'] = sum(results['hull']['ally_ending'])
        results['hull']['total_axes_starting'] = sum(results['hull']['axes_starting'])
        results['hull']['total_axes_ending'] = sum(results['hull']['axes_ending'])

        results['hull']['total_ally_loss'] = results['hull']['total_ally_starting'] - results['hull']['total_ally_ending']
        results['hull']['total_axes_loss'] = results['hull']['total_axes_starting'] - results['hull']['total_axes_ending']

        if len(self.ally_ships) > len(self.axes_ships):
            results['victory'] = True
        else:
            results['victory'] = False
        return results

    def commence_combat(self, day_percent=0.1):
        """
        Orchestrate a single battle
        """
        self.start_fight()
        while self.ally_ships and self.axes_ships:
            # if int(self.day_elapsed * 100) % 100 == 0:
            #     print(f"day: {int(self.day_elapsed * 100) / 100}")
            self.move_ships(percent_of_day_progressed=day_percent)
            self.update_weapons_cooldown(time=day_percent)
            self.day_elapsed += day_percent
            self.assign_targets()
            self.exchange_blasts()
            # print('')
            # print([s.position for s in self.ally_ships])
            # print([s.position for s in self.axes_ships])
        return self.retro()

    def iterative_battle(
        self,
        ally_list,
        axes_list,
        day_precet=0.1,
        iterations=10,
    ):
        """
        Orchestrate multiple battles
        """
        results = {
            'success_rate': None,
            # 'victory': None,
            'track_record': {},
        }
        track_record = []
        for index in range(iterations):
            self.ally_ships = copy.deepcopy(ally_list)
            self.axes_ships = copy.deepcopy(axes_list)

            result = self.commence_combat(day_percent=day_precet)

            results['track_record'][index] = result
            track_record.append(result['victory'])
        results['success_rate'] = len([1 for r in track_record if r]) / iterations
        return results

    def calculate_cost(self, ships):
        """
        Calculate the cost in resources of a fleet
        """
        combat_limit = 0
        build_time = 0
        cost_alloys = 0
        cost_crystals = 0
        cost_motes = 0
        cost_gasses = 0
        power_required = 0
        for ship in ships:
            combat_limit += ship.command_points if ship.command_points else 0
            # fleet_limit += ship.fleet_limit if ship.fleet_limit else 0
            build_time += ship.build_time if ship.build_time else 0
            cost_alloys += ship.cost_alloys if ship.cost_alloys else 0
            cost_crystals += ship.cost_crystals if ship.cost_crystals else 0
            cost_motes += ship.cost_motes if ship.cost_motes else 0
            cost_gasses += ship.cost_gasses if ship.cost_gasses else 0
            for turret in ship.turrets:
                if turret.weapon is None:
                    continue
                cost_alloys += turret.weapon.cost_alloys if turret.weapon.cost_alloys else 0
                cost_crystals += turret.weapon.cost_crystals if turret.weapon.cost_crystals else 0
                cost_motes += turret.weapon.cost_motes if turret.weapon.cost_motes else 0
                cost_gasses += turret.weapon.cost_gasses if turret.weapon.cost_gasses else 0
                power_required += turret.weapon.power_required if turret.weapon.power_required else 0
        response = {
            'combat_limit': combat_limit,
            'build_time': build_time,
            'cost_alloys': cost_alloys,
            'cost_crystals': cost_crystals,
            'cost_motes': cost_motes,
            'cost_gasses': cost_gasses,
            'power_required': power_required,
        }
        return response

    def fleet_too_expensive(
        self,
        combat_limit = None,
        build_time=None,
        cost_alloys=None,
        cost_crystals=None,
        cost_motes=None,
        cost_gasses=None,
        power_required=None,
        ships = None,
    ):
        """
        If the cost of a fleet is under the limit values return True
        else return False
        """

        if build_time is None:
            build_time = self.cost_limiter_build_time
        if cost_alloys is None:
            cost_alloys = self.cost_limiter_cost_alloys
        if cost_crystals is None:
            cost_crystals = self.cost_limiter_cost_crystals
        if cost_motes is None:
            cost_motes = self.cost_limiter_cost_motes
        if cost_gasses is None:
            cost_gasses = self.cost_limiter_cost_gasses

        if ships is None:
            ships = self.ally_ships

        fleet_cost = self.calculate_cost(ships)

        if build_time:
            if fleet_cost['build_time'] > build_time:
                return False
        if cost_alloys:
            if fleet_cost['cost_alloys'] > cost_alloys:
                return False
        if cost_crystals:
            if fleet_cost['cost_crystals'] > cost_crystals:
                return False
        if cost_motes:
            if fleet_cost['cost_motes'] > cost_motes:
                return False
        if cost_gasses:
            if fleet_cost['cost_gasses'] > cost_gasses:
                return False
        return True

    def assign_default_costs(
        self,
        combat_limit = None,
        build_time = None,
        cost_alloys = None,
        cost_crystals = None,
        cost_motes = None,
        cost_gasses = None,
    ):
        """
        Assign default costs
        """
        if combat_limit:
            self.cost_limiter_combat_limit = combat_limit
        if build_time:
            self.cost_limiter_build_time = build_time
        if cost_alloys:
            self.cost_limiter_cost_alloys = cost_alloys
        if cost_crystals:
            self.cost_limiter_cost_crystals = cost_crystals
        if cost_motes:
            self.cost_limiter_cost_motes = cost_motes
        if cost_gasses:
            self.cost_limiter_cost_gasses = cost_gasses

    def fill_fleet(self, ship, fleet, fleet_limit):
        """
        Keep adding ships until the fleet is full based on the resource limits
        """
        shadow_fleet = copy.deepcopy(fleet)
        expense = self.calculate_cost(fleet)
        # print(expense)
        if expense:
            while expense:
                # print('while loop iteration')
                shadow_fleet.append(copy.deepcopy(ship))
                expense = self.fleet_too_expensive(
                    ships=shadow_fleet,
                )
                
                # print(len(shadow_fleet))
                # # print(expense)

            fleet = shadow_fleet[:-1]

        # print(len(fleet))

        return fleet

    def iterativly_fill_fleet(self, ally_list, axes_list, fill_list, fleet_limit, attempt_count=10):
        """
        For each ship in fill_list, try a number of combats and return the results
        """
        for test_ship in fill_list:

            print('')
            print(f"Test ship: {test_ship}")

            test_ally_ships = self.fill_fleet(
                ship=test_ship,
                fleet=copy.deepcopy(ally_list),
                fleet_limit=100
            )
            test_axes_ships = copy.deepcopy(axes_list)

            for ship in test_ally_ships:
                ship.build()
            for ship in test_axes_ships:
                ship.build()

            # print(self.calculate_cost(test_ally_ships))
            # print(len(test_ally_ships))

            result = self.iterative_battle(
                ally_list=test_ally_ships,
                axes_list=test_axes_ships,
                day_precet=0.1,
                iterations=10,
            )
            # print(f"ally ships: {len(self.ally_ships)}, KIA: {len(self.ally_ships_destroyed)}")
            # print(f"axes ships: {len(self.axes_ships)}, KIA: {len(self.axes_ships_destroyed)}")
            ally_loss_list = [r['hull']['total_ally_loss'] for i, r in result['track_record'].items()]
            average_ally_loss = sum(ally_loss_list) / len(ally_loss_list)
            # print(f"average_ally_loss: {average_ally_loss}")
            axes_loss_list = [r['hull']['total_axes_loss'] for i, r in result['track_record'].items()]
            average_axes_loss = sum(axes_loss_list) / len(axes_loss_list)
            # print(f"average_axes_loss: {average_axes_loss}")
            percent_loss_success = average_ally_loss / average_axes_loss
            result['percent_loss_success'] = percent_loss_success
            # print(f"percent {percent_loss_success}")


            print(f"Victory Percentage: {self._float_sizer(result['success_rate'] * 100, 2)}%")
            print(f"Percent Loss Success Rate: {self._float_sizer(result['percent_loss_success'] * 100, 2)}%")
            # Percent cost to produce navies
            # Time to complete battles
            # self.show_results(result)
        

    # def find_domination_count(self):
        

    def show_results(self, results):
        """
        Display the results of many battles
        """
        print(results.keys())
        for index, record in results['track_record'].items():
            print('')
            print('')
            print(f"Trial: {index}")
            print(f"  Duration: {record['time']}")
            print(f"  Victory: {record['victory']}")

            table = []
            str_width = 10
            dead_space = '-'

            # print(range(max(len(record['living_ships']['ally']), len(record['living_ships']['axes']))))
            table.append('|'.join([self._string_width('ally', str_width), self._string_width('axes', str_width)]))

            # Survived
            for index in range(max(len(record['living_ships']['ally']), len(record['living_ships']['axes']))):
                try:
                    ally_ship = f"{record['living_ships']['ally'][index].__class__.__name__}"
                except:
                    ally_ship = dead_space
                try:
                    axes_ship = f"{record['living_ships']['axes'][index].__class__.__name__}"
                except:
                    axes_ship = dead_space
                ally_ship = self._string_width(ally_ship, str_width)
                axes_ship = self._string_width(axes_ship, str_width)
                table.append('|'.join([ally_ship, axes_ship]))
            table.append('')

            # Destroyed
            for index in range(max(len(record['destroyed_ships']['ally']), len(record['destroyed_ships']['axes']))):
                try:
                    ally_ship_d = f"D-{record['destroyed_ships']['ally'][index].__class__.__name__}"
                except:
                    ally_ship_d = dead_space
                try:
                    axes_ship_d = f"D-{record['destroyed_ships']['axes'][index].__class__.__name__}"
                except:
                    axes_ship_d = dead_space
                ally_ship_d = self._string_width(ally_ship_d, str_width)
                axes_ship_d = self._string_width(axes_ship_d, str_width)
                table.append('|'.join([ally_ship_d, axes_ship_d]))
            for line in table:
                print(line)
        print('')
        print('')
        print('Total Stats:')
        print(f"  Victory Rate: {results['success_rate']*100}%")



# for ship in 
        #     itteration_table = []
        #     if len(record['living_ships']['ally']) > len(record['living_ships']['axes']):
        #         difference = len(record['living_ships']['ally']) - len(record['living_ships']['axes'])
        #         diff_array = ['-' for i in range(difference)]
        #         record['living_ships']['axes'].extend(diff_array)
        #     elif len(record['living_ships']['ally']) < len(record['living_ships']['axes']):
        #         difference = len(record['living_ships']['axes']) - len(record['living_ships']['ally'])
        #         diff_array = ['-' for i in range(difference)]
        #         record['living_ships']['ally'].extend(diff_array)
        #     for ally_ship, axes_ship in zip(record['living_ships']['ally'], record['living_ships']['axes']):
        #         print(ally_ship, axes_ship)
        #     # print(record)
        # # for record in results['track_record']

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

cr = Cruiser()
cr.set_bow('artillery')
cr.set_core('artillery')
cr.set_stern('broadside')
cr.turrets[0].set_weapon('laser')
cr.turrets[1].set_weapon('mass_driver')
cr.turrets[2].set_weapon('laser')
cr.turrets[3].set_weapon('mass_driver')

cr2 = Cruiser()
cr2.set_bow('torpedo')
cr2.set_core('hangar')
cr2.set_stern('broadside')
cr2.turrets[0].set_weapon('laser')
cr2.turrets[1].set_weapon('normal_missle')
cr2.turrets[2].set_weapon('normal_missle')
cr2.turrets[3].set_weapon('flak_gun')
cr2.turrets[4].set_weapon('flak_gun')
cr2.turrets[5].set_weapon('regular_strike_craft')

# Ally composition
build_fleet(co, ally_ships, 1)
build_fleet(ds, ally_ships, 1)
build_fleet(cr2, ally_ships, 1)

# Axes composition
build_fleet(co, axes_ships, 10)
build_fleet(ds, axes_ships, 5)
build_fleet(cr, axes_ships, 1)

# for ship in ally_ships:
#     ship.build()
# for ship in axes_ships:
#     ship.build()

combat = Combat()
# combat.ally_ships = ally_ships
# combat.axes_ships = axes_ships

# results = combat.commence_combat()
# print(json.dumps(results, indent=2))

print('')
print('')
print('combat iterative test')
combat.assign_default_costs(
    build_time=None,
    cost_alloys=2000,
    cost_crystals=None,
    cost_motes=None,
    cost_gasses=None,
)
combat.iterativly_fill_fleet(
    ally_list=ally_ships,
    axes_list=axes_ships,
    fill_list=[
        co,
        ds,
        cr
    ],
    fleet_limit=100,
    attempt_count=10,
)


# if False:
#     # combat.ally_ships = ally_ships
#     # combat.axes_ships = axes_ships

#     combat.assign_default_costs(
#         build_time=None,
#         cost_alloys=2000,
#         cost_crystals=None,
#         cost_motes=None,
#         cost_gasses=None,
#     )

#     ally_ships = combat.fill_fleet(
#         ship=co,
#         fleet=ally_ships,
#         fleet_limit=100
#     )
#     # print(len(ally_ships))

#     # print(combat.calculate_cost(combat.ally_ships))
#     # for ship in ally_ships:
#     #     print(ship)

#     for ship in ally_ships:
#         ship.build()
#     for ship in axes_ships:
#         ship.build()


#     result = combat.iterative_battle(
#         ally_list=ally_ships,
#         axes_list=axes_ships,
#         day_precet=0.1,
#         iterations=10,
#     )
#     print(f"Victory Percentage: {result['success_rate'] * 100}%")
#     # combat.show_results(result)



#     print('exiting')
#     exit()
# else:
#     print('combat iterative test')
#     combat.assign_default_costs(
#         build_time=None,
#         cost_alloys=2000,
#         cost_crystals=None,
#         cost_motes=None,
#         cost_gasses=None,
#     )
#     combat.iterativly_fill_fleet(
#         ally_list=ally_ships,
#         axes_list=axes_ships,
#         fill_list=[
#             co,
#             ds
#         ],
#         fleet_limit=100,
#         attempt_count=5,
#     )
#     exit()


# result = combat.iterative_battle(
#     ally_list=ally_ships,
#     axes_list=axes_ships,
#     day_precet=0.1,
#     iterations=100,
# )
# combat.show_results(result)
# # print(result)

# # print(results[0])
# # print(results[1])

# # print(combat.__dict__)

# # print('')
# # print('')
# # print('')
# # combat.start_fight()

# # itterable = 5000000

# # day_percent = 0.1

# # while combat.ally_ships and combat.axes_ships:
# #     if itterable <= 0:
# #         break
# #     print('')
# #     print('---')
# #     print([s.position for s in combat.ally_ships])
# #     print([s.position for s in combat.axes_ships])

# #     print([s.hull_points for s in combat.ally_ships])
# #     print([s.hull_points for s in combat.axes_ships])
# #     combat.move_ships(percent_of_day_progressed=0.1)
# #     combat.day_elapsed += day_percent
# #     combat.assign_targets()
# #     combat.exchange_blasts()
# #     itterable -= 1

# # print(f"Time elapsed: {float(int(combat.day_elapsed * 100) / 100)} days")
# # for ship in combat.ally_ships:
# #     print('')
# #     print(ship)
# #     # print(ship.position)
# #     # print(ship.hull_points)
# #     # print(ship.armor_points)
# #     # print(ship.shield_points)


# # for ship in combat.axes_ships:
# #     print('')
# #     print(ship)
# #     # print(ship.position)
# #     # print(ship.hull_points)
# #     # print(ship.armor_points)
# #     # print(ship.shield_points)

# # )