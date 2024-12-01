from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import afepf_functions as afepf

uri = "mongodb+srv://username:passowrd@clusterafepf.u389v.mongodb.net/?retryWrites=true&w=majority&appName=Clusterafepf"

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
mode = input("What mode would you like to use today: Add, Update, View, or Delete?")
#If mode is add, then:
if mode.lower() == "add":
    choice = input("Which collection do you wish to add to: Drivers, Teams, or Manufacturers?")
#If choice is drivers, then:
    if choice.lower() == "drivers":
        collection = db.Drivers
        while x != True:
            x = afepf.addDriver(collection) 
#If choice is teams, then:
    elif choice.lower() == "teams":
        collection = db.Teams
        while x != True:
            x = afepf.addTeam(collection)
#If choice is manufacturers, then:
    elif choice.lower() == "manufacturers":
        collection = db.Manufacturers
        while x != True:
            x = afepf.addManufacturer(collection)
#If mode is update, then:            
elif mode.lower() == "update":
    updateChoice = int(input("Do you wish to 1) update a document" + "/n"
                             + "2) add the results of a recent ePrix"))
    if updateChoice == 1:
        choice = input("Which collection do you wish to update to: Drivers, Teams, or Manufacturers?")
#If choice is drivers, then:
        if choice.lower() == "drivers":
            collection = db.Drivers
            while x != True:
                x = afepf.updateDriver(collection) 
#If choice is teams, then:
        elif choice.lower() == "teams":
            collection = db.Teams
            while x != True:
                x = afepf.updateTeam(collection)
#If choice is manufacturers, then:
        elif choice.lower() == "manufacturers":
            collection = db.Manufacturers
            while x != True:
                x = afepf.updateManufacturer(collection)
    elif updateChoice == 2:
        collection = db.Drivers
        afepf.updateDriverResult(collection)
        afepf.updateTeamResult(collection)
        afepf.updateManufacturerResult(collection)
client.close()


