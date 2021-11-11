

# build rules
# HWO harvest in woods
# HST harvest in stone patch
# HIO harvest in Iron Ore patch
# HCO harvest in Copper Ore patch
# HCB harvest in Coal patch
# HPO harvest in Petroleam patch
# F forge in furnace
# C craft
# AR assemble in Red
# ARBY assemble in Red Blue or Yellow
# ABY assemble in Blue or Yellow

# Type, Full Name, Abrev, Creation, Time, Ingredients
# Type - RM Raw Material, IT Basic Item, F Fluid


rules = [
"RM,I,Iron Ore,IR,HIO,0.5",
"RM,I,Copper Ore,CR,HCO,0.5",
"RM,I,Stone,ST,HST,0.5",
"RM,I,Wood,WD,HWO,0.5",
"RM,I,Coal,CB,HCB,0.5",
"RM,F,Crude Oil,HPO,HWO,0.5",

"IT,I,Iron Plates,IPL,F,3.2,IR:1",
"IT,I,Copper Plates,CPL,F,3.2,CR:1",

"IT,I,Gears,GER,CARBG,0.5,IPL:2",
"IT,I,Pipes,PIP,CARBG,0.5,IPL:1",

"IT,I,Coil,COI,CARBG,0.5,CPL:0.5",
"IT,I,Yellow Belt,YBT,CARBG,0.5,IPL:0.5,GER:0.5",
"IT,I,Green Circuits,GCI,CARBG,0.5,IPL:1,COI:1",

"IT,I,Offshore Pump,OFP,CARBG,0.5,GER:1,PIP:1,GCI:2",
"IT,I,Stone Furnace,STF,CARBG,0.5,ST:5",
"IT,I,Boiler,BOL,CARBG,0.5,PIP:4,STF:1",
"IT,I,Steam Engine,SEG,CARBG,0.5,IPL:10,GER:8,PIP:5",
"IT,I,Small Power Pole,SPP,CARBG,0.5,WD:1,CPL:1",

"IT,I,Lab,LAB,CARBG,2,YBT:4,GER:10,GCI:10",
"IT,I,Red Science,RSI,CARBG,5,CPL:1,GER:1",
"IT,I,Automation Research,ATRS,LAB,10,RSI:10,OFP:1,BOL:1,SEG:1,SPP:1,LAB:1",

"IT,I,Assembler 1 Red,AS1,CARBG,IPL:9,GER:5,GCI:3"
]


print(f"Lazy Bastard - there are {len(rules)} rules")
