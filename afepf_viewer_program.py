from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import afepf_functions as afepf

def finish (state):
    finished = False
    finish = input("Are you finished with the " + state + ": Yes or No")
    if finish.lower() == "yes": finished = True
    return finished

uri = "mongodb+srv://viewer:0kNTRuTbTtvrkvNm@clusterafepf.u389v.mongodb.net/?retryWrites=true&w=majority&appName=Clusterafepf"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#Main program
#db = client.AltFePointsFormat
x = False
finished = False
finishedView = False
finishedChamp = False
finishedDetails = False
while finished != True:
    choice = input("Which season do you wish to view from: " + "Season 10" + "\n"
                       + "Season 11")
    if choice.lower() == "season 10": db = client.AltFePointsFormat
    elif choice.lower() == "season 11": db = client.Season11
    else: print("Please enter the season you wish to view like so: 'season 1'")
    while finishedView != True:
        choice1 = int(input("Hello. If you wish to view a championship, enter 1:" + "\n"
                           +"Or if you wish to view a single driver/team/manufacturer's details, enter 2:"))
        if choice1 == 1:
            while finishedChamp != True:
                choice2 = int(input("If you wish to view a Driver Championship (Drivers' Championship, Customer Trophy for Drivers, Nelson Piquet Jr Trophy), enter 1:" + "\n"
                                    + "If you wish to view a Team Championship (Teams' Championship, Customer Teams' Championship), enter 2:" + "\n"
                                    + "If you wish to view the Manufacturer Cup, enter 3"))
            #If choice is drivers, then:
                if choice2 == 1:
                    collection = db.Drivers
                    while x != True:
                        x = afepf.readDriverResult(collection)
                    finishedChamp = finish("Championships results")
            #If choice is teams, then:
                elif choice2 == 2:
                    collection = db.Teams
                    while x != True:
                        x = afepf.readTeamResult(collection)
                    finishedChamp = finish("Championships results")
                #If choice is manufacturers, then:
                elif choice2 == 3:
                    collection = db.Manufacturers
                    while x != True:
                        x = afepf.readManufacturerResult(collection)
                    finishedChamp = finish("Championships results")
                x = False
        elif choice1 == 2:
            while finishedDetails != True:
                choice2 = int(input("If you wish to view a Driver's details, enter 1:" + "\n"
                                    + "If you wish to view a Team's details, enter 2:" + "\n"
                                    + "If you wish to view a Manufacturer's details, enter 3:"))
            #If choice is drivers, then:
                if choice2 == 1:
                    collection = db.Drivers
                    while x != True:
                        x = afepf.readDriver(collection)
                    finishedDetails = finish("Competitor's details")
            #If choice is teams, then:
                elif choice2 == 2:
                    collection = db.Teams
                    while x != True:
                        x = afepf.readTeam(collection)
                    finishedDetails = finish("Competitor's details")
            #If choice is manufacturers, then:
                elif choice2 == 3:
                    collection = db.Manufacturers
                    while x != True:
                        x = afepf.readManufacturer(collection)
                    finishedDetails = finish("Competitor's details")
                x = False
        finishedView = finish("season")
    finished = finish("program")
client.close()
