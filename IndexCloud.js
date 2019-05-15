#https://devblog.axway.com/apis/api-builder-and-mqtt-for-iot-part-1/
var mqtt = require('mqtt');
var client  = mqtt.connect('mqtt://mshdyanl:XXYY@m23.cloudmqtt.com:16570');

client.on('connect', function () {
  console.log('client connected');
  client.publish('myhome', 'Hello from publisher');
});
