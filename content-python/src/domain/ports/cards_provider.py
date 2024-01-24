import abc
from src.domain.usecases.list_cards_use_case.input import ListAllCardsInput
from src.domain.usecases.list_cards_use_case.output import ListCardsOutput

class CardsProviderInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ListCards(self, input: ListAllCardsInput) -> ListCardsOutput:
        raise NotImplementedError
