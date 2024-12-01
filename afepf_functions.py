import pymongo
#Add Driver
def addDriver(collection):
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
    if finished.lower() == "yes": return True
#Add Team
def addTeam(connection):
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
    if finished.lower() == "yes": return True
#Add Manufacturer
def addManufacturer(connection):
    manufacturerName = input("Enter manufacturer's name")
    manufacturerPoints = float(input("Enter manufacturer's points total in Manufacturers’ Cup"))
    manufacturerPosition = int(input("Enter manufacturer's position in Manufacturers’ Cup"))
    newManufacturer = {"Manufacturer_Name": manufacturerName,
             "Manufacturer_Points": manufacturerPoints,
             "Manufacturers_Cup_Position": manufacturerPosition
             }
    result = collection.insert_one(newManufacturer)
    document_id = result.inserted_id
    print(document_id)
    finished = input("Finished adding manufacturers? Yes or no")
    if finished.lower() == "yes": return True
#Update function
def update(filterDoc, updateDoc, collection):
    result = collection.update_one(filterDoc, updateDoc)
    print("Documents updated: " + str(result.modified_count))
    print(collection.find_one(filterDoc))
#Update Driver Result
def updateDriverResult(collection):
    points = float(0)
    customerDriverList = []
    npjtDriverList = []
    cpos = False
    posC = False
    posN = False
#Update Overall Drivers
    for pos in range(1, 23):
        name = input("Enter driver's name who finished in position " + str(pos))
        customer = bool(input("Is the driver a Customer Driver: True or False"))
        if customer != False: customerDriverList.append(name)
        npjt = bool(input("Is the driver a NPJT Driver: True or False"))
        if npjt != False: npjtDriverList.append(name)
        pole = bool(input("Did the driver score the pole for the ePrix: True or False"))
        if pole != False: points += 1
        fastLap = bool(input("Did the driver set the fastest lap for the ePrix: True or False"))
        if fastLap != False: points += 1
        ledLap = bool(input("Did the driver lead a lap during the ePrix: True or False"))
        if ledLap != False: points += 1
        points += float(input("Enter the points they scored from their finishing position:"))
        filterDoc = {"Name": name}
        updateDoc = {"$inc": {"Driver_Points": points}}
        update(filterDoc, updateDoc, collection)
        points = 0
    cursor = collection.find({}, {"_id": 0, "Name": 1, "Driver_Points": 1, "Drivers_Championship_Position": 1}).sort("Driver_Points", pymongo.DESCENDING)
    for document in cursor:
        print(document)
    while cpos != True:
        name2 = input("Enter driver's name to alter their championship position")
        newpos = int(input("Enter their new championship position:"))
        filterDoc2 = {"Name": name2}
        updateDoc2 = {"$set": {"Drivers_Championship_Position": newpos}}
        update(filterDoc2, updateDoc2, collection)
        cpos = bool(input("Finished updating drivers? True or False"))
#Update Customer Drivers
    for customer in customerDriverList:
        print(customer)
        customerPoints = float(input("Enter the points they scored from their finishing position in the Customer class:"))
        filterDocC = {"Name": customer}
        updateDocC = {"$inc": {"Customer_Driver.Customer_Driver_Points": customerPoints}}
        update(filterDocC, updateDocC, collection)
    cursorC = collection.find({}, {"_id": 0, "Name": 1, "Customer_Driver.Customer_Driver_Points": 1,
                                  "Customer_Driver.Customer_Driver_Position": 1}).sort("Customer_Driver.Customer_Driver_Points", pymongo.DESCENDING)
    for document in cursorC:
        print(document)
    while posC != True:
        nameC = input("Enter driver's name to alter their championship position")
        newposC = int(input("Enter their new championship position:"))
        filterDocC2 = {"Name": nameC}
        updateDocC2 = {"$set": {"Customer_Driver.Customer_Driver_Position": newposC}}
        resultC2 = collection.update_one(filterDocC2, updateDocC2)
        update(filterDocC2, updateDocC2, collection)
        posC = bool(input("Finished updating drivers? True or False"))
#Update NPJT Drivers
    for npjt in npjtDriverList:
        print(npjt)
        npjtPoints = float(input("Enter the points they scored from their finishing position in the NPJT class:"))
        filterDocN = {"Name": npjt}
        updateDocN = {"$inc": {"NPJT_Driver.NPJT_Driver_Points": npjtPoints}}
        update(filterDocN, updateDocN, collection)     
    cursorN = collection.find({}, {"_id": 0, "Name": 1, "NPJT_Driver.NPJT_Driver_Points": 1,
                                  "NPJT_Driver.NPJT_Driver_Position": 1}).sort("NPJT_Driver.NPJT_Driver_Points", pymongo.DESCENDING)
    for document in cursorN:
        print(document)
    while posN != True:
        nameN = input("Enter driver's name to alter their championship position")
        newposN = int(input("Enter their new championship position:"))
        filterDocN2 = {"Name": nameN}
        updateDocN2 = {"$set": {"NPJT_Driver.NPJT_Driver_Position": newposN}}
        update(filterDocN2, updateDocN2, collection)
        posC = bool(input("Finished updating drivers? True or False"))        
#Update Team Result
def updateTeamResult(collection):
    points = 0
    customerTeamList = []
    teamPos = False
    teamPosC = False
#Update Overall Teams
    for x in range(10):
        name = input("Enter the team's name to add their points")
        customer = bool(input("Is the team a Customer Team: True or False"))
        if customer != False: customerTeamList.append(name)
        points = float(input("Enter their points scored:"))
        filterDoc = {"Team_Name": name}
        updateDoc = {"$inc": {"Team_Points": points}}
        update(filterDoc, updateDoc, collection)
    cursor = collection.find({}, {"_id": 0, "Name": 1, "Team_Points": 1, "Teams_Championship_Position": 1}).sort("Team_Points", pymongo.DESCENDING)
    for document in cursor:
        print(document)
    while teamPos != True:
        name2 = input("Enter team's name to alter their championship position")
        newpos = int(input("Enter their new championship position:"))
        filterDoc2 = {"Team_Name": name2}
        updateDoc2 = {"$set": {"Teams_Championship_Position": newpos}}
        update(filterDoc2, updateDoc2, collection)
        teamPos = bool(input("Finished updating teams? True or False"))
#Update Customer Teams
    for customer in customerTeamList:
        print(customer)
        customerPoints = int(input("Enter the points they scored in the Customer class:"))
        filterDocC = {"Name": customer}
        updateDocC = {"$inc": {"Customer_Team.Customer_Team_Points": customerPoints}}
        update(filterDocC, updateDocC, collection)
    cursorC = collection.find({}, {"_id": 0, "Name": 1, "Customer_Team.Customer_Team_Points": 1,
                                   "Customer_Team.Customer_Team_Position": 1}).sort("Customer_Team.Customer_Team_Points", pymongo.DESCENDING)
    for document in cursorC:
        print(document)
    while teamPosC != True:
        nameC = input("Enter team's name to alter their championship position")
        newposC = int(input("Enter their new championship position:"))
        filterDocC2 = {"Team_Name": nameC}
        updateDocC2 = {"$set": {"Customer_Team.Customer_Team_Position": newposC}}
        update(filterDocC2, updateDocC2, collection)
        teamPosC = bool(input("Finished updating teams? True or False"))    
#Update Manufacturer Result
def updateManufacturerResult(collection):
    points = 0
    manuPos = False
    for x in range(6):
        name = input("Enter the manufacturer's name to add their points")
        points = int(input("Enter their points scored:"))
        filterDoc = {"Manufacturer_Name": name}
        updateDoc = {"$inc": {"Team_Points": points}}
        update(filterDoc, updateDoc, collection)
    cursor = collection.find({}, {"_id": 0, "Name": 1, "Manufacturer_Points": 1, "Manufacturer_Cup_Position": 1}).sort("Manufacturer_Points", pymongo.DESCENDING)
    for document in cursor:
        print(document)
    while manuPos != True:
        name = input("Enter manufacturer's name to alter their championship position")
        newpos = int(input("Enter their new championship position:"))
        filterDoc2 = {"Team_Name": name2}
        updateDoc2 = {"$set": {"Manufacturer_Cup_Position": newpos}}
        update(filterDoc2, updateDoc2, collection)
        manuPos = bool(input("Finished updating teams? True or False"))
#Update Driver
def updateDriver(collection):
    name = input("Enter the name of the driver you wish to update:")
    filterDoc = {"Name": name}
    choice = int(input("Which field do you want to update: 1) Name" + "\n"
                       + "2) Team" + "\n"
                       + "3) Driver_Points" + "\n"
                       + "4) Drivers_Championship_Position" + "\n"
                       + "5) Customer_Driver_Points" + "\n"
                       + "6) Customer_Driver_Position" + "\n"
                       + "7) NPJT_Driver_Points" + "\n"
                       + "8) NPJT_Driver_Position"))
    if choice == 1:
        newName = input("Please enter the driver's updated name:")
        updateName = {"$set": {"Name":newName}}
        update(filterDoc, updateName, collection)
    elif choice == 2:
        newTeam = input("Please enter the driver's updated team:")
        updateTeam = {"$set": {"Team":newTeam}}
        update(filterDoc, updateTeam, collection)
    elif choice == 3:
        newPoints = float(input("Please enter the driver's updated points total:"))
        updatePoints = {"$set": {"Driver_Points":newPoints}}
        update(filterDoc, updatePoints, collection)
    elif choice == 4:
        newPosition = int(input("Please enter the driver's updated championship position:"))
        updatePosition = {"$set": {"Drivers_Championship_Position":newPosition}}
        update(filterDoc, updatePosition, collection)
    elif choice == 5:
        result = collection.find_one({"$and":[{"Name": name}, {"Customer_Driver.Customer_Driver_Points" :{"$gte":0}}]})
        newCustPoints = float(input("Please enter the driver's updated points total for the Customer Trophy for Drivers:"))
        updateCustPoints = {"$set": {"Customer_Driver.Customer_Driver_Points":newCustPoints}}
        if type(result) != None:
            update(filterDoc, updateCustPoints, collection)
        else:
            cont = input("Field does not yet exist for driver document. Do you still wish to continue?: yes or no")
            if cont.lower() == "yes":
                result = collection.update_one(filterDoc, updateCustPoints, upsert = True)
                print("Documents updated: " + str(result.modified_count))
                print(collection.find_one(filterDoc))
    elif choice == 6:
        result = collection.find_one({"$and":[{"Name": name}, {"Customer_Driver.Customer_Driver_Position" :{"$gte":0}}]})
        newCustPosition = int(input("Please enter the driver's updated championship position for the Customer Trophy for Drivers:"))
        updateCustPosition = {"$set": {"Customer_Driver.Customer_Driver_Position":newCustPosition}}
        if type(result) != None:
            update(filterDoc, updatePosition, collection)
        else:
            cont = input("Field does not yet exist for driver document. Do you still wish to continue?: yes or no")
            if cont.lower() == "yes":
                result = collection.update_one(filterDoc, updateCustPosition, upsert = True)
                print("Documents updated: " + str(result.modified_count))
                print(collection.find_one(filterDoc))
    elif choice == 7:
        result = collection.find_one({"$and":[{"Name": name}, {"NPJT_Driver.NPJT_Driver_Points" :{"$gte":0}}]})
        newNPJTPoints = float(input("Please enter the driver's updated points total for the Nelson Piquet Jr Trophy:"))
        updateNPJTPoints = {"$set": {"NPJT_Driver.NPJT_Driver_Points":newCustPoints}}
        if type(result) != None:
            update(filterDoc, updateCustPoints, collection)
        else:
            cont = input("Field does not yet exist for driver document. Do you still wish to continue?: yes or no")
            if cont.lower() == "yes":
                result = collection.update_one(filterDoc, updateCustPoints, upsert = True)
                print("Documents updated: " + str(result.modified_count))
                print(collection.find_one(filterDoc))
    elif choice == 8:
        result = collection.find_one({"$and":[{"Name": name}, {"NPJT_Driver.NPJT_Driver_Position" :{"$gte":0}}]})
        newNPJTPosition = int(input("Please enter the driver's updated championship position for the Nelson Piquet Jr Trophy:"))
        updateNPJTPosition = {"$set": {"NPJT_Driver.NPJT_Driver_Position":newNPJTPosition}}
        if type(result) != None:
            update(filterDoc, updateNPJTPosition, collection)
        else:
            cont = input("Field does not yet exist for driver document. Do you still wish to continue?: yes or no")
            if cont.lower() == "yes":
                result = collection.update_one(filterDoc, updateDoc, upsert = True)
                print("Documents updated: " + str(result.modified_count))
                print(collection.find_one(filterDoc))
    else:
        print("Enter a number between 1 and 8, which corresponds with the field you would like to update")
    finished = input("Finished adding drivers? Yes or no")
    if finished.lower() == "yes": return True
#Update Team
def updateTeam(collection):
    name = input("Enter the name of the team you wish to update:")
    filterDoc = {"Team_Name": name}
    choice = int(input("Which field do you want to update: 1) Team_Name" + "\n"
                       + "2) Manufacturer" + "\n"
                       + "3) Team_Points" + "\n"
                       + "4) Teams_Championship_Position" + "\n"
                       + "5) Customer_Team_Points" + "\n"
                       + "6) Customer_Team_Position"))
    if choice == 1:
        newName = input("Please enter the team's updated name:")
        updateName = {"$set": {"Team_Name":newName}}
        update(filterDoc, updateName, collection)
    elif choice == 2:
        newManu = input("Please enter the team's updated manufacturer:")
        updateManu = {"$set": {"Manufacturer":newManu}}
        update(filterDoc, updateManu, collection)
    elif choice == 3:
        newPoints = float(input("Please enter the team's updated points total:"))
        updatePoints = {"$set": {"Team_Points":newPoints}}
        update(filterDoc, updatePoints, collection)
    elif choice == 4:
        newPosition = int(input("Please enter the team's updated championship position:"))
        updatePosition = {"$set": {"Teams_Championship_Position":newPosition}}
        update(filterDoc, updatePosition, collection)
    elif choice == 5:
        result = collection.find_one({"$and":[{"Team_Name": name}, {"Customer_Team.Customer_Team_Points" :{"$gte":0}}]})
        newCustPoints = float(input("Please enter the team's updated points total for the Customer Teams Championship:"))
        updateCustPoints = {"$set": {"Customer_Team.Customer_Team_Points":newCustPoints}}
        if type(result) != None:
            update(filterDoc, updateCustPoints, collection)
        else:
            cont = input("Field does not yet exist for team document. Do you still wish to continue?: yes or no")
            if cont.lower() == "yes":
                result = collection.update_one(filterDoc, updateCustPoints, upsert = True)
                print("Documents updated: " + str(result.modified_count))
                print(collection.find_one(filterDoc))
    elif choice == 6:
        result = collection.find_one({"$and":[{"Team_Name": name}, {"Customer_Team.Customer_Team_Position" :{"$gte":0}}]})
        newCustPosition = int(input("Please enter the team's updated championship position for the Customer Teams Championship:"))
        updateCustPosition = {"$set": {"Customer_Team.Customer_Team_Position":newCustPosition}}
        if type(result) != None:
            update(filterDoc, updatePosition, collection)
        else:
            cont = input("Field does not yet exist for team document. Do you still wish to continue?: yes or no")
            if cont.lower() == "yes":
                result = collection.update_one(filterDoc, updateCustPosition, upsert = True)
                print("Documents updated: " + str(result.modified_count))
                print(collection.find_one(filterDoc))
    else:
        print("Enter a number between 1 and 6, which corresponds with the field you would like to update")
    finished = input("Finished adding teams? Yes or no")
    if finished.lower() == "yes": return True
#Update Manufacturer
def updateManufacturer(collection):
    name = input("Enter the name of the driver you wish to update:")
    filterDoc = {"Manufacturer_Name": name}
    choice = int(input("Which field do you want to update: 1) Manufacturer_Name" + "\n"
                       + "2) Manufacturer_Points" + "\n"
                       + "3) Manufacturers_Cup_Position"))
    if choice == 1:
        newName = input("Please enter the manufacturer's updated name:")
        updateName = {"$set": {"Manufacturer_Name":newName}}
        update(filterDoc, updateName, collection)
    elif choice == 2:
        newPoints = float(input("Please enter the manufacturer's updated points total:"))
        updatePoints = {"$set": {"Manufacturer_Points":newPoints}}
        update(filterDoc, updatePoints, collection)
    elif choice == 3:
        newPosition = int(input("Please enter the manufacturer's updated cup position:"))
        updatePosition = {"$set": {"Manufacturers_Cup_Position":newPosition}}
        update(filterDoc, updatePosition, collection)
    else:
        print("Enter a number between 1 and 3, which corresponds with the field you would like to update")
    finished = input("Finished adding manufacturers? Yes or no")
    if finished.lower() == "yes": return True
