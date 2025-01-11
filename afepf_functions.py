import pymongo
from bson.objectid import ObjectId
#Add Driver
def addDriver(collection):
    driverFirstName = input("Enter driver's first name")
    driverSecondName = input("Enter driver's second name")
    driverName = driverFirstName + " " + driverSecondName
    driverInitial = input("Enter driver's initial")
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
                   "Driver_Initial": driverInitial,
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
                   "Driver_Initial": driverInitial,
                   "Team": driverTeam,
                   "Driver_Points": driverPoints,
                   "Drivers_Championship_Position": driverPosition,
                   "Customer_Driver": {"Customer_Driver_Points": customerDriverPoints,
                                       "Customer_Driver_Position": customerDriverPosition
                                       }
                   }
    elif customerDriver.lower() == "no" and npjtDriver.lower() == "yes":
      newDriver = {"Name": driverName,
                   "Driver_Initial": driverInitial,
                   "Team": driverTeam,
                   "Driver_Points": driverPoints,
                   "Drivers_Championship_Position": driverPosition,
                   "NPJT_Driver": {"NPJT_Driver_Points": npjtDriverPoints,
                                   "NPJT_Driver_Position": npjtDriverPosition
                                   }
                   }
    else:
      newDriver = {"Name": driverName,
                   "Driver_Initial": driverInitial,
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
def addTeam(collection):
    teamName = input("Enter team's name")
    teamInitial = input("Enter team's initial")
    teamManufacturer = input("Enter team's manufacturer")
    teamPoints = float(input("Enter team's points total in Teams' Championship"))
    teamPosition = int(input("Enter team's position in Teams' Championship"))
    customerTeam = input("Is team eligibile for the Customer Teams' Championship? Yes or No")
    if customerTeam.lower() == "yes":
      customerTeamPoints = float(input("Enter team's points total in Customer Teams' Championship"))
      customerTeamPosition = int(input("Enter team's position in Customer Teams' Championship"))
    if customerTeam.lower() == "yes":
      newTeam = {"Team_Name": teamName,
                 "Team_Initial": teamInitial,
                 "Manufacturer": teamManufacturer,
                 "Team_Points": teamPoints,
                 "Teams_Championship_Position": teamPosition,
                 "Customer_Team": {"Customer_Team_Points": customerTeamPoints,
                                   "Customer_Team_Position": customerTeamPosition
                                   }
                 }
    else:
      newTeam = {"Team_Name": teamName,
                 "Team_Initial": teamInitial,
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
def addManufacturer(collection):
    manufacturerName = input("Enter manufacturer's name")
    manufacturerInitial = input("Enter manufacturer's initial")
    manufacturerPoints = float(input("Enter manufacturer's points total in Manufacturers’ Cup"))
    manufacturerPosition = int(input("Enter manufacturer's position in Manufacturers’ Cup"))
    newManufacturer = {"Manufacturer_Name": manufacturerName,
                       "Manufacturer_Initial": manufacturerInitial,
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
#Update Points
def updatePoints(pos):
    points = 0.0
    if pos == 1: points = 20.0
    elif pos == 2: points = 17.0
    elif pos == 3: points = 15.0
    elif pos == 4: points = 13.0
    elif pos == 5: points = 11.0
    elif pos == 6: points = 10.0
    elif pos == 7: points = 9.0
    elif pos == 8: points = 8.0
    elif pos == 9: points = 7.0
    elif pos == 10: points = 6.0
    elif pos == 11: points = 5.0
    elif pos == 12: points = 4.0
    elif pos == 13: points = 3.0
    elif pos == 14: points = 2.0
    elif pos == 15: points = 1.0
    return points
#Update Driver Result
def updateDriverResult(collection):
    points = float(0)
    customerPoints = float(0)
    npjtPoints = float(0)
    customerDriverList = []
    npjtDriverList = []
    cpos = False
    posC = False
    posN = False
    pole = False
    fastLap = False
#Update Overall Drivers
    retirements = int(input("How many Retirements/Non-Classified finishers were there from the ePrix?")) 
    for pos in range(1, 23):
        init = input("Enter driver's initial who finished in position " + str(pos))
        customer = input("Is the driver a Customer Driver: yes or no")
        if customer.lower() == "yes": customerDriverList.append(init)
        npjt = input("Is the driver a NPJT Driver: yes or no")
        if npjt.lower() == "yes": npjtDriverList.append(init)
        if pole != True:
            poleScore = input("Did the driver score the pole for the ePrix: yes or no")
            if poleScore.lower() == "yes":
                points += 1
                pole = True
        if pos < 23 - retirements:
            if fastLap != True:
                fastLapScore = input("Did the driver set the fastest lap for the ePrix: yes or no")
                if fastLapScore.lower() == "yes":
                    points += 1
                    fastLap = True
            ledLap = input("Did the driver lead a lap during the ePrix: yes or no")
            if ledLap.lower() == "yes": points += 1
            finishPoints = updatePoints(pos)
            points += finishPoints
        filterDoc = {"Driver_Initial": init}
        updateDoc = {"$inc": {"Driver_Points": points}}
        result = collection.update_one(filterDoc,{"$push": {"Finishes": pos}}, upsert=True)
        update(filterDoc, updateDoc, collection)
        points = 0
    cursor = collection.find({}, {"_id": 0, "Driver_Initial": 1, "Driver_Points": 1,
                                  "Drivers_Championship_Position": 1, "Finishes": 1,}).sort("Driver_Points", pymongo.DESCENDING)
    docPos = 1
    for document in cursor:
         print("Driver Initial: "+ str(document["Driver_Initial"])+ "\n"
               + "Points: "+ str(document["Driver_Points"])+ "\n"
               + "Old Championship Position: " + str(document["Drivers_Championship_Position"]) + "\n"
               + "Finishes: "+ str(document["Finishes"]) + "\n"
               + "New Championship Position: " + str(docPos) + "\n")
         docPos += 1
    while cpos != True:
        init2 = input("Enter driver's initial to alter their championship position")
        newpos = int(input("Enter their new championship position:"))
        filterDoc2 = {"Driver_Initial": init2}
        updateDoc2 = {"$set": {"Drivers_Championship_Position": newpos}}
        update(filterDoc2, updateDoc2, collection)
        cposCheck = input("Finished updating drivers? yes or no")
        if cposCheck.lower() == "yes": cpos = True
#Update Customer Drivers
    for customer in customerDriverList:
        finishC = customerDriverList.index(customer) + 1
        retC = input("Did driver " + str(customer) + " retire from the ePrix? Yes or No")
        if retC.lower() == "no": customerPoints = updatePoints(finishC)
        filterDocC = {"Driver_Initial": customer}
        updateDocC = {"$inc": {"Customer_Driver.Customer_Driver_Points": customerPoints}}
        update(filterDocC, updateDocC, collection)
        updateFinishC = {"$push": {"Customer_Driver.Customer_Finishes": finishC}}
        result = collection.update_one(filterDocC, updateFinishC, upsert=True)
        customerPoints = 0
    cursorC = collection.find({"Customer_Driver.Customer_Driver_Position":{"$gte":1}}, {"_id": 0, "Driver_Initial": 1, "Customer_Driver.Customer_Driver_Points": 1,
                                   "Customer_Driver.Customer_Driver_Position": 1,
                                   "Customer_Driver.Customer_Finishes": 1,}).sort("Customer_Driver.Customer_Driver_Points", pymongo.DESCENDING)
    docPosC = 1 
    for document in cursorC:
        print("Driver Initial: "+ str(document["Driver_Initial"])+ "\n"
               + "Points: "+ str(document["Customer_Driver"]["Customer_Driver_Points"])+ "\n"
               + "Old Championship Position: " + str(document["Customer_Driver"]["Customer_Driver_Position"]) + "\n"
               + "Finishes: "+ str(document["Customer_Driver"]["Customer_Finishes"]) + "\n"
               + "New Championship Position: " + str(docPosC) + "\n")
        docPosC += 1
    while posC != True:
        initC = input("Enter driver's initial to alter their championship position")
        newposC = int(input("Enter their new championship position:"))
        filterDocC2 = {"Driver_Initial": initC}
        updateDocC2 = {"$set": {"Customer_Driver.Customer_Driver_Position": newposC}}
        update(filterDocC2, updateDocC2, collection)
        posCCheck = input("Finished updating drivers? yes or no")
        if posCCheck.lower() == "yes": posC = True
#Update NPJT Drivers
    for npjt in npjtDriverList:
        finishN = npjtDriverList.index(npjt) + 1
        retN = input("Did driver " + str(npjt) + " retire from the ePrix? Yes or No")
        if retN.lower() == "no": npjtPoints = updatePoints(finishN)
        filterDocN = {"Driver_Initial": npjt}
        updateDocN = {"$inc": {"NPJT_Driver.NPJT_Driver_Points": npjtPoints}}
        update(filterDocN, updateDocN, collection)     
        updateFinishN = {"$push": {"NPJT_Driver.NPJT_Finishes": finishN}}
        result = collection.update_one(filterDocN, updateFinishN, upsert=True)
        npjtPoints = 0
    cursorN = collection.find({"NPJT_Driver.NPJT_Driver_Position":{"$gte":1}}, {"_id": 0, "Driver_Initial": 1, "NPJT_Driver.NPJT_Driver_Points": 1,
                                  "NPJT_Driver.NPJT_Driver_Position": 1, "NPJT_Driver.NPJT_Finishes": 1,}).sort("NPJT_Driver.NPJT_Driver_Points", pymongo.DESCENDING)
    docPosN = 1
    
    for document in cursorN:
        print("Driver Initial: "+ str(document["Driver_Initial"])+ "\n"
               + "Points: "+ str(document["NPJT_Driver"]["NPJT_Driver_Points"])+ "\n"
               + "Old Championship Position: " + str(document["NPJT_Driver"]["NPJT_Driver_Position"]) + "\n"
               + "Finishes: "+ str(document["NPJT_Driver"]["NPJT_Finishes"]) + "\n"
               + "New Championship Position: " + str(docPosN) + "\n")
        docPosN += 1
    while posN != True:
        initN = input("Enter driver's initial to alter their championship position")
        newposN = int(input("Enter their new championship position:"))
        filterDocN2 = {"Driver_Initial": initN}
        updateDocN2 = {"$set": {"NPJT_Driver.NPJT_Driver_Position": newposN}}
        update(filterDocN2, updateDocN2, collection)
        posNCheck = input("Finished updating drivers? yes or no")
        if posNCheck.lower() == "yes": posN = True        
#Update Team Result
def updateTeamResult(collection):
    points1 = 0
    points2 = 0
    customerTeamList = []
    teamPos = False
    teamPosC = False
#Update Overall Teams
    for x in range(11):
        init = input("Enter the team's initial to add their points")
        customer = input("Is the team a Customer Team: yes or no")
        if customer.lower() == "yes": customerTeamList.append(init)
        filterDoc = {"Team_Initial": init}
        pos1 = int(input("Enter the finishing position of the team's first car:"))
        retire1 = input("Did the car retire from the ePrix? Yes or No")
        if retire1.lower() == "no": points1 = updatePoints(pos1)
        pos2 = int(input("Enter the finishing position of the team's second car:"))
        retire2 = input("Did the car retire from the ePrix? Yes or No")
        if retire2.lower() == "no": points2 = updatePoints(pos2)
        points = points1 + points2
        updateDoc = {"$inc": {"Team_Points": points}}
        teamFinish = [pos1, pos2]
        updateFinish = {"$push": {"Team_Finishes": teamFinish}}
        result = collection.update_one(filterDoc, updateFinish, upsert=True)
        update(filterDoc, updateDoc, collection)
        points1 = 0
        points2 = 0
    cursor = collection.find({}, {"_id": 0, "Team_Initial": 1, "Team_Points": 1,
                                  "Teams_Championship_Position": 1, "Team_Finishes": 1}).sort("Team_Points", pymongo.DESCENDING)
    docPos = 1
    for document in cursor:
         print("Team Initial: "+ str(document["Team_Initial"])+ "\n"
               + "Points: "+ str(document["Team_Points"])+ "\n"
               + "Championship Position: "+ str(document["Teams_Championship_Position"]) + "\n"
               + "Finishes: "+ str(document["Team_Finishes"]) + "\n"
               + "New Championship Position: " +str(docPos) +"\n")
         docPos += 1
    while teamPos != True:
        init2 = input("Enter team's initial to alter their championship position")
        newpos = int(input("Enter their new championship position:"))
        filterDoc2 = {"Team_Initial": init2}
        updateDoc2 = {"$set": {"Teams_Championship_Position": newpos}}
        update(filterDoc2, updateDoc2, collection)
        teamPosCheck = input("Finished updating teams? yes or no")
        if teamPosCheck.lower() == "yes": teamPos = True
#Update Customer Teams
    for customer in customerTeamList:
        print(customer)
        filterDocC = {"Team_Initial": customer}
        posC1 = int(input("Enter the finishing position of the team's first car in the Customer class:"))
        retire1 = input("Did the car retire from the ePrix? Yes or No")
        if retire1.lower() == "no": points1 = updatePoints(posC1)
        posC2 = int(input("Enter the finishing position of the team's second car in the Customer class:"))
        retire2 = input("Did the car retire from the ePrix? Yes or No")
        #if retire2.lower() == "no": points2 = updatePoints(posC2)
        #customerPoints = points1
        updateDocC = {"$inc": {"Customer_Team.Customer_Team_Points": points1}}      
        teamFinishC = [posC1, posC2]
        updateFinishC = {"$push": {"Customer_Team.Customer_Team_Finishes": teamFinishC}}
        result = collection.update_one(filterDocC, updateFinishC, upsert=True)
        update(filterDocC, updateDocC, collection)
        points1 = 0
        points2 = 0
    cursorC = collection.find({"Customer_Team.Customer_Team_Position": {"$gte":1}}, {"_id": 0, "Team_Initial": 1, "Customer_Team.Customer_Team_Points": 1,
                                   "Customer_Team.Customer_Team_Position": 1,
                                   "Customer_Team.Customer_Team_Finishes": 1}).sort("Customer_Team.Customer_Team_Points", pymongo.DESCENDING)
    docPosC = 1
    for document in cursorC:
         print("Team Initial: "+ str(document["Team_Initial"])+ "\n"
               + "Points: "+ str(document["Customer_Team"]["Customer_Team_Points"])+ "\n"
               + "Championship Position: "+ str(document["Customer_Team"]["Customer_Team_Position"]) + "\n"
               + "Finishes: "+ str(document["Customer_Team"]["Customer_Team_Finishes"]) + "\n"
               + "New Championship Position: " +str(docPosC) +"\n")
         docPosC += 1
    while teamPosC != True:
        initC = input("Enter team's initial to alter their championship position")
        newposC = int(input("Enter their new championship position:"))
        filterDocC2 = {"Team_Initial": initC}
        updateDocC2 = {"$set": {"Customer_Team.Customer_Team_Position": newposC}}
        update(filterDocC2, updateDocC2, collection)
        teamPosCCheck = input("Finished updating teams? yes or no")
        if teamPosCCheck.lower() == "yes": teamPosC = True    
#Update Manufacturer Result
def updateManufacturerResult(collection):
    points1 = 0
    points2 = 0
    manuPos = False
    for x in range(6):
        init = input("Enter the manufacturer's initial to add their points")
        filterDoc = {"Manufacturer_Initial": init}  
        pos1 = int(input("Enter the finishing position of the manufacturer's first car:"))
        retire1 = input("Did the car retire from the ePrix? Yes or No")
        if retire1.lower() == "no": points1 = updatePoints(pos1)
        pos2 = int(input("Enter the finishing position of the manufacturer's second car:"))
        retire2 = input("Did the car retire from the ePrix? Yes or No")
        if retire2.lower() == "no": points2 = updatePoints(pos2)
        points = points1 + points2
        updateDoc = {"$inc": {"Manufacturer_Points": points}}
        update(filterDoc, updateDoc, collection) 
        manuFinish = [pos1, pos2]
        updateFinish = {"$push": {"Manufacturer_Finishes": manuFinish}}
        result = collection.update_one(filterDoc, updateFinish, upsert=True)
        points1 = 0
        points2 = 0
    cursor = collection.find({}, {"_id": 0, "Manufacturer_Initial": 1, "Manufacturer_Points": 1,
                                  "Manufacturers_Cup_Position": 1, "Manufacturer_Finishes": 1}).sort("Manufacturer_Points", pymongo.DESCENDING)
    docPos = 1
    for document in cursor:
         print("Manufacturer Initial: "+ str(document["Manufacturer_Initial"])+ "\n"
               + "Points: "+ str(document["Manufacturer_Points"])+ "\n"
               + "Cup Position: "+ str(document["Manufacturers_Cup_Position"]) + "\n"
               + "Finishes: "+ str(document["Manufacturer_Finishes"]) + "\n"
               + "New Championship Position: " +str(docPos) +"\n")
         docPos += 1
    while manuPos != True:
        init2 = input("Enter manufacturer's init to alter their championship position")
        newpos = int(input("Enter their new championship position:"))
        filterDoc2 = {"Manufacturer_Initial": init2}
        updateDoc2 = {"$set": {"Manufacturers_Cup_Position": newpos}}
        update(filterDoc2, updateDoc2, collection)
        manuPosCheck = input("Finished updating manufacturers? yes or no")
        if  manuPosCheck.lower() == "yes": manuPos = True
#Update Driver
def updateDriver(collection):
    initial = input("Enter the initial of the driver you wish to update:")
    filterDoc = {"Driver_Initial": initial}
    choice = int(input("Which field do you want to update: 1) Name" + "\n"
                       + "2) Driver_Initial" + "\n"
                       + "3) Team" + "\n"
                       + "4) Driver_Points" + "\n"
                       + "5) Drivers_Championship_Position" + "\n"
                       + "6) Customer_Driver_Points" + "\n"
                       + "7) Customer_Driver_Position" + "\n"
                       + "8) NPJT_Driver_Points" + "\n"
                       + "9) NPJT_Driver_Position"))
    if choice == 1:
        newName = input("Please enter the driver's updated name:")
        updateName = {"$set": {"Name":newName}}
        update(filterDoc, updateName, collection)
    elif choice == 2:
        newInitial = (input("Please enter the driver's updated initial:"))
        updateInitial = {"$set": {"Driver_Initial":newInitial}}
        update(filterDoc, updateInitial, collection)
    elif choice == 3:
        newTeam = input("Please enter the driver's updated team:")
        updateTeam = {"$set": {"Team":newTeam}}
        update(filterDoc, updateTeam, collection)
    elif choice == 4:
        newPoints = float(input("Please enter the driver's updated points total:"))
        updatePoints = {"$set": {"Driver_Points":newPoints}}
        update(filterDoc, updatePoints, collection)
    elif choice == 5:
        newPosition = int(input("Please enter the driver's updated championship position:"))
        updatePosition = {"$set": {"Drivers_Championship_Position":newPosition}}
        update(filterDoc, updatePosition, collection)
    elif choice == 6:
        result = collection.find_one({"$and":[{"Driver_Initial": initial}, {"Customer_Driver.Customer_Driver_Points" :{"$gte":0}}]})
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
    elif choice == 7:
        result = collection.find_one({"$and":[{"Driver_Initial": initial}, {"Customer_Driver.Customer_Driver_Position" :{"$gte":0}}]})
        newCustPosition = int(input("Please enter the driver's updated championship position for the Customer Trophy for Drivers:"))
        updateCustPosition = {"$set": {"Customer_Driver.Customer_Driver_Position":newCustPosition}}
        if type(result) != None:
            update(filterDoc, updateCustPosition, collection)
        else:
            cont = input("Field does not yet exist for driver document. Do you still wish to continue?: yes or no")
            if cont.lower() == "yes":
                result = collection.update_one(filterDoc, updateCustPosition, upsert = True)
                print("Documents updated: " + str(result.modified_count))
                print(collection.find_one(filterDoc))
    elif choice == 8:
        result = collection.find_one({"$and":[{"Driver_Initial": initial}, {"NPJT_Driver.NPJT_Driver_Points" :{"$gte":0}}]})
        newNPJTPoints = float(input("Please enter the driver's updated points total for the Nelson Piquet Jr Trophy:"))
        updateNPJTPoints = {"$set": {"NPJT_Driver.NPJT_Driver_Points":newNPJTPoints}}
        if type(result) != None:
            update(filterDoc, updateNPJTPoints, collection)
        else:
            cont = input("Field does not yet exist for driver document. Do you still wish to continue?: yes or no")
            if cont.lower() == "yes":
                result = collection.update_one(filterDoc, updateNPJTPoints, upsert = True)
                print("Documents updated: " + str(result.modified_count))
                print(collection.find_one(filterDoc))
    elif choice == 9:
        result = collection.find_one({"$and":[{"Driver_Initial": initial}, {"NPJT_Driver.NPJT_Driver_Position" :{"$gte":0}}]})
        newNPJTPosition = int(input("Please enter the driver's updated championship position for the Nelson Piquet Jr Trophy:"))
        updateNPJTPosition = {"$set": {"NPJT_Driver.NPJT_Driver_Position":newNPJTPosition}}
        if type(result) != None:
            update(filterDoc, updateNPJTPosition, collection)
        else:
            cont = input("Field does not yet exist for driver document. Do you still wish to continue?: yes or no")
            if cont.lower() == "yes":
                result = collection.update_one(filterDoc, updateNPJTPosition, upsert = True)
                print("Documents updated: " + str(result.modified_count))
                print(collection.find_one(filterDoc))
    else:
        print("Enter a number between 1 and 9, which corresponds with the field you would like to update")
    finished = input("Finished updating drivers? Yes or no")
    if finished.lower() == "yes": return True
#Update Team
def updateTeam(collection):
    initial = input("Enter the initial of the team you wish to update:")
    filterDoc = {"Team_Initial": initial}
    choice = int(input("Which field do you want to update: 1) Team_Name" + "\n"
                       + "2) Team_Initial" + "\n"
                       + "3) Manufacturer" + "\n"
                       + "4) Team_Points" + "\n"
                       + "5) Teams_Championship_Position" + "\n"
                       + "6) Customer_Team_Points" + "\n"
                       + "7) Customer_Team_Position"))
    if choice == 1:
        newName = input("Please enter the team's updated name:")
        updateName = {"$set": {"Team_Name":newName}}
        update(filterDoc, updateName, collection)
    elif choice == 2:
        newInitial = (input("Please enter the team's updated initial:"))
        updateInitial = {"$set": {"Team_Initial":newInitial}}
        update(filterDoc, updateInitial, collection)
    elif choice == 3:
        newManu = input("Please enter the team's updated manufacturer:")
        updateManu = {"$set": {"Manufacturer":newManu}}
        update(filterDoc, updateManu, collection)
    elif choice == 4:
        newPoints = float(input("Please enter the team's updated points total:"))
        updatePoints = {"$set": {"Team_Points":newPoints}}
        update(filterDoc, updatePoints, collection)
    elif choice == 5:
        newPosition = int(input("Please enter the team's updated championship position:"))
        updatePosition = {"$set": {"Teams_Championship_Position":newPosition}}
        update(filterDoc, updatePosition, collection)
    elif choice == 6:
        result = collection.find_one({"$and":[{"Team_Initial": initial}, {"Customer_Team.Customer_Team_Points" :{"$gte":0}}]})
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
    elif choice == 7:
        result = collection.find_one({"$and":[{"Team_Initial": initial}, {"Customer_Team.Customer_Team_Position" :{"$gte":0}}]})
        newCustPosition = int(input("Please enter the team's updated championship position for the Customer Teams Championship:"))
        updateCustPosition = {"$set": {"Customer_Team.Customer_Team_Position":newCustPosition}}
        if type(result) != None:
            update(filterDoc, updateCustPosition, collection)
        else:
            cont = input("Field does not yet exist for team document. Do you still wish to continue?: yes or no")
            if cont.lower() == "yes":
                result = collection.update_one(filterDoc, updateCustPosition, upsert = True)
                print("Documents updated: " + str(result.modified_count))
                print(collection.find_one(filterDoc))
    else:
        print("Enter a number between 1 and 7, which corresponds with the field you would like to update")
    finished = input("Finished updating teams? Yes or no")
    if finished.lower() == "yes": return True
#Update Manufacturer
def updateManufacturer(collection):
    initial = input("Enter the initial of the manufacturer you wish to update:")
    filterDoc = {"Manufacturer_Initial": initial}
    choice = int(input("Which field do you want to update: 1) Manufacturer_Name" + "\n"
                       + "2) Manufacturer_Initial" + "\n"
                       + "3) Manufacturer_Points" + "\n"
                       + "4) Manufacturers_Cup_Position"))
    if choice == 1:
        newName = input("Please enter the manufacturer's updated name:")
        updateName = {"$set": {"Manufacturer_Name":newName}}
        update(filterDoc, updateName, collection)
    elif choice == 2:
        newInitial = (input("Please enter the manufacturer's updated initial:"))
        updateInitial = {"$set": {"Manufacturer_Initial":newInitial}}
        update(filterDoc, updateInitial, collection)
    elif choice == 3:
        newPoints = float(input("Please enter the manufacturer's updated points total:"))
        updatePoints = {"$set": {"Manufacturer_Points":newPoints}}
        update(filterDoc, updatePoints, collection)
    elif choice == 4:
        newPosition = int(input("Please enter the manufacturer's updated cup position:"))
        updatePosition = {"$set": {"Manufacturers_Cup_Position":newPosition}}
        update(filterDoc, updatePosition, collection)
    else:
        print("Enter a number between 1 and 4, which corresponds with the field you would like to update")
    finished = input("Finished updating manufacturers? Yes or no")
    if finished.lower() == "yes": return True
#Read Driver Championships results
def readDriverResult(collection):
    choice = int(input("Which Driver Championship do you wish to view: 1) Overall Drivers' Championship" + "\n"
                       + "2) Customer Trophy for Drivers" + "\n"
                       + "3) Nelson Piquet Jr Trophy"))
    if choice == 1:
        results = collection.find({}).sort("Drivers_Championship_Position", pymongo.ASCENDING)
        for document in results:
            print("Name:"+ str(document["Name"])+ "\n"
                  + "Points: "+ str(document["Driver_Points"])+ "\n"
                  + "Championship Position: "+ str(document["Drivers_Championship_Position"]) + "\n"
                  + "Finishes: "+ str(document["Finishes"]) + "\n") 
    elif choice == 2:
        results = collection.find({"Customer_Driver.Customer_Driver_Points": {"$gte":0}}).sort("Customer_Driver.Customer_Driver_Position", pymongo.ASCENDING)
        for document in results:
            print("Name:"+ str(document["Name"])+ "\n"
                  + "Points: "+ str(document["Customer_Driver"]["Customer_Driver_Points"])+ "\n"
                  + "Championship Position: "+ str(document["Customer_Driver"]["Customer_Driver_Position"]) + "\n"
                  + "Finishes: "+ str(document["Customer_Driver"]["Customer_Finishes"]) + "\n")
    elif choice == 3:
        results = collection.find({"NPJT_Driver.NPJT_Driver_Points": {"$gte":0}}).sort("NPJT_Driver.NPJT_Driver_Position", pymongo.ASCENDING)
        for document in results:
            print("Name:"+ str(document["Name"])+ "\n"
                  + "Points: "+ str(document["NPJT_Driver"]["NPJT_Driver_Points"])+ "\n"
                  + "Championship Position: "+ str(document["NPJT_Driver"]["NPJT_Driver_Position"]) + "\n"
                  + "Finishes: "+ str(document["NPJT_Driver"]["NPJT_Finishes"]) + "\n")
    else:
        print("Incorrect input. Please enter either 1 or 2 or 3 to view a driver championship when asked")
    finished = input("Finished viewing driver championship results? Yes or no")
    if finished.lower() == "yes": return True
#Read Team Championships results
def readTeamResult(collection):
    choice = int(input("Which Team Championship do you wish to view: 1) Overall Teams' Championship" + "\n"
                       + "2) Customer Teams' Championship"))
    if choice == 1:
        results = collection.find({}).sort("Teams_Championship_Position", pymongo.ASCENDING)
        for document in results:
            print("Name:"+ str(document["Team_Name"])+ "\n"
                  + "Points: "+ str(document["Team_Points"])+ "\n"
                  + "Championship Position: "+ str(document["Teams_Championship_Position"]) + "\n"
                  + "Finishes: "+ str(document["Team_Finishes"]) + "\n")
    elif choice == 2:
        results = collection.find({"Customer_Team.Customer_Team_Points": {"$gte":0}}).sort("Customer_Team.Customer_Team_Position", pymongo.ASCENDING)
        for document in results:
            print("Name:"+ str(document["Team_Name"])+ "\n"
                  + "Points: "+ str(document["Customer_Team"]["Customer_Team_Points"])+ "\n"
                  + "Championship Position: "+ str(document["Customer_Team"]["Customer_Team_Position"]) + "\n"
                  + "Finishes: "+ str(document["Customer_Team"]["Customer_Team_Finishes"]) + "\n")
    else:
        print("Incorrect input. Please enter either 1 or 2 to view a team championship when asked")
    finished = input("Finished viewing team championship results? Yes or no")
    if finished.lower() == "yes": return True
#Read Manufacturer Championship results
def readManufacturerResult(collection):
    results = collection.find({}).sort("Manufacturers_Cup_Position", pymongo.ASCENDING)
    for document in results:
        print("Name:"+ str(document["Manufacturer_Name"])+ "\n"
              + "Points: "+ str(document["Manufacturer_Points"])+ "\n"
              + "Cup Position: "+ str(document["Manufacturers_Cup_Position"]) + "\n"
              + "Finishes: "+ str(document["Manufacturer_Finishes"]) + "\n")
    finished = input("Finished viewing manufacturer championship results? Yes or no")
    if finished.lower() == "yes": return True
#Read Driver
def readDriver(collection):
    driver = input("Please enter the Driver Initial of the driver you wish to view:")
    result = collection.find_one({"Driver_Initial":driver})
    print(result)
    finished = input("Finished viewing drivers? Yes or no")
    if finished.lower() == "yes": return True
#Read Team
def readTeam(collection):
    team = input("Please enter the Team Initial of the team you wish to view:")
    result = collection.find_one({"Team_Initial":team})
    print(result)
    finished = input("Finished viewing teams? Yes or no")
    if finished.lower() == "yes": return True
#Read Manufacturer
def readManufacturer(collection):
    manufacturer = input("Please enter the Manufacturer Initial of the manufacturer you wish to view:")
    result = collection.find_one({"Manufacturer_Initial":manufacturer})
    print(result)
    finished = input("Finished viewing manufacturers? Yes or no")
    if finished.lower() == "yes": return True
#Delete Driver
def deleteDriver(collection):
    driver = input("Enter the ObjectId of the Driver document you wish to delete")
    docToDelete = {"_id": ObjectId(driver)}
    confirm = input(str(collection.find_one(docToDelete)) + "\n" + "Do you wish to delete this document? Please enter Yes or No")
    if confirm == "Yes":
        result = collection.delete_one(docToDelete)
        print(collection.find_one(docToDelete))
        print("Documents deleted: " + str(result.deleted_count))
    else:
        print("Document will not be deleted. If this is not intended outcome, Please try again.")
    finished = input("Finished deleting drivers? Yes or no")
    if finished.lower() == "yes": return True
#Delete Team
def deleteTeam(collection):
    team = input("Enter the ObjectId of the Team document you wish to delete")
    docToDelete = {"_id": ObjectId(team)}
    confirm = input(str(collection.find_one(docToDelete)) + "\n" + "Do you wish to delete this document? Please enter Yes or No")
    if confirm == "Yes":
        result = collection.delete_one(docToDelete)
        print(collection.find_one(docToDelete))
        print("Documents deleted: " + str(result.deleted_count))
    else:
        print("Document will not be deleted. If this is not intended outcome, Please try again.")
    finished = input("Finished deleting teams? Yes or no")
    if finished.lower() == "yes": return True
#Delete Manufacturer
def deleteManufacturer(collection):
    manufacturer = input("Enter the ObjectId of the Manufacturer document you wish to delete")
    docToDelete = {"_id": ObjectId(manufacturer)}
    confirm = input(str(collection.find_one(docToDelete)) + "\n" + "Do you wish to delete this document? Please enter Yes or No")
    if confirm == "Yes":
        result = collection.delete_one(docToDelete)
        print(collection.find_one(docToDelete))
        print("Documents deleted: " + str(result.deleted_count))
    else:
        print("Document will not be deleted. If this is not intended outcome, Please try again.")
    finished = input("Finished deleting manufacturers? Yes or no")
    if finished.lower() == "yes": return True
