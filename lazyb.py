
# flake8: noqa

from colored import fg, bg, attr
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

# 1st rule is - Raw Material, called Iron Ore, abbreviaion is IR, Harvested in Iron Ore Patch, needs 0.5 time, and no ingredients
# 7th rule is - Basic Item, called Iron Plates, abreviation is IPL, forged in Furnace, needs 3.2 secs and one ingrediant one Iron Ore (IR:1)

# ruless = [
# "RM,Iron Ore,IR,HIO,0.5",
# "RM,Copper Ore,CR,HCO,0.5",
# "RM,Stone,STO,HST,0.5",
# "RM,Wood,WD,HWO,0.5",
# "RM,Coal,CB,HCB,0.5",
# "RF,Crude Oil,HPO,HWO,0.5",

# "IT,Iron Plates,IPL,F,3.2,IR:1",
# "IT,Copper Plates,CPL,F,3.2,CR:1",

# "IT,Gears,GER,CARBG,0.5,IPL:2",
# "IT,Pipes,PIP,CARBG,0.5,IPL:1",

# "IT,Coil,COI,CARBG,0.5,CPL:0.5",
# "IT,Yellow Belt,YBT,CARBG,0.5,IPL:0.5,GER:0.5",
# "IT,Green Circuits,GCI,CARBG,0.5,IPL:1,COI:1",

# "IT,Offshore Pump,OFP,CARBG,0.5,GER:1,PIP:1,GCI:2",
# "IT,Stone Furnace,STF,CARBG,0.5,ST:5",
# "IT,Boiler,BOL,CARBG,0.5,PIP:4,STF:1",
# "IT,Steam Engine,SEG,CARBG,0.5,IPL:10,GER:8,PIP:5",
# "IT,Small Power Pole,SPP,CARBG,0.5,WD:1,CPL:1",

# "IT,Lab,LAB,CARBG,2,YBT:4,GER:10,GCI:10",
# "IT,Red Science,RSI,CARBG,5,CPL:1,GER:1",
# "IT,Automation Research,ATRS,LAB,10,RSI:10,OFP:1,BOL:1,SEG:1,SPP:1,LAB:1",

# "IT,Assembler 1 Red,AS1,CARBG,IPL:9,GER:5,GCI:3"
# ]

# 1st rule is - Iron Ore is a Raw Material, needs 0.5 time, abbreviaion is IRO, Harvested in Iron Ore Patch,and no ingredients
# 7th rule is - Iron Plates is an Item, needs 3.2 secs, abreviation is IPL,  method is forged in Furnace,  and one ingrediant one Iron Ore (IR:1)


rules = {
"Iron Ore":{"rtyp":"RawMat","T":0.5,"Ab":"IRO","harvest":"Iron Ore Patch","meth":"Harvest,Miner"},
"Copper Ore":{"rtyp":"RawMat","T":0.5,"Ab":"CPO","harvest":"Copper Ore Patch","meth":"Harvest,Miner"},
"Stone":{"rtyp":"RawMat","T":0.5,"Ab":"STO","harvest":"Stone Patch","meth":"Harvest,Miner"},
"Wood":{"rtyp":"RawMat","T":0.5,"Ab":"WOD","harvest":"Woods","meth":"Harvest"},
"Coal":{"rtyp":"RawMat","T":0.5,"Ab":"COL","harvest":"Coal Patch","meth":"Harvest,Miner"},
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
"Automation Research":{"rtyp":"Item","T":5,"Ab":"ATR","meth":"Lab","Req":{"RSI":10,"OFP":1,"BOL":1,"SEG":1,"SPP":1,"LAB":1}},

"Assembler 1":{"rtyp":"Item","T":5,"Ab":"AS1","meth":"Craft,ARBG","Req":{"IPL":9,"GER":5,"GCI":3,"ATR":1}},
}

class RulingClass:

    abdict = {}
    reqlist = []

    def __init__(self):

        # make abreviation lookup dict
        i = 0
        self.abdict = {}
        for itemname,rule in rules.items():
            ab = rule["Ab"]
            self.abdict[ab] = rule
            rule["name"] = itemname
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


    def add_rule_to_list(self,rule):
        self.reqlist.append(rule)
        if not "Req" in rule:
            # must be a raw material
            return
        req = rule["Req"]
        for reqab,reqquant in req.items():
            if not reqab in self.abdict:
                rulename = rule["name"]
                raise Exception(f"Error - bad abreviation {reqab} in rule {rulename}")
            reqrule = self.abdict[reqab]
            if reqquant==0.5:
                reqquant = 1
            for i in range(0,reqquant):
                self.add_rule_to_list(reqrule)

    def make_req_list(self, req:str):

        if not req in self.abdict:
            raise Exception("req not in abdict")

        start_rule = self.abdict[req]

        self.reqlist = []
        self.add_rule_to_list(start_rule)


print(f"Lazy Bastard - there are {len(rules)} rules")

rc = RulingClass()

makename = "AS1"
rc.make_req_list("AS1")

ncraft = 0
nfurnace = 0
nraw = 0
nironplate = 0
ncopperplate = 0
nironore = 0
ncopperore = 0
nstone = 0
idx = 0
for r in rc.reqlist:

    meth = r["meth"]
    if "Craft" in meth:
        ncraft += 1
    elif "Furnace" in meth:
        nfurnace += 1
    else:
        nraw += 1

    if r["rtyp"]=="Item":
        if r["Ab"]=="IPL":
            nironplate += 1
        if r["Ab"]=="CPL":
            ncopperplate += 1

    if r["rtyp"]=="RawMat":
        if r["Ab"]=="IRO":
            nironore += 1
        if r["Ab"]=="CPO":
            ncopperore += 1
        if r["Ab"]=="STO":
            nstone += 1            


    color = bg('navy_blue') + fg('white')
    reset = attr('reset')
    if "Craft" in r["meth"]:
        color = bg('indian_red_1a') + fg('white')
    
    idx += 1
    print(color,idx," ", r, reset)

print(f"to make {makename} you need craft:{ncraft} furnace:{nfurnace} raw:{nraw}")
print(f"to make {makename} you need iron-plate:{nironplate} copper-plate:{ncopperplate}")
print(f"to make {makename} you need iron-ore:{nironore} copper-ore:{ncopperore}  stone:{nstone}")


print(f"to make {makename} you need req_list_len:{len(rc.reqlist)}")
