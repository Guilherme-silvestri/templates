from src.adapters.log.LogBookProvider import LogProvider
from src.adapters.external_resources.dm_proxy_api_cards.DMCardProxyAPI import DMCardProxyAPIService

logger = None
card_api = None

class APIResources:
    def __init__(self) -> None:
        self.logger = LogProvider()
        self.card_api = DMCardProxyAPIService()

    def shutdown_resources(self):
        self.logger = None #logger shutdown process here
        self.card_api = None #card_api shutdown process here
