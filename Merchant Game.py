import random
import json
from pathlib import Path, PureWindowsPath

#MERCHANT ADVENTURE

#Merchant Map
#To make it to each location, a merchant must have gold or roll well.
#Each location has a market, which has a given economic state and a cost to leave
#If the merchant fails to pay the cost, he can roll skill against the cost to leave
#Failure here is death. See how far the merchant can go!

filename = PureWindowsPath(".\Scenarios\MainCampaign.json")
fileReader = open(Path(filename),"r")
totalData = json.loads(fileReader.read())
townCollection = totalData["towns"]
encounterCollection = totalData["encounters"]
fileReader.close()

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
    return random.randint(1,20)

def d6roll():
    return random.randint(1,6)

def threeD6roll():
    return d6roll() + d6roll() + d6roll()

def statusPrint():
    statMessage = "Merchant Status:\n Gold: {} Sell Skill: {} Hazard Skill: {}"
    print(statMessage.format(player["gold"],player["sell"],player["hazard"]))

#Merchant Visits first town

def travelLoop():
    gameRunning = True
    currentTown = townCollection[townCollection["Start"]["connections"][0]]

    #Core Game Loop: 
    #Merchant Generated (roll 3d6 for Sell and Hazard Skills)
    print("Welcome to Merchant Adventure!\nCreating Merchant...")

    player["sell"] = threeD6roll()
    player["hazard"] = threeD6roll()
    player["gold"] = threeD6roll()

    print("Merchant Created! Onward to gold and glory!")


    while(gameRunning):
        
        townName = currentTown["name"]
        leaveCost = currentTown["leaveCost"]
        townHazard = currentTown["hazardCheck"]

        statusPrint()
        print("\nWelcome to {}!".format(townName))
        print(currentTown["townDescription"])
        ecoRoll = economyGeneration(currentTown)
        tradeMod = [ecoRoll[0] + player["sell"],ecoRoll[1],ecoRoll[2]]
        print(currentTown["marketDescription"] +"\n")
        salesCycle(tradeMod,townName)
        print("The Merchant believes it's time to move on. [{} Gold]".format(player["gold"]))
        
        if(currentTown["connections"] != "Finish"):
            nextTown = selectConnection(currentTown)
        else:
            nextTown = "Finish"
        
        print("Leaving {}...\n".format(townName))
        print("The merchant seeks to hire security on the way out of town...")
        if(player["gold"] >= leaveCost):
            player["gold"] = player["gold"] - leaveCost
            print("The Merchant parts with {} gold for the security of mercenaries.".format(leaveCost))
        else:
            print("Unable to afford {} gold for mercenary fees, the Merchant strikes out alone.".format(leaveCost))
            hazardPass = hazardCheck(currentTown, townHazard)
            if(hazardPass):
                print("With victory secured, the merchant continues onward!\n")
            else:
                print("End of Game.\n")
                gameRunning = False
        
        if(nextTown != "Finish"):        
            currentTown = townCollection[nextTown]
        else:
            gameRunning = False

    if(nextTown == "Finish"):
        print("Congratulations! The Merchant has made it through the season!")
    else:
        print("The Merchant has failed. Please try again.")

    
    statusPrint()

#Economy generated

def economyGeneration(town):
    baseEcon = town["market"]

    econTable = {
        1:"Bust",
        2:"Normal",
        3:"Boom"
    }

    result = econTable.get(random.randint(1,3))
    #result = econTable.get(3)

    if(result == "Bust"):
        print("Bust Economy Reported at this location.")
        return [baseEcon - 3,1,"Bust"]
    elif(result == "Normal"):
        print("Normal Economy At Current Market.")
        return [baseEcon,2,"Normal"]
    elif(result == "Boom"):
        print("Boom Economy Reported at Current Location.")
        return [baseEcon + 3,3,"Boom"]
    
    print("Normal Economy, it seems.")
    return [baseEcon,2,"Normal"]

#Sales skill checks made (three rolls)

def salesCycle(economy, townName):
    print("Open for Business in the Market!\n")
    encounter = [townName ,"End"]

    for i in range(1,economy[1]+1):
        print("Day {} of sales in {} market...".format(i, townName))
        result = d20roll()
        if(result <= economy[0]):
            earnings = threeD6roll() * d6roll()
            player["gold"] = player["gold"] + earnings
            print ("Success! {} gold earned. [{} Gold]".format(earnings,player["gold"]))
            levelUp("sell")
        else:
            player["gold"] = player["gold"] - d6roll()
            print ("Failure. Lost time, lost money. [{} Gold]".format(player["gold"]))
        
        #Check for random encounter
        entRoll = d20roll()
        if (entRoll >= 5):
            #Check to see if encounter is generic or specific
            if(10 <= d20roll()):
                encounter = randomEncounter(economy[2],i,encounter)
            else:
                encounter = ["Generic","End"]
                encounter = randomEncounter(economy[2],i,encounter)
    
    print("Sales complete in {} market.".format(townName))
def randomEncounter(economy, day, encounterState):
    #Determine if encounterState has been adjusted by previous encounters
    #If not, find possible starting encounters and roll for a random one
    #print("\nCurrent EncounterState: {}".format(encounterState))

    encounterKeys = encounterCollection[encounterState[0]].keys()
    townEncounters = encounterCollection[encounterState[0]]
    if(encounterState[1] == "End"):
        #Gather Possible encounters
        startKeys = []
        possibleEncounters = []

        for i in encounterKeys:
            if ("-" not in i):
                startKeys.append(i)

        for i in startKeys:
            if ((economy in townEncounters[i]["states"][0]) and (day in townEncounters[i]["states"][1])):
                possibleEncounters.append(townEncounters[i])
        
        #Select Random encounter and play it
        playResult = playEncounter(random.choice(possibleEncounters))
        encounterState = encounterEvent(playResult, encounterState[0])
        return encounterState

    #If so, continue to next state
    else:
        playResult = playEncounter(townEncounters[encounterState[1]])
        encounterState = encounterEvent(playResult, encounterState[0])
        return encounterState
    #If an encounter occurs, print the correct lines
    #Print the options and administer the consenquences

    #Return Encounter State

def playEncounter(encounter):
    print("\n{}\n".format(encounter["intro"]))

    optionKeyList = encounter["options"].keys()
    for i in optionKeyList:
        print("{}. {}".format(i, encounter["options"][i]["description"]))

    selectionMade = False
    while(selectionMade == False):
        try:
            select = input("Select Option: ")
        except ValueError:
            print("Invalid Selection")
        else:
            if(select in optionKeyList):
                selectionMade = True
                print("{} \n".format(encounter["options"][select]["response"]))
                return encounter["options"][select]["effects"]
            else:
                print("Invalid Selection.")
    
def encounterEvent(event, townName):
    #print("Encounter Event: {}".format(event))
    
    #Debit: Lose X amount of money
    if(event[0][0] == "Debit"):
        player["gold"] = player["gold"] - event[0][1]
        statusPrint()
        return [townName, event[1][0]]
    #Credit: Gain X amount of money
    elif(event[0][0] == "Credit"):
        statusPrint()
        player["gold"] = player["gold"] + event[0][1]
        return [townName, event[1][0]]
    #Chance: roll 1d20. Roll at or under the goal leads to option 1, Over leads to option 2
    elif(event[0][0] == "Chance"):
        roll = d20roll()
        if(roll <= event[0][1]):
            passResultLink = event[1][0]
            passEvent = encounterCollection[townName][passResultLink]
            return [townName, playEncounter(passEvent)[1][0]]
        else:
            failResultLink = event[1][1]
            failEvent = encounterCollection[townName][failResultLink] 
            return [townName, playEncounter(failEvent)[1][0]]
    #HSkillUp: Gain a level in the Hazard Skill
    elif(event[0][0] == "HSkillUp"):
        levelUp("hazard")
        return [townName, event[1][0]]
    #SSkillUp: Gain a level in the Sale skill
    elif(event[0][0] == "SSkillUp"):
        levelUp("sell")
        return [townName, event[1][0]]
    #None: End of Encounter Event
    elif(event[0][0] == "None"):
        return [townName, event[1][0]]

#Success tallied, gold distributed
#Merchant leaves
#If sufficient gold, merchant is on the way to next town
#If insufficient gold, merchant has to fight! 

def hazardCheck(town, hazardLevel):
    print("\nOn the outskirts of {}, the merchant is attacked!".format(town["name"]))
    print(town["hazardDescription"])
    result = d20roll()

    if(result <= hazardLevel):
        print("The merchant has successfully survived the onslaught!")
        levelUp("hazard")
        return True
    else:
        print("The merchant has fallen by the wayside.")
        return False

def selectConnection(town):
    validSelection = False
    tConnections = town["connections"]
    
    while(validSelection == False):
        print("\nAvailable connections are: ")
        for i in range(len(tConnections)):
            print("{}. {}".format(i+1,tConnections[i]))
        
        try:
            select = int(input("Select Next Town: "))
        except ValueError:
            print("Invalid Selection!")
        else:
            if (select in range(1,len(tConnections)+1)):
                result = tConnections[select-1]
                validSelection = True
            else:
                print("Please Select A Valid Town.") 
    
    return result


#If success, make it to next town
#If failure, dies. 
#If death or final success, display end screen and retry

gameRunning = True

while(gameRunning == True):    
    print("\nMerchant Adventure v0.3")
    print("Copyright 2023, Written By Jason Lee")
    print("An American Beef Productions Game\n")
    print("1. Start New Game")
    print("2. Exit Game.")
    
    try:
        selection = (int)(input("Make Selection: "))
    except ValueError:
        print("Invalid Selection.")
    else:
        if(selection == 1):
            travelLoop()
        elif(selection ==2):
            gameRunning = False
        else: 
            print("Invalid Selection.")
