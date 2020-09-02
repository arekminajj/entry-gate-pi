import requests
import json
import time
import gate

url = 'https://stormy-badlands-80104.herokuapp.com/api/status'

response = requests.get(url)
status = response.json()
print(status['IsClosed'])
print(status['ShouldBeClosed'])

def updateApiJson(is_closed, should_be_closed):
    statusDict = {'IsClosed': is_closed, 'ShouldBeClosed': should_be_closed}
    newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    postResponse = requests.post(url, data = json.dumps(statusDict), headers=newHeaders)
    print(postResponse)
    print(json.dumps(statusDict))

#STILL GOT IT HERE CUZ I MAY USE IT IN THE FUTURE.
def updateLocalJson(is_closed, should_be_closed):
    statusDict = {'IsClosed': is_closed, 'ShouldBeClosed': should_be_closed}
    with open('status.json', 'w') as json_file:
        json.dump(statusDict, json_file)

while(True):    
    time.sleep(1)
    response = requests.get(url)
    status = response.json()
    print(status['IsClosed'])
    print(status['ShouldBeClosed'])

    with open('status.json') as json_file:
        data = json.load(json_file)
        isclosed = status['IsClosed']
        shouldbeclosed = status['ShouldBeClosed']

    if isclosed == True and shouldbeclosed == True:
        print("Gate is closed")
    elif isclosed == True and shouldbeclosed == False:
        gate.openclose(21) # OPEN THE GATE!
        print("Gate is opening")
        updateApiJson(False, shouldbeclosed)
    elif isclosed == False and shouldbeclosed == False:
        print("Gate is open")
    elif isclosed == False and shouldbeclosed == True:
        gate.openclose(21) #CLOSE DA GATE!
        print("Gate is closing")
        updateApiJson(True, shouldbeclosed)
