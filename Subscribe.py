import wiotp.sdk.application
import time, json
import random

myConfig = {
    "auth":{
        "token":"----------",
        "key":"------------"        
    }
}

def myCommandCallback(cmd):
    print("command received: %s" % cmd.data)

client = wiotp.sdk.application.ApplicationClient(config = myConfig)

def myEventCallback(event):
    str = "%s event '%s' received from device [%s]: %s"
    print(str % (event.format, event.eventId, event.device, json.dumps(event.data)))

client.connect()
client.deviceEventCallback = myEventCallback
client.subscribeToDeviceEvents()
