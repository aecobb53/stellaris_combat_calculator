

from os import system
# from turtle import color
from pydantic import BaseModel
from typing import Optional
from typing import List, Optional, Dict
import json


class Job:
    def __init__(
        self,
        name,
        energy=0,
        minerals=0,
        food=0,
        alloys=0,
        consumer_goods=0,
        exotic_gasses=0,
        rare_crystals=0,
        volatile_motes=0,
        zro=0,
        dark_matter=0,
        living_metal=0,
        nanites=0,
        influence=0,
        unity=0,
        research=0,
        amenities=0,
        trade_value=0,
    ):
        self.name = name
        self.energy = energy
        self.minerals = minerals
        self.food = food
        self.alloys = alloys
        self.consumer_goods = consumer_goods
        self.exotic_gasses = exotic_gasses
        self.rare_crystals = rare_crystals
        self.volatile_motes = volatile_motes
        self.zro = zro
        self.dark_matter = dark_matter
        self.living_metal = living_metal
        self.nanites = nanites
        self.influence = influence
        self.unity = unity
        self.research = research
        self.amenities = amenities
        self.trade_value = trade_value

    @property
    def put(self):
        output = {
            "name": self.name,
            "energy": self.energy,
            "minerals": self.minerals,
            "food": self.food,
            "alloys": self.alloys,
            "consumer_goods": self.consumer_goods,
            "exotic_gasses": self.exotic_gasses,
            "rare_crystals": self.rare_crystals,
            "volatile_motes": self.volatile_motes,
            "zro": self.zro,
            "dark_matter": self.dark_matter,
            "living_metal": self.living_metal,
            "nanites": self.nanites,
            "influence": self.influence,
            "unity": self.unity,
            "research": self.research,
            "amenities": self.amenities,
            "trade_value": self.trade_value,
        }
        return output

    @classmethod
    def build(cls, dct):
        obj = cls(
            name=dct.get('name'),
            energy=dct.get('energy'),
            minerals=dct.get('minerals'),
            food=dct.get('food'),
            alloys=dct.get('alloys'),
            consumer_goods=dct.get('consumer_goods'),
            exotic_gasses=dct.get('exotic_gasses'),
            rare_crystals=dct.get('rare_crystals'),
            volatile_motes=dct.get('volatile_motes'),
            zro=dct.get('zro'),
            dark_matter=dct.get('dark_matter'),
            living_metal=dct.get('living_metal'),
            nanites=dct.get('nanites'),
            influence=dct.get('influence'),
            unity=dct.get('unity'),
            research=dct.get('research'),
            amenities=dct.get('amenities'),
            trade_value=dct.get('trade_value'),
        )
        return obj




class Building:
    def __init__(
        self,
        name,
        jobs: List[Job] = [],
        housing=0,
        energy=0,
        minerals=0,
        food=0,
        alloys=0,
        consumer_goods=0,
        exotic_gasses=0,
        rare_crystals=0,
        volatile_motes=0,
        zro=0,
        dark_matter=0,
        living_metal=0,
        nanites=0,
        influence=0,
        unity=0,
        research=0,
        trade_value=0,
        amenities=0,
        energy_multiplier=0,
        minerals_multiplier=0,
        food_multiplier=0,
        alloys_multiplier=0,
        consumer_goods_multiplier=0,
        unity_multiplier=0,
        research_multiplier=0,
        trade_value_multiplier=0,
    ):
        self.name = name
        self.jobs = jobs
        self.housing = housing
        self.energy = energy
        self.minerals = minerals
        self.food = food
        self.alloys = alloys
        self.consumer_goods = consumer_goods
        self.exotic_gasses = exotic_gasses
        self.rare_crystals = rare_crystals
        self.volatile_motes = volatile_motes
        self.zro = zro
        self.dark_matter = dark_matter
        self.living_metal = living_metal
        self.nanites = nanites
        self.influence = influence
        self.unity = unity
        self.research = research
        self.trade_value = trade_value
        self.amenities = amenities
        self.energy_multiplier = energy_multiplier
        self.minerals_multiplier = minerals_multiplier
        self.food_multiplier = food_multiplier
        self.alloys_multiplier = alloys_multiplier
        self.consumer_goods_multiplier = consumer_goods_multiplier
        self.unity_multiplier = unity_multiplier
        self.research_multiplier = research_multiplier
        self.trade_value_multiplier = trade_value_multiplier

    @property
    def put(self):
        output = {
            "name": self.name,
            "jobs": [j.put for j in self.jobs],
            "housing": self.housing,
            "energy": self.energy,
            "minerals": self.minerals,
            "food": self.food,
            "alloys": self.alloys,
            "consumer_goods": self.consumer_goods,
            "exotic_gasses": self.exotic_gasses,
            "rare_crystals": self.rare_crystals,
            "volatile_motes": self.volatile_motes,
            "zro": self.zro,
            "dark_matter": self.dark_matter,
            "living_metal": self.living_metal,
            "nanites": self.nanites,
            "influence": self.influence,
            "unity": self.unity,
            "research": self.research,
            "trade_value": self.trade_value,
            "amenities": self.amenities,
            "energy_multiplier": self.energy_multiplier,
            "minerals_multiplier": self.minerals_multiplier,
            "food_multiplier": self.food_multiplier,
            "alloys_multiplier": self.alloys_multiplier,
            "consumer_goods_multiplier": self.consumer_goods_multiplier,
            "unity_multiplier": self.unity_multiplier,
            "research_multiplier": self.research_multiplier,
            "trade_value_multiplier": self.trade_value_multiplier,
        }
        return output

    @classmethod
    def build(cls, dct):
        obj = cls(
            name=dct.get('name'),
            jobs=[Job.build(j) for j in dct.get('jobs')],
            housing=dct.get('housing'),
            energy=dct.get('energy'),
            minerals=dct.get('minerals'),
            food=dct.get('food'),
            alloys=dct.get('alloys'),
            consumer_goods=dct.get('consumer_goods'),
            exotic_gasses=dct.get('exotic_gasses'),
            rare_crystals=dct.get('rare_crystals'),
            volatile_motes=dct.get('volatile_motes'),
            zro=dct.get('zro'),
            dark_matter=dct.get('dark_matter'),
            living_metal=dct.get('living_metal'),
            nanites=dct.get('nanites'),
            influence=dct.get('influence'),
            unity=dct.get('unity'),
            research=dct.get('research'),
            trade_value=dct.get('trade_value'),
            amenities=dct.get('amenities'),
            energy_multiplier=dct.get('energy_multiplier'),
            minerals_multiplier=dct.get('minerals_multiplier'),
            food_multiplier=dct.get('food_multiplier'),
            alloys_multiplier=dct.get('alloys_multiplier'),
            consumer_goods_multiplier=dct.get('consumer_goods_multiplier'),
            unity_multiplier=dct.get('unity_multiplier'),
            research_multiplier=dct.get('research_multiplier'),
            trade_value_multiplier=dct.get('trade_value_multiplier'),
        )


class District:
    def __init__(
        self,
        name: str,
        housing: int = 0,
        jobs: List[Job] = [],
    ):
        self.name = name
        self.housing = housing
        self.jobs = jobs

    @property
    def put(self):
        output = {
            "name": self.name,
            "housing": self.housing,
            "jobs": [j.put for j in self.jobs],
        }
        return output

    @classmethod
    def build(cls, dct):
        try:
            obj = cls(
                name=dct.get('name'),
                housing=dct.get('housing'),
                jobs=[Job.build(j) for j in dct.get('jobs', [])],
            )
        except Exception as e:
            e
        return obj

    def add_jobs(self, job: Job, count: int = 1):
        for _ in range(count):
            self.jobs.append(job)


class System:
    def __init__(
        self,
        energy=0,
        minerals=0,
        food=0,
        alloys=0,
        consumer_goods=0,
        exotic_gasses=0,
        rare_crystals=0,
        volatile_motes=0,
        zro=0,
        dark_matter=0,
        living_metal=0,
        nanites=0,
        unity=0,
        research=0,
        trade_value=0,
    ):
        self.energy = energy
        self.minerals = minerals
        self.food = food
        self.alloys = alloys
        self.consumer_goods = consumer_goods
        self.exotic_gasses = exotic_gasses
        self.rare_crystals = rare_crystals
        self.volatile_motes = volatile_motes
        self.zro = zro
        self.dark_matter = dark_matter
        self.living_metal = living_metal
        self.nanites = nanites
        self.unity = unity
        self.research = research
        self.trade_value = trade_value

    @property
    def put(self):
        output = {
            "energy": self.energy,
            "minerals": self.minerals,
            "food": self.food,
            "alloys": self.alloys,
            "consumer_goods": self.consumer_goods,
            "exotic_gasses": self.exotic_gasses,
            "rare_crystals": self.rare_crystals,
            "volatile_motes": self.volatile_motes,
            "zro": self.zro,
            "dark_matter": self.dark_matter,
            "living_metal": self.living_metal,
            "nanites": self.nanites,
            "unity": self.unity,
            "research": self.research,
            "trade_value": self.trade_value,
        }
        return output

    @classmethod
    def build(cls, dct):
        obj = cls(
            energy=dct.get('energy'),
            minerals=dct.get('minerals'),
            food=dct.get('food'),
            alloys=dct.get('alloys'),
            consumer_goods=dct.get('consumer_goods'),
            exotic_gasses=dct.get('exotic_gasses'),
            rare_crystals=dct.get('rare_crystals'),
            volatile_motes=dct.get('volatile_motes'),
            zro=dct.get('zro'),
            dark_matter=dct.get('dark_matter'),
            living_metal=dct.get('living_metal'),
            nanites=dct.get('nanites'),
            unity=dct.get('unity'),
            research=dct.get('research'),
            trade_value=dct.get('trade_value'),
        )
        return obj

    @property
    def sprawl(self):
        sprawl = 1
        return sprawl

class Colony:
    def __init__(
        self,
        name: str = '',
        population: int = 0,
        branch_offices: int = 0,
        districts: List[District] = [],
        buildings: List[Building] = [],
    ):
        self.name = name
        self.population = population
        self.branch_offices = branch_offices
        self.districts = districts
        self.buildings = buildings

    @property
    def put(self):
        x=1
        output = {
            "name": self.name,
            "population": self.population,
            "branch_offices": self.branch_offices,
            "districts": [d.put for d in self.districts],
            "buildings": [b.put for b in self.buildings],
        }
        return output

    @classmethod
    def build(cls, dct):
        obj = cls(
            name=dct.get('name'),
            population=dct.get('population'),
            branch_offices=dct.get('branch_offices'),
            districts=[District.build(d) for d in dct.get('districts')],
            buildings=[Building.build(b) for b in dct.get('buildings')],
        )
        return obj

    def add_district(self, district: District, count:int = 1):
        for _ in range(count):
            self.districts.append(district)

    def add_building(self, building: Building, count: int = 1):
        for _ in range(count):
            self.buildings.append(building)

    @property
    def sprawl(self):
        sprawl = 0
        sprawl += self.population # Population
        sprawl += 10 # Colony
        sprawl += len(self.districts) * .5 # Districts
        sprawl += self.branch_offices * 2 # Districts
        return sprawl

    @property
    def research(self):
        research = 0
        research_multiplier = 1
        for district in self.districts:
            research += district.research
        for building in self.buildings:
            research += building.research
            research_multiplier += building.research_multiplier
            for job in building.jobs:
                research += job.research
        return research * research_multiplier

    @property
    def jobs(self):
        jobs = []
        for district in self.districts:
            jobs.extend(district.jobs)
        for building in self.buildings:
            jobs.extend(building.jobs)
        return jobs

    @property
    def housing(self):
        housing = 0
        for district in self.districts:
            housing += district.housing
        for building in self.buildings:
            housing += building.housing
        return housing

    @property
    def required_population(self):
        return len(self.jobs)

    def add_building(self, building: Building, count=1):
        for _ in range(count):
            self.buildings.append(building)


class SprawlCalculator:
    def __init__(self, colonies: List[Colony] = [], systems: List[System] = []):
        self.colonies = colonies
        self.systems = systems

    def add_system(self, system: System):
        self.systems.append(system)

    def add_colony(self, colony: Colony):
        self.colonies.append(colony)

    @property
    def sprawl(self):
        sprawl = 0
        for system in self.systems:
            sprawl += system.sprawl
        for colony in self.colonies:
            sprawl += colony.sprawl
        return sprawl

    @property
    def relative_research(self):
        if self.sprawl < 100:
            return 1
        return 100 - self.sprawl * .001

    @property
    def relative_traditions(self):
        if self.sprawl < 100:
            return 1
        return 100 - self.sprawl * .002

    @property
    def research(self):
        research = 0
        for system in self.systems:
            research += system.research
        for colony in self.colonies:
            research += colony.research
        return int(research * self.relative_research)

    @property
    def put(self):
        output = {
            "colonies": [c.put for c in self.colonies],
            "systems": [s.put for s in self.systems],
        }
        return output

    @classmethod
    def build(cls, dct):
        obj = cls(
            colonies=[Colony.build(c) for c in dct.get('colonies')],
            systems=[System.build(s) for s in dct.get('systems')],
        )
        return obj



sc = SprawlCalculator()

for _ in range(50):
    sc.add_system(system=System())

# Jobs
job_clerk = Job('Clerk', trade_value=4, amenities=2)
job_technician = Job('Technician', energy=6)
job_miner = Job('Miner', minerals=6)
job_farmer = Job('Farmer', food=6)
job_researcher = Job('Researcher', research=4)
job_unity = Job('Unity', unity=4)
# job_amenities = Job('Amenities', amenities=)

# Districts
district_city = District(
    name='City', housing=5, jobs=[job_clerk]
)
district_generator = District(
    name='Generator', housing=2, jobs=[job_technician for _ in range(4)]
)
district_mining = District(
    name='Mining', housing=2, jobs=[job_miner for _ in range(4)]
)
district_agriculture = District(
    name='Agriculture', housing=2, jobs=[job_farmer for _ in range(4)]
)

# Buildings
building_system = Building(
    name='System', jobs=[], housing=12 , amenities=12
)
building_energy_nexus = Building(
    name='Energy Nexus', jobs=[job_technician for _ in range(2)]
)
building_mineral_hub = Building(
    name='Mineral Hub', jobs=[job_miner for _ in range(2)]
)
building_food_center = Building(
    name='Food Center', jobs=[job_farmer for _ in range(2)]
)
building_research = Building(
    name='Research', jobs=[job_researcher]
)
building_unity = Building(
    name='Unity', jobs=[job_unity]
)
building_housing = Building(
    name='Paradise Dome', housing=6, amenities=10
)




col1 = Colony(name='Starting Colony', branch_offices=0)

col1.add_district(district=district_city, count=6)
col1.add_district(district=district_generator, count=8)
col1.add_district(district=district_mining, count=8)

col1.add_building(building=building_system)
col1.add_building(building=building_energy_nexus, count=1)
col1.add_building(building=building_mineral_hub, count=1)
col1.add_building(building=building_unity, count=4)
col1.add_building(building=building_housing, count=1)

sc.add_colony(col1)

# J1 = col1.jobs
required_population = col1.required_population
housing = col1.housing
dist_count = len(col1.districts)
build_count = len(col1.buildings)

x=1

col2 = Colony(name='Science Colony', branch_offices=0)
x=1

# col2.add_district(district=district_city, count=6)
# col2.add_district(district=district_generator, count=6)
# col2.add_district(district=district_mining, count=6)

# col2.add_building(building=building_system)
# col2.add_building(building=building_research, count=6)
# col2.add_building(building=building_mineral_hub, count=1)
# col2.add_building(building=building_unity, count=4)
# col2.add_building(building=building_housing, count=1)

sc.add_colony(col2)

# J1 = col2.jobs
required_population = col2.required_population
housing = col2.housing
dist_count = len(col2.districts)
build_count = len(col2.buildings)

x=1



# # d_city = District(
# #     name='City District',
# #     housing=5,
# # )
# # d_generator = District(
# #     name='Generator District',
# #     housing=2,
# # )
# # d_generator.add_jobs(
# #     job=Job(
# #         name='Technician',
# #         energy=6,
# #     ),
# #     count=2
# # )

# col1.add_district(
#     district=d_city,
#     count=4
# )
# for _ in range(4):
#     col1.districts.append(District(
#         name='Generator District',
#         housing=2,
#         jobs=[Job(
#             name='Technician',
#             energy=6,
#         )]
#     ))

# x=1

# for _ in range(4):
#     col1.districts.append(District(
#         name='Mining District',
#         housing=2,
#         jobs=[Job(
#             name='Miner',
#             minerals=4,
#         )]
#     ))
# # Mining District
# # Agriculture District

# # Industrial District
# # Trade District



# c = Colony()
# c.add_building(
#     Building(
#         name='Imperial Palace',
#         jobs=[
#             Job(name='Research Director', research=6),
#             Job(name='Research Director', research=6),
#             Job(name='Research Director', research=6)
#         ]
#     )
# )
# c.add_building(
#     Building(
#         name='Research Institute',
#         jobs=[
#             Job(name='Research Director', research=6)
#         ],
#         research_multiplier=.15
#     )
# )
# c.add_building(
#     Building(
#         name='Advanced Research Complexes',
#         jobs=[
#             Job(name='Researcher', research=4),
#             Job(name='Researcher', research=4),
#             Job(name='Researcher', research=4),
#             Job(name='Researcher', research=4),
#             Job(name='Researcher', research=4),
#             Job(name='Researcher', research=4)
#         ]
#     )
# )


# for i in range(10):
#     sc.add_systems(System())

# sc.add_colony(c)

# s1 = sc.relative_research


# sc.add_colony(c)

# s2 = sc.relative_research


sprl = sc.sprawl
sci = sc.research

with open('current_sprawl_calculation_example.json', 'w') as df:
    df.write(json.dumps(sc.put, indent=4))

x=1
