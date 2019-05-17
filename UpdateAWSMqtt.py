import time
import os
#import motor_runner
#import net_check
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
#https://cloudncode.blog/2017/11/07/make-your-first-iot-device-via-aws-iot-service-and-raspberry-pi/
def run_motor(self, params, packet):
	motor_runner.pulse(2)
	myMQTTClient.publish('$aws/things/RpiTest1/shadow/get', packet.payload, 0)
 
myMQTTClient = AWSIoTMQTTClient("raspberryPiHome") #random key, if another connection using the same key is opened the previous one is auto closed by AWS IOT
 
myMQTTClient.configureEndpoint("a3h6jjcgxk2mdj-ats.iot.ap-southeast-1.amazonaws.com", 8883)
 
certRootPath = 'C:\\ProgApps\\Mosquitto\\Test\\aws-iot-device-sdk-python\\'
myMQTTClient.configureCredentials("{}rootCA.pem".format(certRootPath), "{}087ec6e9eb-private.pem.key".format(certRootPath), "{}087ec6e9eb-certificate.pem.crt".format(certRootPath))
 
myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
 
myMQTTClient.connect()
myMQTTClient.subscribe("$aws/things/RpiTest1/shadow/update", 1, run_motor)
 
def looper():
	while True:
		time.sleep(5) #sleep for 5 seconds and then sleep again
	#check_internet()	 
		looper()
 
def function_handler(event, context):
	return
