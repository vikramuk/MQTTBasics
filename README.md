# MQTTBasics
https://raw.githubusercontent.com/owntracks/tools/master/TLS/generate-CA.sh

Create Certificates:
openssl genrsa -des3 -out ca.key 2048

openssl req -new -x509 -days 1826 -key ca.key -out ca.crt

openssl genrsa -out server.key 2048

openssl req -new  -key server.key -out server.csr

openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 360

openssl verify -CAfile ca.crt server.crt

mosquitto_pub -h host.name -u username -P password -t test/topic -p 8883 –cafile ~/keys/ca.crt -m message

aws iot get-registration-code

openssl genrsa -out verificationCert.key 2048

openssl req -new -key verificationCert.key -out verificationCert.csr

mosquitto_pub --cafile C:\ssl\ca.crt --cert C:\ssl\client.crt --key C:\ssl\client.key -d -h a3h6jjcgxk2mdj-ats.iot.ap-southeast-1.amazonaws.com -p 8883 -t test -m "hello there" 

mosquitto_pub --cafile /etc/mosquitto/certs/ca.crt --cert user1.crt --key user1.key  -d  -h a3h6jjcgxk2mdj-ats.iot.ap-southeast-1.amazonaws.com  -p 8883 -t "test" -m "message"

openssl x509 -req -in verificationCert.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out verificationCert.pem -days 500 -sha256

openssl s_client -showcerts -connect hostname:443 < /dev/null
