from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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

mode = input("What mode would you like to use today: Add, Update, View, or Delete?")

if mode.lower() == "add":
    choice = input("Which collection do you wish to add to: Drivers, Teams, or Manufacturers?")
    if choice.lower() == "drivers":
        collection = db.Drivers
        x = False
        while x != True:
          driverFirstName = input("Enter driver's first name")
          driverSecondName = input("Enter driver's second name")
          driverName = driverFirstName + " " + driverSecondName
          driverTeam = input("Enter driver's team's name")
          driverPoints = float(input("Enter driver's points total in Drivers' Championship"))
          driverPosition = int(input("Enter driver's position in Drivers' Championship"))
          customerDriver = input("Is driver eligibile for the Customer Trophy for Drivers? Yes or No")
          if customerDriver.lower() == "yes":
              customerDriverPoints = float(input("Enter driver's points total in Customer Trophy for Drivers"))
              customerDriverPosition = int(input("Enter driver's position in Customer Trophy for Drivers"))
          npjtDriver = input("Is driver eligibile for the Nelson Piquet Jr Trophy? Yes or No")
          if npjtDriver.lower() == "yes":
              npjtDriverPoints = float(input("Enter driver's points total in the Nelson Piquet Jr Trophy"))
              npjtDriverPosition = int(input("Enter driver's position in the Nelson Piquet Jr Trophy"))
          if customerDriver.lower() == "yes" and npjtDriver.lower() == "yes":
              newDriver = {"Name": driverName,
                           "Team": driverTeam,
                           "Driver_Points": driverPoints,
                           "Drivers_Championship_Position": driverPosition,
                           "Customer_Driver": {"Customer_Driver_Points": customerDriverPoints,
                                               "Customer_Driver_Position": customerDriverPosition
                                               },
                           "NPJT_Driver": {"NPJT_Driver_Points": npjtDriverPoints,
                                           "NPJT_Driver_Position": npjtDriverPosition
                                           }
                           }
          elif customerDriver.lower() == "yes" and npjtDriver.lower() == "no":
              newDriver = {"Name": driverName,
                           "Team": driverTeam,
                           "Driver_Points": driverPoints,
                           "Drivers_Championship_Position": driverPosition,
                           "Customer_Driver": {"Customer_Driver_Points": customerDriverPoints,
                                               "Customer_Driver_Position": customerDriverPosition
                                               }
                           }
          elif customerDriver.lower() == "no" and npjtDriver.lower() == "yes":
              newDriver = {"Name": driverName,
                           "Team": driverTeam,
                           "Driver_Points": driverPoints,
                           "Drivers_Championship_Position": driverPosition,
                           "NPJT_Driver": {"NPJT_Driver_Points": npjtDriverPoints,
                                           "NPJT_Driver_Position": npjtDriverPosition
                                           }
                           }
          else:
              newDriver = {"Name": driverName,
                           "Team": driverTeam,
                           "Driver_Points": driverPoints,
                           "Drivers_Championship_Position": driverPosition
                           }
          result = collection.insert_one(newDriver)
          document_id = result.inserted_id
          print(document_id)
          finished = input("Finished adding drivers? Yes or no")
          if finished.lower() == "yes":
              x = True;
    
    if choice.lower() == "teams":
        collection = db.Teams
        x = False
        while x != True:
          teamName = input("Enter team's name")
          teamManufacturer = input("Enter team's manufacturer")
          teamPoints = float(input("Enter team's points total in Teams' Championship"))
          teamPosition = int(input("Enter team's position in Teams' Championship"))
          customerTeam = input("Is team eligibile for the Customer Teams' Championship? Yes or No")
          if customerTeam.lower() == "yes":
              customerTeamPoints = float(input("Enter team's points total in Customer Teams' Championship"))
              customerTeamPosition = int(input("Enter team's position in Customer Teams' Championship"))
          if customerTeam.lower() == "yes":
              newTeam = {"Team_Name": teamName,
                           "Manufacturer": teamManufacturer,
                           "Team_Points": teamPoints,
                           "Teams_Championship_Position": teamPosition,
                           "Customer_Team": {"Customer_Team_Points": customerTeamPoints,
                                               "Customer_Team_Position": customerTeamPosition
                                               }
                           }
          else:
              newTeam = {"Team_Name": teamName,
                           "Manufacturer": teamManufacturer,
                           "Team_Points": teamPoints,
                           "Teams_Championship_Position": teamPosition
                           }
          result = collection.insert_one(newTeam)
          document_id = result.inserted_id
          print(document_id)
          finished = input("Finished adding teams? Yes or no")
          if finished.lower() == "yes":
              x = True;

    if choice.lower() == "manufacturers":
        collection = db.Manufacturers
        x = False
        while x != True:
          manufacturerName = input("Enter manufacturer's name")
          manufacturerPoints = float(input("Enter manufacturer's points total in Manufacturers’ Cup"))
          manufacturerPosition = int(input("Enter manufacturer's position in Manufacturers’ Cup"))
          newTeam = {"Manufacturer_Name": manufacturerName,
                     "Manufacturer_Points": manufacturerPoints,
                     "Manufacturers_Cup_Position": manufacturerPosition
                     }
          result = collection.insert_one(newTeam)
          document_id = result.inserted_id
          print(document_id)
          finished = input("Finished adding manufacturers? Yes or no")
          if finished.lower() == "yes":
              x = True;    
client.close()          
