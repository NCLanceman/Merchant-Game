import json
import os

scenarioTemplate = {
    "scenarioName": "",
    "filename": "",
    "towns":{
        "Start":{
            "connections":[]
        }
    },
    "encounters":{
    
    }
}

townTemplate = {
        "name": "",
        "market": "",
        "leaveCost": "",
        "hazardCheck": "",
        "townDescription": "",
        "marketDescription": "",
        "hazardDescription": "",
        "connections": []
    }


encounterTemplate = {
                "states": [[],[]],
                "intro":"",
                "options": {}
            }

encounterOptionTemplate = {
                    "description": "",
                    "response": "",
                    "effects": [[],[]]
                    }


#Step One: Create a New Scenario
#Step Two: Create a New Town
#Step Three: Save Scenario
#Step Four: Validate Scenario
#--Check if there is a Start and End in town connections

def createScenario():
    newScenario = scenarioTemplate.copy()

    newScenario["scenarioName"] = input("Enter Scenario Name: ")
    newScenario["filename"] = ("{}.json".format(input("Enter Filename: ")))
    print("Creating First Town...")
    firstTown = createTown()
    newScenario["towns"]["Start"]["connections"] = firstTown["name"]
    newScenario["towns"][firstTown["name"]] = firstTown
    newScenario["encounters"]["Generic"] = {}

    print("Town Added: {}".format(firstTown["name"]))

    menu = ["Add New Town", "Print List of Towns"]
    
    scenarioCreatorLoop = True
    while(scenarioCreatorLoop == True):
        selection = menuSelector(menu)
        if(selection == 0):
            newTown = createTown()
            newScenario["towns"][newTown["name"]] = newTown
            print("Town Added: {}".format(newTown["name"]))
        elif(selection == 1):
            for i in list(newScenario["towns"].keys()):
                if(i != "Start"):
                    print(i)
        elif(selection == 2):
            scenarioCreatorLoop = False

        menu = ["Add New Town", "Print List of Towns"]

    
    return newScenario




def createTown():
    newTown = townTemplate.copy()  
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
        selection = input("Accept? Y or N: ")
        if(selection[:1].lower() == 'y'):
            print("Town Saved to New Scenario.")
            validSelect = True
        elif(selection[:1].lower() == 'n'):
            print("Editing town...")
            newTown = editTown(newTown)
            validSelect = True
        else:
            print("Invalid Selection.")
    
    return newTown

def townDataPrinter(townData):
    print("Town Name: {}".format(townData["name"]))
    print("Market Modifier: {}".format(townData["market"]))
    print("Leave Cost: {}".format(townData["leaveCost"]))
    print("Hazard Check: {}".format(townData["hazardCheck"]))
    print("Town Description: \n{}".format(townData["hazardCheck"]))
    print("Market Description:\n {}".format(townData["marketDescription"]))
    print("Hazard Description: \n{}".format(townData["hazardDescription"]))

#Ensure that the name of the town is also the name of it's key in the Towns dictionary
def townListValidator(scenario):
    townList = list(scenario["towns"].keys())

    #Search for Name Mismatches
    for i in townList:
        if (scenario["towns"][i].get("name",False) != False):
            if(i != scenario["towns"][i]["name"]):
                print("Name mismatch detected: Town in Current Scenario {} listed as {}".format(scenario["towns"][i]["name"], i))
                tempTown = scenario["towns"][i]
                scenario["towns"].pop(i)
                scenario["towns"][tempTown["name"]] = tempTown
                print("Name updated.")
            else:
                print("Town Name {} verified.".format(i))
    
    #Search for duplicate

    return scenario


def editTown(townData):
    townDataPrinter(townData)

    editingData = True

    while (editingData):
        print("\nEDITING MENU: ")
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

#TODO: Add method for editing connections on existing towns to other existing towns

def scenarioEditor(scenario):
    editingScenario = True

    while(editingScenario):    
        print("\nScenario Editor Menu")
        menu = ["Edit Town", "Add/Edit Connections","Add Town","Add/Edit Encounters"]
        townList = list(scenario["towns"].keys())  
        
        firstMenuSelect = menuSelector(menu)
       
        if(firstMenuSelect == 0):
            townSelected = False
            while(townSelected == False):
                selection = menuSelector(townList)
                
                if(selection in range(0,len(townList))):
                    editedTown = editTown(scenario["towns"][townList[selection-1]])
                    scenario["towns"][townList[selection-1]] = editedTown
                elif (selection == len(townList)+1):
                    print("Returning to Menu.")
                    townSelected = True
                else:
                    print("Please select a valid town.")
        elif (firstMenuSelect == 1):
            menu = ["Change Start Point","Edit Town Connections"]

            selection = menuSelector(menu)
            
            if(selection == 0):
                startLocation = scenario["towns"]["Start"]["connections"][0]
                
                print("Current Start Location: {}".format(startLocation))

                startSelect = menuSelector(townList)
                if(startSelect in range(0, len(townList))):
                    startLocation = townList[startSelect-1]
                    scenario["towns"]["Start"]["connections"] = [startLocation]
                elif(startSelect == len(townList)+1):
                    print("Returning to Previous Menu...")
            elif(selection == 1):                
                connectionSelector = menuSelector(townList)
                
                if(connectionSelector in range(0,len(townList))):
                    scenario = editConnections(scenario,townList[connectionSelector-1])
                elif(connectionSelector == len(townList)+1):
                    print("Returning to Menu...")
            elif(selection == 2):
                print("Returning to Menu...")
        elif (firstMenuSelect == 2):
            newTown = createTown()
            scenario["towns"][newTown["name"]] = newTown
            print("Town Added: {}".format(newTown["name"]))
        elif (firstMenuSelect == 3):
            scenario = editEncounters(scenario)
        elif (firstMenuSelect == 4):
            print("Returning to Menu...")
            editingScenario = False
    
    return scenario



def editConnections(scenario, selectedTown):
    connections = scenario["towns"][selectedTown]["connections"]
    townList = list(scenario["towns"].keys())

    print("Current connections for {}: {}".format(selectedTown,connections))    

    editingConnections = True
    while(editingConnections == True):
        menu = ["Add Connection","Remove Connection"]
        selection = menuSelector(menu)
        
        if(selection == 1):           
            addingConnection = True
            while(addingConnection == True):
                
                addConnectionSelect = menuSelector(townList)
                if(addConnectionSelect in range(0,len(townList))):
                    connections.append(townList[addConnectionSelect-1])
                    addingConnection = False
                else:
                    print("Returning to Menu...")
                    addingConnection = False
        elif(selection == 2):           
            removingConnection = True
            while(removingConnection == True):
                removeConnectionSelect = menuSelector(connections)

                if(removeConnectionSelect in range(0, len(connections))):
                    connections.pop(removeConnectionSelect-1)
                    removingConnection = False
                elif(removeConnectionSelect == len(connections)+1):
                    print("Returning to Previous Menu...")
                    removingConnection = False
        elif(selection == 3):
            print("Returning to previous menu...")
            editingConnections = False
    
    scenario["towns"][selectedTown]["connections"] = connections
    return scenario

def editEncounters(scenario):
    menu = ["Add/Edit Town Specific Encounters","Add/Edit Generic Encounters"] 

    editingEncounters = True
    selection = menuSelector(menu)
                    
    #TODO: Draw the rest of the fucking owl

    return scenario

def encounterEditor(scenario, townSelection):
    print("encounterEditor placeholder")

def menuSelector(menuList):
    menuLoop = True
    menuList.append("Return to Previous Menu.")
    
    for i in range(len(menuList)):
        print("{}. {}".format(i+1, menuList[i]))

    while(menuLoop == True):
        try:
            selection = (int)(input("Enter Selection: "))
        except ValueError:
            print("Invalid Selection")
        else:
            if(selection in range(1, len(menuList)+1)):
                menuLoop = False
            else:
                print("Invalid Selection")
    
    return selection-1



editorRunning = True
loadedScenario = "None"
loadedScenarioName = "None"

while(editorRunning == True):        
    print("\nCaravansari Editor v0.2")
    print("Copyright 2023, Written By Jason Lee")
    print("An American Beef Productions Tool\n")
    print("\nCurrently Loaded Scenario: {}".format(loadedScenarioName))
    print("1. Create New Scenario")
    print("2. Load Scenario.")

    if(loadedScenario != "None"):
        print("3. Save Current Scenario.")
        print("4. Edit Scenario.")
    
    print("5. Exit Editor.")
    
    try:
        selection = (int)(input("Make Selection: "))
    except ValueError:
        print("Invalid Selection.")
    else:
        if(selection == 1):
            loadedScenario = createScenario()
            loadedScenarioName = loadedScenario["scenarioName"]
        elif(selection == 2):
            scenarioList = os.listdir(".\Scenarios")

            for i in range(len(scenarioList)):
                print("{}. {}".format((i+1), scenarioList[i]))
            
            try:
                selection = (int)(input("Select Scenario: "))
            except ValueError:
                print("Invalid Selection.")
            else:
                if (selection-1) in range(0,len(scenarioList)):
                    fileReader = open(".\Scenarios\{}".format(scenarioList[selection-1]),"r")
                    loadedScenario = json.loads(fileReader.read())
                    loadedScenarioName = loadedScenario["scenarioName"]
                    fileReader.close()
                else:
                    print("Invalid Selection!")    
        elif(selection == 3 and loadedScenario != "None"):
            fileWriter = open((".\Scenarios\{}".format(loadedScenario["filename"])), "w")
            fileWriter.write(json.dumps(loadedScenario, indent=4))
            fileWriter.close()
            print("Saved {} to Disk.".format(loadedScenarioName))
        elif(selection == 4 and loadedScenario != "None"):
            loadedScenario = scenarioEditor(loadedScenario)
            print("\nValidating Edits...")
            loadedScenario = townListValidator(loadedScenario)
        elif(selection == 5):
            editorRunning = False
            print("END OF PROGRAM.")
        else: 
            print("Invalid Selection.")