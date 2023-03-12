import random

#MERCHANT ADVENTURE

#Merchant Map
#To make it to each location, a merchant must have gold or roll well.
#Each location has a market, which has a given economic state and a cost to leave
#If the merchant fails to pay the cost, he can roll skill against the cost to leave
#Failure here is death. See how far the merchant can go!

#Collection of Towns
#Name / Base Market / Cost to Leave / Skill Check / Description
#Hatterston / +5 / 20 / +2 
townList = [{
    "name": "Hatterston",
    "market": 5,
    "leaveCost": 20,
    "hazardCheck": 2
},
#Purple Ridge City / +8 / 30 / +5
{
    "name": "Purple Ridge City",
    "market": 8,
    "leaveCost": 30,
    "hazardCheck": 5
},
#Burgsbergs / +0 / 20 / -2
{
    "name": "Burgsbergs",
    "market": 0,
    "leaveCost": 20,
    "hazardCheck": -2
},
#Hatanniland / -2 / 30 / -4
{
    "name": "Hatanniland",
    "market": -2,
    "leaveCost": 30,
    "hazardCheck": -4
},
#Fallen Pine Township / -5 / 40 / -2
{
    "name": "Fallen Pine Township",
    "market": -5,
    "leaveCost": 40,
    "hazardCheck": -2
},
#Pextorantal / +0 / 30 / +0
{
    "name": "Pextorantal",
    "market": 0,
    "leaveCost": 30,
    "hazardCheck": 0
},
#Silent Rapids / -5 / 40 / +5
{
    "name": "Silent Rapids",
    "market": -5,
    "leaveCost": 40,
    "hazardCheck": 5
},
#Caninus Megacity 21 / -6 / 40 / +5
{
    "name": "Caninus Megacity 21",
    "market": -6,
    "leaveCost": 40,
    "hazardCheck": 5
},
#Tansho-Nagashi City / -10 / 60 / +0
{
    "name": "Tansho-Nagashi City",
    "market": -10,
    "leaveCost": 60,
    "hazardCheck": 0
},
#Fooksalot / 0 / 50 / +2
{
    "name": "Fooksalot",
    "market": 0,
    "leaveCost": 50,
    "hazardCheck": +2
}]

#Merchant Stats:
#Gold on Hand / Sell Skill / Hazard Skill
player = {
    "gold": 0,
    "sell": 0,
    "hazard": 0,
}

def levelUp(skill):
    player[skill] = player[skill] + 1


#Sell Skill rolls against initial sales / Increases with Good Sales
#Hazard Skill rolls against skill to leave / Increases with Successful Hazard Checks

#Base Mechanics
#1d20 roll under
def d20roll():
    return random.randint(1,21)

def d6roll():
    return random.randint(1,7)

def threeD6roll():
    return d6roll() + d6roll() + d6roll()

#Core Game Loop: 
#Merchant Generated (roll 3d6 for Sell and Hazard Skills)
print("Welcome to Merchant Adventure!\n Creating Merchant...")

player["sell"] = threeD6roll()
player["hazard"] = threeD6roll()
player["gold"] = threeD6roll()

print("Merchant Created! Onward to gold and glory!")

def statusPrint():
    statMessage = "Merchant Status:\n Gold: {} Sell Skill: {} Hazard Skill: {}"
    print(statMessage.format(player["gold"],player["sell"],player["hazard"]))

statusPrint()


#Merchant Visits first town

def travelLoop():
    for i in range(len(townList)):
        townName = townList[i]["name"]
        leaveCost = townList[i]["leaveCost"]

        statusPrint()
        print("\nWelcome to {}!".format(townName))
        tradeMod = economyGeneration(townList[i]) + player["sell"]
        salesCycle(tradeMod,townName)
        print("Leaving {}...".format(townName))
        print("The merchant seeks to hire security on the way out of town...")
        if(player["gold"] >= townList[i]["leaveCost"]):
            player["gold"] = player["gold"] - leaveCost
            print("The Merchant parts with {} gold for the security of mercenaries.".format(leaveCost))
        else:
            print("Unable to afford {} gold for mercenary fees, the Merchant strikes out alone.".format(leaveCost))
            hazardPass = hazardCheck(townName, townList[i]["hazardCheck"])
            if(hazardPass):
                print("With victory secured, the merchant continues onward!\n")
            else:
                print("End of Game.")
                break

    statusPrint()
    print("END OF PROGRAM")

#Economy generated

def economyGeneration(town):
    baseEcon = town["market"]

    econTable = {
        1:"Bust",
        2:"Normal",
        3:"Boom"
    }

    result = econTable.get(random.randint(1,4))

    if(result == "Bust"):
        print("Bust Economy Reported at this location.")
        return baseEcon - 8
    elif(result == "Normal"):
        print("Normal Economy At Current Market.")
        return baseEcon
    elif(result == "Boom"):
        print("Boom Economy Reported at Current Location.")
        return baseEcon + 8
    
    print("Normal Economy, it seems.")
    return baseEcon

#Sales skill checks made (three rolls)

def salesCycle(saleTN, townName):
    print("Open for Business in the Market...")
    
    for i in range(1,3):
        print("Day {} of sales in {} market...".format(i, townName))
        result = d20roll()
        if(result > saleTN):
            earnings = threeD6roll() * d6roll()
            player["gold"] = player["gold"] + earnings
            print ("Success! {} gold earned.".format(earnings))
            levelUp("sell")
        else:
            player["gold"] = player["gold"] - d6roll()
            print ("Failure. Lost time, lost money.")
    
    print("Sales complete in {} market".format(townName))

#Success tallied, gold distributed
#Merchant leaves
#If sufficient gold, merchant is on the way to next town
#If insufficient gold, merchant has to fight! 

def hazardCheck(townName, hazardLevel):
    print("On the outskirts of {}, the merchant is attacked!".format(townName))
    result = d20roll()

    if(result <= hazardLevel):
        print("The merchant has successfully survived the onslaught!")
        levelUp("hazard")
        return True
    else:
        print("The merchant has fallen by the wayside.")
        return False

#If success, make it to next town
#If failure, dies. 
#If death or final success, display end screen and retry

travelLoop()