from src.domain.ports.cards_provider import CardsProviderInterface
from src.domain.usecases.list_cards_use_case.input import ListAllCardsInput
from src.domain.usecases.list_cards_use_case.output import ListCardsOutput
from src.domain.usecases.list_cards_use_case.output import CardOutput

class DMCardProxyAPIService(CardsProviderInterface):
    def __init__(self):
        pass
    
    def map_data():
        cards = []

        card = CardOutput(
            id = "ssdad",
            company_name = "ssdad",
            is_expired = "ssdad",
            expiration_date = "ssdad",
            status = "ssdad",
            button_rules = "ssdad",
            card = "ssdad",
            password_created = "ssdad",
            created_at = "ssdad",
            better_shop_day = "ssdad",
            total_limit = "ssdad",
            used_limit = "ssdad",
            company_id = "ssdad",
            card_type = "ssdad",
            provisional_card_link = "ssdad",
            is_provisional = "ssdad",
            closing_invoice_date = "ssdad",
            invoice_expiration_date = "ssdad",
        )
        cards.append(card)

        return cards

    def ListCards(self, input: ListAllCardsInput) -> ListCardsOutput:
        result = ListCardsOutput()
        result.message = ["Hello World!"]
        result.data = self.map_data()
        result.notice = []
        result.token = []
        return result
