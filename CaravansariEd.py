import json

stockTemplate = {
    "scenarioName": "",
    "filename": "",
    "towns":{
        "Start":{
            "connections":[""]
        }
    },
    "encounters":{
    
    }
}

townTemplate = {
    "TownName":{
        "name": "",
        "market": "",
        "leaveCost": "",
        "hazardCheck": "",
        "townDescription": "",
        "marketDescription": "",
        "hazardDescription": "",
        "connections": []
    }
}

encounterTemplate = {
    "EncounterNum": {
                #States: [[Economic States], [Days to Start On]]
                "states": [[],[]],
                "intro":"",
                "options": {
                    "1":{
                    "description": "",
                    "response": "",
                    "effects": [["",0],[""]]
                },
                    "2": {
                    "description": "",
                    "response": "",
                    "effects": [[""],[""]]
                    }
                },
            },
}

programRunning = True

#Main Menu
print("Welcome to the Caravanserai Editor for Merchant Adventure!")
print("Build v1")

print("Make your selection: ")
#Create New Scenario
print("1. Create New Scenario")
print("2. Edit Existing Scenario")
print("3. Exit Program")

def mainMenuSelector():
    print("Main Menu: ")
    print("1. Create New Scenario")
    print("2. Edit Existing Scenario")
    print("3. Exit Program")


    while(programRunning):
        try:
            selection = int(input("Enter Selection: "))
        except TypeError:
            print("Invalid Selection.")
        else:
            if (selection == 1):
                #Create New Scenario
                createScenarioMenu()
            elif (selection == 2):
                #Edit Existing Scenario
                editScenarioMenu()
            elif (selection == 3):
                programRunning = False
            else:
                print("Invalid Selection.")
    
    print ("END OF PROGRAM.")

def createScenarioMenu():
    #Load Stock Template
    #Create First Town
    newScenario = stockTemplate
    newScenario["scenarioName"] = input("Scenario Name: ")
    newScenario["filename"] = ("{}.json".format(input("Filename: ")))
    firstTown = createTown()
    newScenario["towns"][firstTown["name"]] = firstTown

    #Menu options for adding additional towns
    print("1. Create Additional Town.")
    print("2. Edit Existing Town")
    print("3. Add Random Encounter")
    print("4. Save Scenario")

    try:
        selection = (int)(input("Menu Selection: "))
    except ValueError:
        print("Invalid Selection.")
    else:
        if(selection == 1):
            newTown = createTown()
            newScenario["towns"][newTown["name"]] = newTown
        elif(selection == 2):
            town = townListSelector(newScenario)
            editTown(town)
        elif(selection == 3):
            #Selections for Adding Random Encounter
            print("To Be Implemented")
        elif(selection == 4):
            fileWriter = open(newScenario["filename"], "w")
            fileWriter.write(json.dumps(newScenario, indent=4))
            fileWriter.close()

def editScenarioMenu():
    #Load Scenario Menu
    #Edit Towns
    #-List Existing Towns
    #--Edit Towns
    editTown()
    #--Add New Towns
    createTown()
    #List Existing Encounters
    #-List By Towns
    #--Select Starting Encounter
    #---Select Follow On Encounter
    #--Add New Encounter to Existing Town

def createTown():
    newTown = townTemplate
    
    newTown["name"] = input("Enter Town Name: ")
    newTown["market"] = (int)(input("Enter Market Modifier: "))
    newTown["leaveCost"] = (int)(input("Enter Leave Cost: "))
    newTown["hazardCheck"] = (int)(input("Enter Hazard Check: "))
    newTown["townDescription"] = input("Enter Town Description: ")
    newTown["marketDescription"] = input("Enter Market Description: ")
    newTown["hazardDescription"] = input("Enter Hazard Desctiption: ")
    
    #TODO: Add method for adding connections, but default to "End"

    newTown["connections"] = ["End"]

    townDataPrinter(newTown)
    
    validSelect = False

    while(validSelect == False):
        selection = input("Accept? Y or N")
        if(selection[0].lower == 'y'):
            print("Town Saved to New Scenario.")
            validSelect = True
        elif(selection[0].lower == 'n'):
            print("Editing town...")
            editTown(newTown)
            validSelect = True
        else:
            print("Invalid Selection.")
        
def editTown(townData):
    townDataPrinter(townData)

    editingData = True

    while (editingData):
        print("EDITING MENU: ")
        print("1. Town Name")
        print("2. Market Modifier")
        print("3. Leave Cost")
        print("4. Hazard Check")
        print("5. Town Description")
        print("6. Market Description")
        print("7. Hazard Description")
        print("8. Return to Previous")
        
        try:
            selection = (int)(input("Select Data to Edit: "))
        except ValueError:
            print("Invalid Selection")
        else:
            if(selection == 1):
                townData["name"] = input("Current Town Name: {}\nNew Town Name: ".format(townData["name"]))
            elif(selection==2):
                townData["market"] = (int)(input("Current Market Modifier: {}\nNew Market Modifier: ".format(townData["market"])))
            elif(selection == 3):
                townData["leaveCost"] = (int)(input("Current Leave Cost: {}\nNew Leave Cost: ".format(townData["leaveCost"])))
            elif(selection == 4):
                townData["hazardCheck"] = (int)(input("Current Hazard Check: {}\nNew Hazard Check: ".format(townData["hazardCheck"])))
            elif(selection == 5):
                townData["townDescription"] = input("Current Town Description: {}\n New Town Description: ".format(townData["townDescription"]))
            elif(selection == 6):
                townData["marketDescription"] = input("Current Market Description: {}\n New Market Description: ".format(townData["marketDescription"]))
            elif(selection == 7):
                townData["hazardDescription"] = input("Current Hazard Desctiption: {}\n New Hazard Description: ".format(townData["hazardDescription"]))
            elif(selection == 8):
                print("Leaving Editing Menu...")
                editingData = False
            else:
                print("Invalid Selection.")
    
    return townData

def townDataPrinter(townData):
    print("Town Name: {}".format(townData["name"]))
    print("Market Modifier: {}".format(townData["market"]))
    print("Leave Cost: {}".format(townData["leaveCost"]))
    print("Hazard Check: {}".format(townData["hazardCheck"]))
    print("Town Description: \n{}".format(townData["hazardCheck"]))
    print("Market Description:\n {}".format(townData["marketDescription"]))
    print("Hazard Description: \n{}".format(townData["hazardDescription"]))

def townListSelector(tCollection):
    townList = []
    townSelected = False

    for i in tCollection:
        townList.append(i)

    for i in range(0, len(townList)):
        print("{}. {}".format(i+1, townList[i]["name"]))
    
    while(townSelected == False):
        try: 
            selection = (int)(input("Make Selection: "))
        except ValueError:
            print("Invalid Selection!")
        else:
            if (selection-1 in range(0,len(townList))):
                townSelected = True
                return townList[selection-1]
            else:
                print("Invalid Selection!")

def scenarioSelector():

            
        
        