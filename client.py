import requests
import json
import time
#import gate

url = 'https://stormy-badlands-80104.herokuapp.com/api/status'

#api
response = requests.get(url)
status = response.json()
print(status['IsClosed'])
print(status['ShouldBeClosed'])

#API
def updateApiJson(is_closed, should_be_closed):
    statusDict = {'IsClosed': is_closed, 'ShouldBeClosed': should_be_closed}
    newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    postResponse = requests.post(url, data = json.dumps(statusDict), headers=newHeaders)
    print(postResponse)
    print(json.dumps(statusDict))

#LOCAL
def updateLocalJson(is_closed, should_be_closed):
    statusDict = {'IsClosed': is_closed, 'ShouldBeClosed': should_be_closed}
    with open('status.json', 'w') as json_file:
        json.dump(statusDict, json_file)

while(True):
    #API
    time.sleep(1)
    response = requests.get(url)
    status = response.json()
    print(status['IsClosed'])
    print(status['ShouldBeClosed'])

    with open('status.json') as json_file:
        data = json.load(json_file)
        #isclosed = data['IsClosed']
        #shouldbeclosed = data['ShouldBeClosed']
        isclosed = status['IsClosed']
        shouldbeclosed = status['ShouldBeClosed']

    if isclosed == True and shouldbeclosed == True:
        print("Gate is closed")
    elif isclosed == True and shouldbeclosed == False:
        print("Gate is opening")
        updateApiJson(False, shouldbeclosed)
    elif isclosed == False and shouldbeclosed == False:
        print("Gate is open")
    elif isclosed == False and shouldbeclosed == True:
        print("Gate is closing")
        updateApiJson(True, shouldbeclosed)
