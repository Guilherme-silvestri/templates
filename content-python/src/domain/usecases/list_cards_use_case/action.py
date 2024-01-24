from src.domain.usecases.list_cards_use_case.input import ListAllCardsInput
from src.domain.usecases.list_cards_use_case.output import ListCardsOutput
from src.domain.ports.cards_provider import CardsProviderInterface
from src.domain.ports.logprovider import LogProviderInterface

class ListAllCardsV1UseCase:
    def __init__(self, logProvider: LogProviderInterface, cardsProvider: CardsProviderInterface):
        self.logger = logProvider
        self.cards_provider = cardsProvider

    def search_customer_cards(self, input_data: ListAllCardsInput) -> ListCardsOutput:
        try:
            self.logger.info(f"Iniciando Busca de Cartões para o CPF")
            cards = self.cards_provider.ListCards(input_data)
            return cards
        except Exception:
            self.logger.critical(f"Erro ao realizar consulta para o CPF: {input_data.tax_id}")
