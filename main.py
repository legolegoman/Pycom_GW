""" LoPy LoRaWAN Nano Gateway example usage """

import config
import pycom
from nanogateway import NanoGateway

pycom.heartbeat(False)
pycom.rgbled(0x1f0000) # red

if __name__ == '__main__':
    nanogw = NanoGateway(
        id=config.GATEWAY_ID,
        frequency=config.LORA_FREQUENCY,
        datarate=config.LORA_GW_DR,
        ssid=config.WIFI_SSID,
        password=config.WIFI_PASS,
        server=config.SERVER,
        port=config.PORT,
        ntp_server=config.NTP,
        ntp_period=config.NTP_PERIOD_S
        )

    nanogw.start()
    nanogw._log('You may now press ENTER to enter the REPL')
    pycom.rgbled(0x001f00) # green
    input()
