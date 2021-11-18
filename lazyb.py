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


ruless = [
"RM,Iron Ore,IR,HIO,0.5",
"RM,Copper Ore,CR,HCO,0.5",
"RM,Stone,STO,HST,0.5",
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

rules = {
"Iron Ore":{"rtyp":"RawMat","T":0.5,"Ab":"IRO","harvest":"Iron Ore Patch","meth":"Craft,Miner"},
"Copper Ore":{"rtyp":"RawMat","T":0.5,"Ab":"CPO","harvest":"Copper Ore Patch","meth":"Craft,Miner"},
"Stone":{"rtyp":"RawMat","T":0.5,"Ab":"STO","harvest":"Stone Patch","meth":"Craft,Miner"},
"Wood":{"rtyp":"RawMat","T":0.5,"Ab":"WOD","harvest":"Woods","meth":"Craft"},
"Coal":{"rtyp":"RawMat","T":0.5,"Ab":"COL","harvest":"Coal Patch","meth":"Craft,Miner"},
"Oil":{"rtyp":"RawFluid","T":0.5,"Ab":"OIL","harvest":"Oil Patch","meth":"Oil Pump"},

"Iron Plates":{"rtyp":"Item","T":3.2,"Ab":"IPL","meth":"Furnace","Req":{"IRO":1}},
"Copper Plates":{"rtyp":"Item","T":3.2,"Ab":"CPL","meth":"Furnace","Req":{"CPO":1}},

"Gears":{"rtyp":"Item","T":0.5,"Ab":"GER","meth":"Craft,ARBG","Req":{"IPL":2}},
"Pipes":{"rtyp":"Item","T":0.5,"Ab":"PIP","meth":"Craft,ARBG","Req":{"IPL":1}},

"Coil":{"rtyp":"Item","T":0.5,"Ab":"COI","meth":"Craft,ARBG","Req":{"CPL":0.5}},
"Yellow Belt":{"rtyp":"Item","T":0.5,"Ab":"YBT","meth":"Craft,ARBG","Req":{"IPL":0.5,"GER":0.5}},
"Green Circuits":{"rtyp":"Item","T":0.5,"Ab":"GCI","meth":"Craft,ARBG","Req":{"IPL":1,"COI":1}},

"Offshore Pump":{"rtyp":"Item","T":0.5,"Ab":"OFP","meth":"Craft,ARBG","Req":{"GER":1,"PIP":1,"GCI":2}},
"Stone Furnace":{"rtyp":"Item","T":0.5,"Ab":"STF","meth":"Craft,ARBG","Req":{"STO":5}},
"Boiler":{"rtyp":"Item","T":0.5,"Ab":"BOL","meth":"Craft,ARBG","Req":{"PIP":4,"STF":1}},
"Steam Engine":{"rtyp":"Item","T":0.5,"Ab":"SEG","meth":"Craft,ARBG","Req":{"IPL":10,"GER":8,"PIP":5}},
"Small PowerPole":{"rtyp":"Item","T":0.5,"Ab":"SPP","meth":"Craft,ARBG","Req":{"WOD":1,"CPL":1}},

"Lab":{"rtyp":"Item","T":2,"Ab":"LAB","meth":"Craft,ARBG","Req":{"YBT":4,"GER":10,"GCI":10}},
"Red Science":{"rtyp":"Item","T":5,"Ab":"RSI","meth":"Craft,ARBG","Req":{"CPL":1,"GER":1}},
"Automation Research":{"rtyp":"Item","T":5,"Ab":"ATR","meth":"Lab","Req":{"RSI":1,"OFP":1,"BOL":1,"SEG":1,"SPP":1,"LAB":1}},

"Assembler 1":{"rtyp":"Item","T":5,"Ab":"AS1","meth":"Craft,ARBG","Req":{"IPL":9,"GER":5,"GCI":3}},
}

class RulingClass:

    abdict = {}

    def __init__(self):
        i = 0
        self.abdict = {}
        for itemname,rule in rules.items():
            ab = rule["Ab"]
            self.abdict[ab] = rule
            print(f"{i} {itemname} {ab} len:{len(self.abdict)}")
            i += 1

        # check requirements correctness
        nbad = 0
        nok = 0
        for itemname,rule in rules.items():
            rtyp = rule["rtyp"]
            if rtyp=="Item":
                req = rule["Req"]
                for reqab,reqquant in req.items():
                    if not reqab in self.abdict:
                        print(f"Error - bad abreviation {reqab} in rule {itemname}")
                        nbad += 1
                    else:
                        nok += 1
        print(f"Checked rule abreviations in reqs nok:{nok} nbad:{nbad}")



print(f"Lazy Bastard - there are {len(rules)} rules")

rc = RulingClass()


