#Azure IoT Hub connection and receiving messages
from iothub_client import IotHubClient, IoTHubTransportProvider
from iothub_client import IotHubMessage, IotHubMessageDispositionResult
from iothub_client import IotHubClientRetryPolicy

TIMEOUT = 241000
MINIMUM_POLLING_TIME = 9
#messageTimeout - the maximum time in milliseconds until a message times out.
#the timeout period starts at IoTHubClient.send_event_async
#By default, messages do not expite.
MESSAGE_TIMEOUT = 10000
#chose HTTP, AMQP, AMQP_WS or MQTT
PROTOCOL = IoTHubTransportProvider.MQTT

#String containing Hostname, Device Id & Device Key in the foramt:
#"HostName = <host_name>"; DeviceId = <device_id>;SharedAccessKey = <device_key>"
try:
    CONNECTION_STRING = os.environ["CONNECTION_STRING"]
except KeyError:
    pass

def receive_message_callback(message, counter):
    message_buffer = message.get_bytearray()
    size = len(message_buffer)
    msg = message_buffer[:size].decode('utf-8')
    if(msg == "image"):
        postblob()
    return IotHubMessageDispositionResult.ACCEPTED

def iothub_client_init():
    #prepare iothub client
    client = IotHubClient(CONNECTION_STRING, PROTOCOL)
    if client.protocol ==IoTHubTransportProvider.HTTP:
        client.setOption("timeout", TIMEOUT)
        client.setOption("MinimumPollingTime", MINIMUM_POLLING_TIME)
    #set the time until a message times out
    client.set_option("messageTimeout", MESSAGE_TIMEOUT)
    #to enable MQTT logging set to 1
    if client.protocol == IoTHubTransportProvider.MQTT:
        client.set_option("logtrace", 0)
    client.set_message_callback(
        receive_message_callback, 0)
    retryPolicy = IotHubClientRetryPolicy.RETRY_INTERVAL
    retryInterval = 100
    client.set_retry_policy(retryPolicy, retryInterval)
    return client
