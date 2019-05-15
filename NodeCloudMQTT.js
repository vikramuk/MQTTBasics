var cloudMQTTUrl = 'mqtt://mshdyanl:XXYY@m23.cloudmqtt.com:16570';
var mqtt = require('mqtt');
var client;
var deviceId;

require('getmac').getMac(function(err, macAddress){
    if (err)  throw err;
    deviceId = macAddress;
    console.log(deviceId);
    client  = mqtt.connect(cloudMQTTUrl,
    {
      clientId: deviceId,
      will: {
        topic: 'myhome/server/will',
        payload: deviceId
      },
      keepalive: 60
    });

    client.on('connect', function () {
      console.log('client connected');
      message = JSON.stringify({
        deviceId:deviceId,
        temp : 70 + 5*Math.random() -2.5
      });
      client.publish('myhome/server', message);
    });

    setInterval(function(){
      console.log('sending ...');
      message = JSON.stringify({
        deviceId:deviceId,
        temp : 70 + 5*Math.random() -2.5
      });
      client.publish('myhome/server', message);
    }, 15000);

});
