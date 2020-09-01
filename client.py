import requests
import json
import time
#import gate

#response = requests.get('')
#status = response.json()
#print(status['IsClosed'])

with open('status.json') as json_file:
    data = json.load(json_file)
    isclosed = data['IsClosed']
    shouldbeclosed = data['ShouldBeClosed']

    while(True):
        time.sleep(1)
        #response = requests.get('')
        #status = response.json()
        #print(status['IsClosed'])
        #print(status['ShouldBeClosed'])

        with open('status.json') as json_file:
            data = json.load(json_file)
            isclosed = data['IsClosed']
            shouldbeclosed = data['ShouldBeClosed']
        
        if isclosed == True and shouldbeclosed == True:
            print("Gate is closed")
        if isclosed == True and shouldbeclosed == False:
            print("Gate is opening")
            #gate.open_close()
        if isclosed == False and shouldbeclosed == False:
            print("Gate is open")
        if isclosed == False and shouldbeclosed == True:
            print("Gate is closing")
            #gate.open_close()

#TODO: MAKE POST REQUESTS TO API WITH DATA
#TODO: UPDATE LOCAL JSON
#TODO: PUT THIS ALL TOGETHER