
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
# ARBG assemble in Red Blue or Yellow
# ABG assemble in Blue or Yellow

# Type, Full Name, Abrev, Creation, Time, Ingredients
# Type - RM Raw Material, IT Basic Item, F Fluid




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
    methdict = {}
    namedict = {}
    reqlist = []

    def __init__(self):

        # make abreviation lookup dict
        i = 0
        self.abdict = {}
        self.methdict = {}
        self.namedict = {}
        for itemname,rule in rules.items():
            ab = rule["Ab"]
            self.abdict[ab] = rule
            self.namedict[ab] = itemname
            self.methdict[ab] = rule["meth"]
            rule["name"] = itemname
            print(f"{i} {itemname} {ab} rule:{rule}")
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
        self.reqlist.reverse()
        
    def rationalize_req_list(self):
        inventory = {}
        idx = 0
        for r in self.reqlist:
            itemtyp = r["Ab"]
            if itemtyp in inventory:
                inventory[itemtyp] += 1
            else:
                inventory[itemtyp] = 1
            if "Req" in r:
                req = r["Req"]
                for k in req:
                    if k not in inventory:
                        print(f"error on line {idx} creating {itemtyp} - {k} not in inventory")
                    else:
                       reqreq = req[k]
                       inventory[k] -= reqreq
                       if inventory[k]<0:
                          print(f"error on line {idx} creating {itemtyp} -  out of {k}")
                   
        print("Final Inventory")
        for k in inventory:
            v = inventory[k]
            print(f"  leftover {k} is {v}")
            

    def print_req_list(self):
        inventory = []
        idx = 0       
        for r in self.reqlist:
            color = bg('navy_blue') + fg('white')
            reset = attr('reset')
            if "Craft" in r["meth"]:
                color = bg('indian_red_1a') + fg('white')           
            idx += 1
            print(color,idx," ", r, reset)                

    def print_req_list_item_stats(self,make_item):
        item_stats = {}
        for r in self.reqlist:
            if r["rtyp"]=="Item":
                itemtyp = r["Ab"]
                if itemtyp in item_stats:
                    item_stats[itemtyp] += 1
                else:
                    item_stats[itemtyp] = 1
                    
        print(f"To make {make_item}")
        for k in item_stats: 
            v = item_stats[k]
            m = self.methdict[k]
            fn = self.namedict[k]
            print(f"   Need to {m} {v} of {k} - {fn}")
            
    def print_req_list_rawmat_stats(self,make_item):
        rawmat_stats = {}
        for r in self.reqlist:
            if r["rtyp"]=="RawMat":
                itemtyp = r["Ab"]
                if itemtyp in rawmat_stats:
                    rawmat_stats[itemtyp] += 1
                else:
                    rawmat_stats[itemtyp] = 1
                    
        print(f"To make {make_item}")
        for k in rawmat_stats: 
            v = rawmat_stats[k]
            print(f"   Need to mine {v} of {k}")            
            
    def print_req_list_cfw_stats(self,make_item):
        ncraft = 0
        nfurnace = 0
        nraw = 0    
        for r in self.reqlist:
            meth = r["meth"]
            if "Craft" in meth:
                ncraft += 1
            elif "Furnace" in meth:
                nfurnace += 1
            else:
                nraw += 1
            
        print(f"to make {makename} you need craft:{ncraft} furnace:{nfurnace} raw:{nraw}")

                    

print(f"Lazy Bastard - there are {len(rules)} rules")

rc = RulingClass()

makename = "AS1"
rc.make_req_list("AS1")
rc.print_req_list()
rc.rationalize_req_list()
rc.print_req_list_cfw_stats("AS1")
rc.print_req_list_rawmat_stats("AS1")
rc.print_req_list_item_stats("AS1")
