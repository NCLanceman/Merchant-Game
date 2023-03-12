import json
import os

scenarioData = {
    "scenarioName": "Main Campaign",
    "filename": "MainCampaign.json",
    "towns":{ 
    "Start":{
        "connections": ["Hatterston"]
    },
        "Hatterston":{
    "name": "Hatterston",
    "market": 5,
    "leaveCost": 50,
    "hazardCheck": 2,
    "townDescription": "An idillyic village of small hamlets and oaken trees.",
    "marketDescription": "The merchant has found space for a stall in the town square.\nWorkmen and livestock pass on their various errands on this bright, sunshiny day.",
    "hazardDescription": "The road is beset by bandits!",
    "connections": ["Purple Ridge City"]
    },
    #1. Purple Ridge City / +8 / 30 / +5
    "Purple Ridge City":{
        "name": "Purple Ridge City",
        "market": 5,
        "leaveCost": 70,
        "hazardCheck": 5,
        "townDescription": "A bustling town in the smoky purple mountains, a famous crossroads of the frontier.",
        "marketDescription": "After setting up shop on the cobblestone avenue, the merchant hawks his wares to passers by.",
        "hazardDescription": "A glint of steel shows through the mists. Bandits attack!",
        "connections": ["Burgsbergs","Hatanniland"]
    },
    #2. Burgsbergs / +0 / 20 / -2
    "Burgsbergs":{
        "name": "Burgsbergs",
        "market": 10,
        "leaveCost": 75,
        "hazardCheck": -2,
        "townDescription": "A somewhat recursively named town built around an iceburg, settled by wealthy merchants.",
        "marketDescription": "Cloaked in furs and set up near snocone stalls, the merchant is ready to sell ice to eskimos.",
        "hazardDescription": "A tamed polar bear let off it's chain and attacks, with bandits following!",
        "connections": ["Hatanniland"]
    },
    #3. Hatanniland / -2 / 30 / -4
    "Hatanniland":{
        "name": "Hatanniland",
        "market": -10,
        "leaveCost": 60,
        "hazardCheck": -4,
        "townDescription": "A tribal stronghold held by the Hattani people on the plains.",
        "marketDescription": "Between beaded chains and buffalo hides, the merchant lays out a rug and prepares for the day.",
        "hazardDescription": "Mounted tribesmen level their spears at the merchant. Ride!",
        "connections": ["Fallen Pine Township"]
    },
    #4. Fallen Pine Township / -5 / 40 / -2
    "Fallen Pine Township":{
        "name": "Fallen Pine Township",
        "market": -10,
        "leaveCost": 70,
        "hazardCheck": -2,
        "townDescription": "A logging community in the coastal pine forests, upland of the Old Ruins.",
        "marketDescription": "Between ox cart ruts and new pine board buildings, the merchant is not at a loss for places to set up.",
        "hazardDescription": "Bushwackers drop a tree in the path of the wagon and aim their rifles at the merchant. Draw!",
        "connections": ["Pextorantal","Silent Rapids"]
    },
    #5. Pextorantal / +0 / 30 / +0
    "Pextorantal":{
        "name": "Pextorantal",
        "market": -15,
        "leaveCost": 100,
        "hazardCheck": 0,
        "townDescription": "The markings on the concrete have been rendered unreadable in the passage of time. The name is really a best guess.",
        "marketDescription": "Barrel fires illuminate the ruins as the townsfolk ogle the new wagon of wares brought by the merchant.",
        "hazardDescription": "A wire stretches in front of the road, too late to avoid. Attack comes from the night!",
        "connections": ["Silent Rapids"]
    },
    #6. Silent Rapids / -5 / 40 / +5
    "Silent Rapids":{
        "name": "Silent Rapids",
        "market": -5,
        "leaveCost": 150,
        "hazardCheck": 5,
        "townDescription": "The fish have finally returned to the rivers of this town, though they're a bit different now.",
        "marketDescription": "A stall by the docks gives a good view of the boats on the lake."+
        "\nOccasionally a crab the size of a terrier scuttles past, chased by a cat.",
        "hazardDescription": "The chitionous snaps of crab claws and ominous chanting follow you. Flee!",
        "connections": ["Caninus Megacity 21","Tansho-Nagashi City"]

    },
    #7. Caninus Megacity 21 / -6 / 40 / +5
    "Caninus Megacity 21":{
        "name": "Caninus Megacity 21",
        "market": -6,
        "leaveCost": 75,
        "hazardCheck": 5,
        "townDescription": "A neon-drenched cybertopia archology run by dog-men, and the occasional human friend.",
        "marketDescription": "After purchasing a permit and posting the stall on cyberspace bulletin boards, adorable cyberdogs come to see the wares.",
        "hazardDescription": "A pack of scruffy looking cyber dogs in leather jackets and brandishing monoswords block your path. Bad dogs!",
        "connections": ["Fooksalot"]
    },
    #8. Tansho-Nagashi City / -10 / 60 / +0
    "Tansho-Nagashi City":{
        "name": "Tansho-Nagashi City",
        "market": -10,
        "leaveCost": 70,
        "hazardCheck": 0,
        "townDescription": "Cherry blossoms line the road to the land of samurai and their castles.",
        "marketDescription": "With a badge from the local daimyo, the merchant markets himself as a passing taikun with wares from far off lands.",
        "hazardDescription": "Ninjas attack the merchant! Better hope Conservation of Ninjitsu is real!",
        "connections": ["Fooksalot"]
    },
    #9. Fooksalot / 0 / 50 / +2
    "Fooksalot":{
        "name": "Fooksalot",
        "market": 0,
        "leaveCost": 100,
        "hazardCheck": 2,
        "townDescription": "A small, garish town of red silks, video poker, and blue alien prostitutes.",
        "marketDescription": "After enduring endless horrible puns from the mayor herself, the merchant dons\n"
        +"the traditional broad brimmed feathered purple hat of the local merchant and begins to sell his goods.",
        "hazardDescription": "Space Pirates fire a laser blunderbuss at the merchant's wagon. It's on!",
        "connections": "Finish"
    }},

    "encounters":{
        "Hatterston":{
            1:{
                "states": [["Boom","Normal","Bust"],[1,2,3]],
                "intro":"This is a placeholder for a random encounter in Hatterston",
                "options": {
                    "1":{
                    "description": "An auspicious beginning...",
                    "response": "To fortune and glory!",
                    "effects": [["None"],["End"]]
                }}
            }

        },
        "Purple Ridge City":{
                    "1":{
                        "states": [["Boom","Normal","Bust"],[1,2,3]],
                        "intro":"This is a placeholder for a random encounter in Purple Ridge City.",
                        "options": {
                            "1":{
                            "description": "Well, there's spacious skies and fertile plains about...",
                            "response": "Almost makes you want to sing, doesn't it?",
                            "effects": [["None"],["End"]]
                            }}
                    }
        },
        "Burgsbergs":{
                    "1":{
                        "states": [["Boom","Normal","Bust"],[1,2,3]],
                        "intro":"This is a placeholder for a random encounter in Burgsbergs.",
                        "options": {
                            "1":{
                            "description": "Ice to meet you!",
                            "response": "Chill out.",
                            "effects": [["None"],["End"]]
                            }}
                    }
        },
        "Hatanniland":{
                    "1":{
                        "states": [["Boom","Normal","Bust"],[1,2,3]],
                        "intro":"This is a placeholder for a random encounter in Hatanniland.",
                        "options": {
                            "1":{
                            "description": "If the drum beats stop and the smoke signals start, is that bad?",
                            "response": "Not until the headdresses come on.",
                            "effects": [["None"],["End"]]
                            }}
                    }

        },
        "Fallen Pine Township":{
                    "1":{
                        "states": [["Boom","Normal","Bust"],[1,2,3]],
                        "intro":"This is a placeholder for a random encounter in Fallen Pine Township.",
                        "options": {
                            "1":{
                            "description": "If a tree falls in the forest, and no one's around to hear it, can I sell it for lumber?",
                            "response": "You canny merchant you.",
                            "effects": [["None"],["End"]]
                            }}
                    }
        },
        "Pextorantal":{
                    "1":{
                        "states": [["Boom","Normal","Bust"],[1,2,3]],
                        "intro":"This is a placeholder for a random encounter in Pextorantal.",
                        "options": {
                            "1":{
                            "description": "Over the right barrel, rat on a stick is pretty good actually.",
                            "response": "Not as good as Tiajuana Iguana.",
                            "effects": [["None"],["End"]]
                            }}
                    }
        },
        "Silent Rapids": {
                    "1":{
                        "states": [["Boom","Normal","Bust"],[1,2,3]],
                        "intro":"This is a placeholder for a random encounter in Silent Rapids.",
                        "options": {
                            "1":{
                            "description": "I'm gettin' Innsmouth vibes from this place...",
                            "response": "Look, don't buy any green sea trinkets, okay?",
                            "effects": [["None"],["End"]]
                            }}
                    }

        },
        "Caninus Megacity 21": {
                    "1":{
                        "states": [["Boom","Normal","Bust"],[1,2,3]],
                        "intro":"This is a placeholder for a random encounter in Caninus Megacity 21.",
                        "options": {
                            "1":{
                            "description": "How much _is_ that puppy in the window?",
                            "response": "The one with the chromed out tail? You might have to pay in corp scrip.",
                            "effects": [["None"],["End"]]
                            }}
                    }

        },
        "Tansho-Nagashi City": {
                    "1":{
                        "states": [["Boom","Normal","Bust"],[1,2,3]],
                        "intro":"This is a placeholder for a random in Tansho-Nagashi City.",
                        "options": {
                            "1":{
                            "description": "Oh. Konnichiwa then.",
                            "response": "Arigato!",
                            "effects": [["None"],["End"]]
                            }}
                    }

        },
        "Fooksalot": {
                    "1":{
                        "states": [["Boom","Normal","Bust"],[1,2,3]],
                        "intro":"This is a placeholder for a random encounter in Fooksalot.",
                        "options": {
                            "1":{
                            "description": "The 'Live Nude Chicks' neon sign next to an animated pair of chopsticks intrigues me...",
                            "response": "It's a restaraunt. The least shady food vendor here, actually.",
                            "effects": [["None"],["End"]]
                            }}
                    }
        },
        "Generic":{
                    "1": {
                "states": [["Boom","Normal"],[1]],
                "intro":"A neighboring merchant offers you a short stake in an enterprise for a small fee. "+
                "The price is small but the rewards might be great.",
                "options": {
                    "1":{
                    "description": "Accept the bid. [-25 GOLD]",
                    "response": "You accept the other merchant's stake. May fortune smile on you!",
                    "effects": [["Debit",25],["1-1"]]
                },
                    "2": {
                    "description": "Decline the bid.",
                    "response": "You decline the offer. A bit of prudence might not hurt.",
                    "effects": [["None"],["End"]]
                    }
                },
            },
            "1-1":{
                "states": [["Boom","Normal"],[2,3]],
                "intro": "The neighboring merchant from earlier returns with news of the endeavor.",
                "options": {
                    "1":{
                    "description": "The die was cast...",
                    "response": "At length he describes the venture.",
                    "effects": [["Chance", 10],["1-2","1-3"]]
                    }}
            },
            "1-2":{
                "states": [["Boom","Normal"],[2,3]],
                "intro": "Fortune smiled on you both!",
                "options": {
                    "1":{
                    "description": "To fortune and glory!",
                    "response": "Your cheer is palpable.",
                    "effects": [["Credit", 100],["End"]]
                }}
            },
            "1-3":{
                "states": [["Boom","Normal"],[2,3]],
                "intro": "The endeavor ended in failure",
                "options": {
                    "1":{
                    "description": "Curses!",
                    "response": "You knew the risks when you signed on.",
                    "effects": [["None"],["End"]]
                }}
            },
            "2":{
                "states": [["Boom","Normal","Bust"],[1,2,3]],
                "intro":"This is a placeholder for a Generic random encounter.",
                "options": {
                    "1":{
                    "description": "Well, finish the game dammit!",
                    "response": "Working on it!",
                    "effects": [["None"],["End"]]
                }}
            }
        }
    }

}

if(os.path.isdir(".\Scenarios") == False):
    os.mkdir(".\Scenarios")
  

fileWriter = open(".\Scenarios\MainCampaign.json", "w")
fileWriter.write(json.dumps(scenarioData, indent=4))
fileWriter.close()