import wiotp.sdk.device
import time
import random

myConfig = {
    "identity":{
        "orgId":"----",
        "typeId":"type",
        "deviceId":"type-3"
    },
    "auth":{
        "token":"-----"
    }
}

def myCommandCallback(cmd):
    print("command received: %s" % cmd.data)

client = wiotp.sdk.device.DeviceClient(config = myConfig)

client.connect()

while True:
    myData = {'category' : 'client device', 'message':'alarme cerca eletrica'}
    client.publishEvent(eventId="operational issues",msgFormat="json", data=myData, qos=0, onPublish=None)
    client.commandCallBack = myCommandCallback
    time.sleep(10)