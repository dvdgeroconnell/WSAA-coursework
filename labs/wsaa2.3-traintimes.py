
from xml.dom.minidom import parseString
import requests
import csv

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)
# check it works
# newl='' gets rid of the new lines when printing
print (doc.toprettyxml(newl='')) #output to console

# if I want to store the xml in a file
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)


# I had an issue with blank lines in the file so found solution at
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
# adding the newline= '' parameter
with  open('week02_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        #traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        #traincode = traincodenode.firstChild.nodeValue.strip()
        #print (traincode)

        # now lets get everything
        dataList = []
        flag = False
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            print(f"Train Object tags are {retrieveTag}")
            dataList.append(datanode.firstChild.nodeValue.strip())
            # this print shows each line being incrementally built
            print(f"{dataList}")
            # only store train codes beginning with 'D'
            if retrieveTag == 'TrainCode' and datanode.firstChild.nodeValue[0] == 'D':
                flag = True
    
        # instead of printing this you could output to another format
        #print (dataList)
        # for example a CSV file
        # in this case we're only storing train codes beginning with 'D'  
        if flag:
            train_writer.writerow(dataList)

