import argparse
import time

starttime = time.time()

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
"RM,Iron Ore,IR,HIO,0.5",
"RM,Copper Ore,CR,HCO,0.5",
"RM,Stone,ST,HST,0.5",
"RM,Wood,WD,HWO,0.5",
"RM,Coal,CB,HCB,0.5",
"RF,Crude Oil,HPO,HWO,0.5",

"IT,Iron Plates,IPL,F,3.2,IR:1",
"IT,Copper Plates,CPL,F,3.2,CR:1",

"IT,Gears,GER,CARBG,0.5,IPL:2",
"IT,Pipes,PIP,CARBG,0.5,IPL:1",

"IT,Coil,COI,CARBG,0.5,CPL:0.5",
"IT,Yellow Belt,YBT,CARBG,0.5,IPL:0.5,GER:0.5",
"IT,Green Circuits,GCI,CARBG,0.5,IPL:1,COI:1",

"IT,Offshore Pump,OFP,CARBG,0.5,GER:1,PIP:1,GCI:2",
"IT,Stone Furnace,STF,CARBG,0.5,ST:5",
"IT,Boiler,BOL,CARBG,0.5,PIP:4,STF:1",
"IT,Steam Engine,SEG,CARBG,0.5,IPL:10,GER:8,PIP:5",
"IT,Small Power Pole,SPP,CARBG,0.5,WD:1,CPL:1",

"IT,Lab,LAB,CARBG,2,YBT:4,GER:10,GCI:10",
"IT,Red Science,RSI,CARBG,5,CPL:1,GER:1",
"IT,Automation Research,ATRS,LAB,10,RSI:10,OFP:1,BOL:1,SEG:1,SPP:1,LAB:1",

"IT,Assembler 1 Red,AS1,CARBG,IPL:9,GER:5,GCI:3"
]

rulesj = {
"Iron Ore":{"rtyp":"RawMat","time":"0.5","Abr":"IRO","harvest":"Iron Ore Patch","method":"Person,Miner"},
"Copper Ore":{"rtyp":"RawMat","Time":"0.5","Abr":"CPO","harvest":"Copper Ore Patch","method":"Person,Miner"},
"Stone":{"rtyp":"RawMat","Time":"0.5","Abr":"CPO","harvest":"Stone Patch","method":"Person,Miner"},
"Wood":{"rtyp":"RawMat","Time":"0.5","Abr":"WOD","harvest":"Woods","method":"Person"},
"Coal":{"rtyp":"RawMat","Time":"0.5","Abr":"COL","harvest":"Coal Patch","method":"Person,Miner"},
"Oil":{"rtyp":"RawFluid","Time":"0.5","Abr":"OIL","harvest":"Oil Patch","method":"Oil Pump"},
}



print(f"Lazy Bastard - there are {len(rules)} rules")
