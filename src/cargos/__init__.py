registered_cargos = []
# keep these alphabetised for ease of maintaining
from cargos import acid
from cargos import aggregates
from cargos import alcohol
from cargos import aluminia
from cargos import aluminium
from cargos import ammonia
from cargos import bauxite
from cargos import beans
from cargos import building_materials
from cargos import carbon_black
from cargos import cassava
from cargos import cast_iron
from cargos import cement
from cargos import chemicals
from cargos import chlorine
from cargos import chromite_ore
from cargos import clay
from cargos import cleaning_agents
from cargos import coal
from cargos import coal_tar
from cargos import coffee
from cargos import coke
from cargos import copper
from cargos import copper_concentrate
from cargos import copper_ore
from cargos import cranes_and_hoists
from cargos import diamonds
from cargos import edible_oil
from cargos import elastomer_products
from cargos import electrical_parts
from cargos import engineering_supplies
from cargos import explosives
from cargos import farm_supplies
from cargos import ferroalloys
from cargos import fertiliser
from cargos import fish
from cargos import food
from cargos import food_additives
from cargos import forgings_and_castings
from cargos import formic_acid
from cargos import fruits
from cargos import glass
from cargos import goods
from cargos import grain
from cargos import hardware
from cargos import hydrochloric_acid
from cargos import iron_ore
from cargos import kaolin
from cargos import lifting_equipment
from cargos import livestock
from cargos import limestone
from cargos import logs
from cargos import lye
from cargos import mail
from cargos import maize
from cargos import manganese
from cargos import methanol
from cargos import milk
from cargos import naphtha
from cargos import nickel
from cargos import nitrates
from cargos import nitrogen
from cargos import nuts
from cargos import oil
from cargos import oxygen
from cargos import packaging
from cargos import paints_and_coatings
from cargos import paper
from cargos import passengers
from cargos import peat
from cargos import petrol
from cargos import phosphate
from cargos import phosphoric_acid
from cargos import pig_iron
from cargos import pipework
from cargos import plastics
from cargos import potash
from cargos import concrete_products
from cargos import pumps_and_valves
from cargos import pyrite_ore
from cargos import quicklime
from cargos import raw_latex
from cargos import rebar
from cargos import recyclables
from cargos import rubber
from cargos import sand
from cargos import salt
from cargos import scrap_metal
from cargos import slag
from cargos import soda_ash
from cargos import steel
from cargos import steel_billets_and_blooms
from cargos import steel_ingots
from cargos import steel_merchant_bar
from cargos import steel_pipe
from cargos import steel_sections
from cargos import steel_sheet
from cargos import steel_slab
from cargos import steel_tube
from cargos import steel_wire_rod
from cargos import steel_wire_rope
from cargos import sulphur
from cargos import sulphuric_acid
from cargos import timber
from cargos import tin
from cargos import tinplate
from cargos import tyre_cord
from cargos import tyres
from cargos import vehicle_bodies
from cargos import vehicle_engines
from cargos import vehicle_parts
from cargos import vehicles
from cargos import welding_consumables
from cargos import wool
from cargos import yarn
from cargos import zinc

acid.cargo.register()
aggregates.cargo.register()
alcohol.cargo.register()
# UNUSED aluminia.cargo.register()
aluminium.cargo.register()
ammonia.cargo.register()
# UNUSED bauxite.cargo.register()
beans.cargo.register()
building_materials.cargo.register()
carbon_black.cargo.register()
cassava.cargo.register()
cast_iron.cargo.register()
cement.cargo.register()
chemicals.cargo.register()
chlorine.cargo.register()
# IAHC chromite_ore.cargo.register()
clay.cargo.register()
cleaning_agents.cargo.register()
coal.cargo.register()
coal_tar.cargo.register()
coffee.cargo.register()
coke.cargo.register()
copper.cargo.register()
# IAHC copper_concentrate.cargo.register()
copper_ore.cargo.register()
cranes_and_hoists.cargo.register()
diamonds.cargo.register()
edible_oil.cargo.register()
elastomer_products.cargo.register()
electrical_parts.cargo.register()
engineering_supplies.cargo.register()
explosives.cargo.register()
farm_supplies.cargo.register()
ferroalloys.cargo.register()
fertiliser.cargo.register()
fish.cargo.register()
food.cargo.register()
forgings_and_castings.cargo.register()
# BLTC food_additives.cargo.register()
# IAHC formic_acid.cargo.register()
fruits.cargo.register()
glass.cargo.register()
goods.cargo.register()
grain.cargo.register()
# BLTC hydrochloric_acid.cargo.register()
hardware.cargo.register()
iron_ore.cargo.register()
kaolin.cargo.register()
lifting_equipment.cargo.register()
livestock.cargo.register()
limestone.cargo.register()
logs.cargo.register()
lye.cargo.register()
mail.cargo.register()
maize.cargo.register()
manganese.cargo.register()
# UNUSED methanol.cargo.register()
milk.cargo.register()
# BLTC naphtha.cargo.register()
# UNUSED nickel.cargo.register()
nitrates.cargo.register()
nitrogen.cargo.register()
nuts.cargo.register()
oil.cargo.register()
oxygen.cargo.register()
# BLTC packaging.cargo.register()
paints_and_coatings.cargo.register()
paper.cargo.register()
passengers.cargo.register()
peat.cargo.register()
petrol.cargo.register()
phosphate.cargo.register()
# BLTC phosphoric_acid.cargo.register()
pig_iron.cargo.register()
pipework.cargo.register()
plastics.cargo.register()
potash.cargo.register()
concrete_products.cargo.register()
pumps_and_valves.cargo.register()
pyrite_ore.cargo.register()
quicklime.cargo.register()
# IAHC raw_latex.cargo.register()
rebar.cargo.register()
# UNUSED recyclables.cargo.register()
rubber.cargo.register()
sand.cargo.register()
salt.cargo.register()
scrap_metal.cargo.register()
slag.cargo.register()
soda_ash.cargo.register()
steel.cargo.register()
steel_billets_and_blooms.cargo.register()
steel_ingots.cargo.register()
steel_merchant_bar.cargo.register()
steel_pipe.cargo.register()
steel_sections.cargo.register()
steel_sheet.cargo.register()
steel_slab.cargo.register()
steel_tube.cargo.register()
steel_wire_rod.cargo.register()
steel_wire_rope.cargo.register()
sulphur.cargo.register()
# BLTC sulphuric_acid.cargo.register()
timber.cargo.register()
# BLTC tin.cargo.register()
# BLTC tinplate.cargo.register()
tyre_cord.cargo.register()
tyres.cargo.register()
vehicle_bodies.cargo.register()
vehicle_engines.cargo.register()
vehicle_parts.cargo.register()
vehicles.cargo.register()
welding_consumables.cargo.register()
wool.cargo.register()
# IAHC yarn.cargo.register()
zinc.cargo.register()
