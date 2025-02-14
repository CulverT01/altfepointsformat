from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import afepf_functions as afepf

def finish (state):
    finished = False
    finish = input("Are you finished with the " + state + ": Yes or No")
    if finish.lower() == "yes": finished = True
    return finished

uri = "mongodb+srv://username:password@clusterafepf.u389v.mongodb.net/?retryWrites=true&w=majority&appName=Clusterafepf"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#Main program
#db
x = False
finished = False
finishedMode = False
finishedAdd = False
finishedUpd = False
finishedUpdoc = False
finishedView = False
finishedVwSi = False
finishedVwCh = False
finishedDel = False
while finished != True:
    season = input("Which season do you wish to view from: " + "Season 10" + "\n"
                       + "Season 11")
    if season.lower() == "season 10": db = client.AltFePointsFormat
    elif season.lower() == "season 11": db = client.Season11
    else: print("Please enter the season you wish to view like so: 'season 1'")
    while finishedMode != True:
        mode = int(input("What mode would you like to use today, please enter 1, 2, 3, or 4: 1) Add" + "\n"
                         + "2) Update" + "\n"
                         + "3) View" + "\n"
                         +"4) Delete"))
        #If mode is add, then:
        if mode == 1:
            while finishedAdd != True:
                choice = int(input("Which collection do you wish to add to: 1) Drivers" + "\n"
                                   + "2) Teams" + "\n"
                                   + "3) Manufacturers?"))
        #If choice is drivers, then:
                if choice == 1:
                    collection = db.Drivers
                    while x != True:
                        x = afepf.addDriver(collection)             
        #If choice is teams, then:
                elif choice == 2:
                    collection = db.Teams
                    while x != True:
                        x = afepf.addTeam(collection)
        #If choice is manufacturers, then:
                elif choice == 3:
                    collection = db.Manufacturers
                    while x != True:
                        x = afepf.addManufacturer(collection)
                x = False
                finishedAdd = finish("adding of documents")
            finishedAdd = False
        #If mode is update, then:            
        elif mode == 2:
            while finishedUpd != True:
                updateChoice = int(input("Do you wish to 1) Update a document" + "\n"
                                         + "2) Add the results of a recent ePrix"))
                if updateChoice == 1:
                    while finishedUpdoc != True:
                        choice = int(input("Which collection do you wish to update a document for: 1) Drivers" + "\n"
                                           + "2) Teams" + "\n"
                                           + "3) Manufacturers?"))
        #If choice is drivers, then:
                        if choice == 1:
                            collection = db.Drivers
                            while x != True:
                                x = afepf.updateDriver(collection)
                            finishedUpdoc = finish("updating of the collection")
        #If choice is teams, then:
                        elif choice == 2:
                            collection = db.Teams
                            while x != True:
                                x = afepf.updateTeam(collection)
                            finishedUpdoc = finish("updating of the collection")
        #If choice is manufacturers, then:
                        elif choice == 3:
                            collection = db.Manufacturers
                            while x != True:
                                x = afepf.updateManufacturer(collection)
                            finishedUpdoc = finish("updating of the collection")
                        x = False
                    finishedUpdoc = False
                    finishedUpd = finish("updating of the database")
                elif updateChoice == 2:
                    collection = db.Drivers
                    afepf.updateDriverResult(collection)
                    collection = db.Teams
                    afepf.updateTeamResult(collection)
                    collection = db.Manufacturers
                    afepf.updateManufacturerResult(collection)
                    finishedUpd = finish("updating of the database")
            finishedUpd = False
        #If mode is view, then:
        elif mode == 3:
            while finishedView != True:
                viewChoice = int(input("Do you wish to view 1) A single document" + "\n"
                                       + "2) The most recent standings for a championship"))
                if viewChoice == 1:
                    while finishedVwSi != True:
                        choice = int(input("Which collection do you wish to view from: 1) Drivers" + "\n"
                                           + "2) Teams" + "\n"
                                           + "3) Manufacturers?"))
        #If choice is drivers, then:
                        if choice == 1:
                            collection = db.Drivers
                            while x != True:
                                x = afepf.readDriver(collection)
                            finishedVwSi = finish("competitor's details")
        #If choice is teams, then:
                        elif choice == 2:
                            collection = db.Teams
                            while x != True:
                                x = afepf.readTeam(collection)
                            finishedVwSi = finish("competitor's details")
        #If choice is manufacturers, then:
                        elif choice == 3:
                            collection = db.Manufacturers
                            while x != True:
                                x = afepf.readManufacturer(collection)
                            finishedVwSi = finish("competitor's details")
                        x = False
                    finishedVwSi = False
                    finishedView = finish("viewing of the database")
                elif viewChoice == 2:
                    while finishedVwCh != True:
                        choice2 = int(input("Which collection do you wish to view championships from: 1) Drivers (Drivers' Championship, Customer Trophy for Drivers, Nelson Piquet Jr Trophy)" + "\n"
                                            + "2) Teams (Teams' Championship, Customer Teams' Championship)" + "\n"
                                            + "3) Manufacturers?"))
        #If choice is drivers, then:
                        if choice2 == 1:
                            collection = db.Drivers
                            while x != True:
                                x = afepf.readDriverResult(collection)
                            finishedVwCh = finish("championships results")
        #If choice is teams, then:
                        elif choice2 == 2:
                            collection = db.Teams
                            while x != True:
                                x = afepf.readTeamResult(collection)
                            finishedVwCh = finish("championships results")
        #If choice is manufacturers, then:
                        elif choice2 == 3:
                            collection = db.Manufacturers
                            while x != True:
                                x = afepf.readManufacturerResult(collection)
                            finishedVwCh = finish("championships results")
                        x = False
                    finishedVwCh = False
                    finishedView = finish("viewing of the database")
                finishedView = False
        #If mode is delete, then:
        elif mode == 4:
            while finishedDel != True:
                delChoice = int(input("Which collection do you wish to delete from: 1) Drivers" + "\n"
                                       + "2) Teams" + "\n"
                                       + "3) Manufacturers?"))
        #If choice is drivers, then:
                if delChoice == 1:
                    collection = db.Drivers
                    while x != True:
                        x = afepf.deleteDriver(collection)
        #If choice is teams, then:
                elif delChoice == 2:
                    collection = db.Teams
                    while x != True:
                        x = afepf.deleteTeam(collection)
        #If choice is manufacturers, then:
                elif delChoice == 3:
                    collection = db.Manufacturers
                    while x != True:
                        x = afepf.deleteManufacturer(collection)
                x = False
                finishedDel = finish("deleting of documents")
            finishedDel = False
        else:
            print("Please enter a number between 1 and 4")
        finishedMode = finish("season")
    finishedMode = False
    finished = finish("program")
#Close connection to the database
client.close()


