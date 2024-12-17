from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import afepf_functions as afepf

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
db = client.AltFePointsFormat
x = False
finished = False
while finished != True:
    mode = input("What mode would you like to use today: Add, Update, View, or Delete?")
    #If mode is add, then:
    if mode.lower() == "add":
        choice = int(input("Which collection do you wish to view from: 1) Drivers" + "\n"
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
    #If mode is update, then:            
    elif mode.lower() == "update":
        updateChoice = int(input("Do you wish to 1) Update a document" + "\n"
                                 + "2) Add the results of a recent ePrix"))
        if updateChoice == 1:
            choice = int(input("Which collection do you wish to view from: 1) Drivers" + "\n"
                               + "2) Teams" + "\n"
                               + "3) Manufacturers?"))
    #If choice is drivers, then:
            if choice == 1:
                collection = db.Drivers
                while x != True:
                    x = afepf.updateDriver(collection) 
    #If choice is teams, then:
            elif choice == 2:
                collection = db.Teams
                while x != True:
                    x = afepf.updateTeam(collection)
    #If choice is manufacturers, then:
            elif choice == 3:
                collection = db.Manufacturers
                while x != True:
                    x = afepf.updateManufacturer(collection)
        elif updateChoice == 2:
            collection = db.Drivers
            afepf.updateDriverResult(collection)
            collection = db.Teams
            afepf.updateTeamResult(collection)
            collection = db.Manufacturers
            afepf.updateManufacturerResult(collection)
    elif mode.lower() == "view":
        viewChoice = int(input("Do you wish to view 1) A single document" + "\n"
                               + "2) The most recent standings for a championship"))
        if viewChoice == 1:
            choice = int(input("Which collection do you wish to view from: 1) Drivers" + "\n"
                               + "2) Teams" + "\n"
                               + "3) Manufacturers?"))
    #If choice is drivers, then:
            if choice == 1:
                collection = db.Drivers
                while x != True:
                    x = afepf.readDriver(collection) 
    #If choice is teams, then:
            elif choice == 2:
                collection = db.Teams
                while x != True:
                    x = afepf.readTeam(collection)
    #If choice is manufacturers, then:
            elif choice == 3:
                collection = db.Manufacturers
                while x != True:
                    x = afepf.readManufacturer(collection)
        elif viewChoice == 2:
            choice2 = int(input("Which collection do you wish to view championships from: 1) Drivers (Drivers' Championship, Customer Trophy for Drivers, Nelson Piquet Jr Trophy)" + "\n"
                                + "2) Teams (Teams' Championship, Customer Teams' Championship)" + "\n"
                                + "3) Manufacturers?"))
    #If choice is drivers, then:
            if choice2 == 1:
                collection = db.Drivers
                while x != True:
                    x = afepf.readDriverResult(collection) 
    #If choice is teams, then:
            elif choice2 == 2:
                collection = db.Teams
                while x != True:
                    x = afepf.readTeamResult(collection)
    #If choice is manufacturers, then:
            elif choice2 == 3:
                collection = db.Manufacturers
                while x != True:
                    x = afepf.readManufacturerResult(collection)
    elif mode.lower() == "delete":
        delChoice = int(input("Which collection do you wish to delete from: 1) Drivers" + "\n"
                               + "2) Teams" + "\n"
                               + "3) Manufacturers?"))
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
    finish = input("Are you finished with the program: Yes or No")
    if finish.lower() == "yes": finished = True
    x = False
#Close connection to the database
client.close()


