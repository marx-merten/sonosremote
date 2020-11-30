import uasyncio
import utime
import logging

LOG = logging.getLogger("WifiManager")


class WifiManager:
    def __init__(self, connect_timeout=10, portal_timeout=60*5, portal_name="SonosRemote", hostname="SonosRemote"):
        self.timeout = connect_timeout
        self.ssid = portal_name
        self.portal_timeout = portal_timeout
        self.known_networks = {}
        self.hostname = hostname

    def add_network(self, name, password):
        self.known_networks[name] = password

    def start_network(self):
        loop = uasyncio.get_event_loop()
        loop.create_task(self.connect_or_manage())

    async def connect_or_manage(self):
        LOG.debug("Try to connect on "+self.ssid)
        await uasyncio.sleep_ms(2000)
        LOG.debug("done ?")
        await uasyncio.sleep_ms(2000)
        LOG.debug("Finished")
