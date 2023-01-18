from cgi import test
from empire_planner import *

# Jobs
job_clerk = Job('Clerk', trade_value=4, amenities=2)
job_researcher = Job('Researcher', research=4) # Requires 2 consumer goods per month
job_gas_extractor = Job('Gas Extractor', exotic_gasses=2)

# Buildings
building_planetary_administration = Building(
    name='System Admin building - Tier I', jobs=[], housing=5 , amenities=5
)
building_system_capital = Building(
    name='System Capital', jobs=[], housing=12 , amenities=12
)
building_habitat_capital = Building(
    name='Habitat Capital', jobs=[], housing=5 , amenities=5
)
building_research_lab_III = Building(
    name='Advanced Research Complex - Tier III', jobs=[job_researcher for _ in range(6)]
) # Requires 2 strategic resources per month
building_communal_housing = Building(
    name='Utopian Communal Housing - Tier II', jobs=[], housing=10, amenities=6
) # Requires 2 strategic resources per month
building_gas_extraction = Building(
    name='Gas extraction well - Tier II', jobs=[job_gas_extractor]
)

# Districts
district_colony = District(
    name='Colony', housing=5, jobs=[job_clerk]
)
district_habitat = District(
    name='Habitat', housing=8, jobs=[job_clerk, job_clerk]
)
district_ring = District(
    name='Ring World', housing=25, jobs=[job_clerk for _ in range(3)]
)
district_research = District(
    name='Habitat Research', housing=3, jobs=[job_researcher for _ in range(3)]
)
district_research_ring = District(
    name='Ring World Research', housing=10, jobs=[job_researcher for _ in range(10)]
)

markdown_text = [
    f"| Size | Planet | Habitat | Ring | Ascended | Empire size | Research | Research/Size |",
    f"| --- | --- | --- | --- | --- | --- | --- | --- |"
]

# markdown_text.append(f"| {} | {} | {} | {} | {} | {} | {} |")


# Smallest planet possible full science
test_col_1 = Colony(name='size 10 world Science full science')
test_col_1.add_district(district=district_colony, count=10)
test_col_1.add_building(building=building_system_capital)
test_col_1.add_building(building=building_research_lab_III, count=9)

pointer = test_col_1
pointer.population = pointer.required_population
aaa_required_population_1 = pointer.required_population
aaa_housing_1 = pointer.housing
aaa_dist_count_1 = len(pointer.districts)
aaa_build_count_1 = len(pointer.buildings)
aaa_sprawl_1 = pointer.sprawl
aaa_research_1 = pointer.research
aaa_research_to_sprawl_1 = pointer.research / pointer.sprawl
markdown_text.append(f"| 10 | X | - | - | - | {pointer.sprawl} | {pointer.research} | {pointer.sprawl} |")


# Largest planet possible full science
test_col_2 = Colony(name='size 25 world Science full science')
test_col_2.add_district(district=district_colony, count=25)
test_col_2.add_building(building=building_system_capital)
test_col_2.add_building(building=building_research_lab_III, count=11)

pointer = test_col_2
pointer.population = pointer.required_population
aaa_required_population_2 = pointer.required_population
aaa_housing_2 = pointer.housing
aaa_dist_count_2 = len(pointer.districts)
aaa_build_count_2 = len(pointer.buildings)
aaa_sprawl_2 = pointer.sprawl
aaa_research_2 = pointer.research
aaa_research_to_sprawl_2 = pointer.research / pointer.sprawl
markdown_text.append(f"| 25 | X | - | - | - | {pointer.sprawl} | {pointer.research} | {pointer.sprawl} |")


# Smallest habitat possible full science
test_col_3 = Colony(name='size 4 habitat Science full science', is_habitat=True)
test_col_3.add_district(district=district_habitat, count=4)
test_col_3.add_district(district=district_research, count=0)
test_col_3.add_building(building=building_habitat_capital)
# test_col_3.add_building(building=building_communal_housing, count=0)
test_col_3.add_building(building=building_research_lab_III, count=5)

pointer = test_col_3
pointer.population = pointer.required_population
aaa_required_population_3 = pointer.required_population
aaa_housing_3 = pointer.housing
aaa_dist_count_3 = len(pointer.districts)
aaa_build_count_3 = len(pointer.buildings)
aaa_sprawl_3 = pointer.sprawl
aaa_research_3 = pointer.research
aaa_research_to_sprawl_3 = pointer.research / pointer.sprawl
# 132 research all housing districts but still not actually enough housing
markdown_text.append(f"| 4 | - | X | - | - | {pointer.sprawl} | {pointer.research} | {pointer.sprawl} |")

# Largest habitat possible full science
test_col_4 = Colony(name='size 8 habitat Science full science', is_habitat=True)
test_col_4.add_district(district=district_habitat, count=8)
test_col_4.add_district(district=district_research, count=0)
test_col_4.add_building(building=building_habitat_capital)
# test_col_4.add_building(building=building_communal_housing, count=1)
test_col_4.add_building(building=building_research_lab_III, count=5)

pointer = test_col_4
pointer.population = pointer.required_population
aaa_required_population_4 = pointer.required_population
aaa_housing_4 = pointer.housing
aaa_dist_count_4 = len(pointer.districts)
aaa_build_count_4 = len(pointer.buildings)
aaa_sprawl_4 = pointer.sprawl
aaa_research_4 = pointer.research
aaa_research_to_sprawl_4 = pointer.research / pointer.sprawl
# 132 research all housing districts but still not actually enough housing
markdown_text.append(f"| 8 | - | X | - | - | {pointer.sprawl} | {pointer.research} | {pointer.sprawl} |")


# Smallest habitat possible full science and ascended
test_col_5 = Colony(name='size 4 habitat Science full science and ascended', is_habitat=True, ascension_level=3)
test_col_5.add_district(district=district_habitat, count=4)
test_col_5.add_district(district=district_research, count=0)
test_col_5.add_building(building=building_habitat_capital)
# test_col_5.add_building(building=building_communal_housing, count=0)
test_col_5.add_building(building=building_research_lab_III, count=5)

pointer = test_col_5
pointer.population = pointer.required_population
aaa_required_population_5 = pointer.required_population
aaa_housing_5 = pointer.housing
aaa_dist_count_5 = len(pointer.districts)
aaa_build_count_5 = len(pointer.buildings)
aaa_sprawl_5 = pointer.sprawl
aaa_research_5 = pointer.research
aaa_research_to_sprawl_5 = pointer.research / pointer.sprawl
# 120 research all housing districts but still not actually enough housing
# 96 research as many research districts as i can manage
markdown_text.append(f"| 4 | - | X | - | X | {pointer.sprawl} | {pointer.research} | {pointer.sprawl} |")

# Ring world segment
test_col_6 = Colony(name='Ring world segment', is_ring_world=True)
test_col_6.add_district(district=district_ring, count=3)
test_col_6.add_district(district=district_research_ring, count=7)
test_col_6.add_building(building=building_planetary_administration)
# test_col_6.add_building(building=building_communal_housing, count=0)
test_col_6.add_building(building=building_research_lab_III, count=11)

pointer = test_col_6
pointer.population = pointer.required_population
aaa_required_population_6 = pointer.required_population
aaa_housing_6 = pointer.housing
aaa_dist_count_6 = len(pointer.districts)
aaa_build_count_6 = len(pointer.buildings)
aaa_sprawl_6 = pointer.sprawl
aaa_research_6 = pointer.research
aaa_research_to_sprawl_6 = pointer.research / pointer.sprawl
# 120 research all housing districts but still not actually enough housing
# 96 research as many research districts as i can manage
markdown_text.append(f"| 10 | - | - | X | - | {pointer.sprawl} | {pointer.research} | {pointer.sprawl} |")

with open('city_results_tables.md', 'w') as mdf:
    for line in markdown_text:
        mdf.write(line + '\n')

x=1

"""
Habitat building count: So assuming not Voidborne -> 6. If voidborne -> 8 (still not including void dwellers)
You maths seems about right, ignoring the +1 building that Void Dwellers can get from their traditions:
2 Buildings - Capital
2 Buildings - Technologies
2 Buildings - Voidborne
1 Building - Functional Architecture
1 Building - Adaptability Tradition
"""

"""
You can construct a max of 10 segments on a ring section
So does that mean a total of 40 segments??
"""

exit()


# Jobs
job_clerk = Job('Clerk', trade_value=4, amenities=2)
job_technician = Job('Technician', energy=6)
job_miner = Job('Miner', minerals=6)
job_farmer = Job('Farmer', food=6)
job_researcher = Job('Researcher', research=4)
job_unity = Job('Unity', unity=4)
# job_amenities = Job('Amenities', amenities=)

# Districts
district_colony = District(
    name='Colony', housing=5, jobs=[job_clerk]
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

# Habitat districts
district_habitation = District(
    name='Habitat colony', housing=8, jobs=[job_clerk, job_clerk]
)
district_research = District(
    name='Research', housing=3, jobs=[job_researcher for _ in range(3)]
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











# dist1 = District(name='one')
# dist2 = District(name='two')

# x1 = Colony(name='1', districts=[district_colony])
# x2 = Colony(name='2', )

# print(x1, f"-{x1.name}-")
# print(x2, f"-{x2.name}-")
# print('---')
# print(x1.districts)
# print(x2.districts)
# print('---')
# print(x1.jobs)
# print(x2.jobs)

# x=1

sc = SprawlCalculator()
for _ in range(50):
    sc.add_system(system=System())

# COL1
col1 = Colony(name='Starter Colony')

col1.add_district(district=district_colony, count=6)
col1.add_district(district=district_generator, count=8)
col1.add_district(district=district_mining, count=8)

col1.add_building(building=building_system)
col1.add_building(building=building_energy_nexus, count=1)
col1.add_building(building=building_mineral_hub, count=1)
col1.add_building(building=building_unity, count=4)
col1.add_building(building=building_housing, count=1)
sc.add_colony(col1)


# COL2
col2 = Colony(name='Science Colony')

col2.add_district(district=district_colony, count=6)
col2.add_district(district=district_generator, count=10)
col2.add_district(district=district_mining, count=2)

col2.add_building(building=building_system)
col2.add_building(building=building_research, count=8)
sc.add_colony(col2)


# COL3
col3 = Colony(name='Mining Colony')

col3.add_district(district=district_colony, count=5)
col3.add_district(district=district_generator, count=1)
col3.add_district(district=district_mining, count=12)

col3.add_building(building=building_system)
col3.add_building(building=building_mineral_hub, count=1)
sc.add_colony(col3)


# COL4
col4 = Colony(name='Food Colony')

col4.add_district(district=district_colony, count=6)
col4.add_district(district=district_agriculture, count=15)

col4.add_building(building=building_system)
col4.add_building(building=building_food_center, count=1)
sc.add_colony(col4)


# jobs_lists = [
#     len(col1.jobs),
#     len(col2.jobs),
#     len(col3.jobs),
#     len(col4.jobs),
# ]

pointer = col4
aaa_required_population_1 = pointer.required_population
aaa_housing_1 = pointer.housing
aaa_dist_count_1 = len(pointer.districts)
aaa_build_count_1 = len(pointer.buildings)
aaa_sprawl_1 = pointer.sprawl
aaa_research_1 = pointer.research
sprl1 = sc.sprawl
sci1 = sc.research

x=1

# COL2
col5 = Colony(name='Science Habitat')

col5.add_district(district=district_habitation, count=1)
col5.add_district(district=district_research, count=3)

col5.add_building(building=building_system)
col5.add_building(building=building_research, count=2)
sc.add_colony(col5)

pointer = col5
aaa_required_population_2 = pointer.required_population
aaa_housing_2 = pointer.housing
aaa_dist_count_2 = len(pointer.districts)
aaa_build_count_2 = len(pointer.buildings)
aaa_sprawl_2 = pointer.sprawl
aaa_research_2 = pointer.research
sprl2 = sc.sprawl
sci2 = sc.research

x=1

# with open('current_sprawl_calculation_example.json', 'w') as df:
#     df.write(json.dumps(sc.put, indent=4))

# x=1
