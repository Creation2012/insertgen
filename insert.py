import sys
import random as rnd

#INSERT INTO `CarModels` (`CarModelID`, `CarModelName`, `ManufacturerID`, `CarTypesCarTypeID`) VALUES 
# (NULL, 'test', '1', '20'); 

tables = {
        '`CarModels`': ['`CarModelID`','`CarModelName`','`ManufacturerID`', '`CarTypesCarTypeID`'],
        '`Cars`': ['`CarID`', '`Color`', '`CarModelsCarModelID`', '`EnginePower`', '`DailyLendingPrice`', '`NeedMaintance`', '`Active`', '`AdditionalInfo`'],
        '`Clients`': ['`ClientID`', '`ClientDrivingLicense`', '`PreviousOrders`', '`Verified`'],
        '`Employees`': ['`EmployeeID`', '`JobID`', '`LentCars`'],
        '`Human`': ['`HumanID`', '`FirstName`', '`LastName`', '`EmailAddress`', '`PhoneID`', '`Login`', '`Password`', '`AdditionalInfo`'],
        '`Orders`': ['`OrderID`', '`ClientID`', '`EmployeeID`', '`CarID`', '`StartDate`', '`EndDate`', '`OrderStatus`', '`FullLeningPrice`', '`AdditionalInfo`'],
        '`Phones`': ['`PhoneID`','`PhoneNumber`', '`BackupPhoneNumber`']
}

# python insert.py i [table_name] 3-1-25
num = sys.argv[1]
table = sys.argv[2]

insert = "INSERT INTO {} (".format(table)
for i in tables['`'+sys.argv[2]+'`']:
    insert += i +','

insert = insert[:len(insert)-1]+") VALUES \n"

ranges = {}

for i in sys.argv[3:]:
    temp = i.strip().split('-')
    temp = list(map(int,temp))
    ranges[temp[0]-1] = range(temp[1],temp[2]+1)
    
unique = rnd.sample(range(1,int(num)+2),int(num)+1)

for i in range(1,int(num)+1):
    insert += "(NULL,"
    for n, col in enumerate(tables['`'+sys.argv[2]+'`']):
        if n == 0:
            continue

        if n in ranges:
            insert += '\''+str(rnd.sample(ranges[n],1)[0])+'\','
        else:
            insert += '\''+ str(unique[i])  +'\','

    insert = insert[:len(insert)-1] + "),\n"

insert = insert[:len(insert)-2]
f = open("output.txt","w")
f.write(insert)