from http import HTTPStatus

from fastapi import APIRouter, Path
from src.api.V1.exceptions.ValidationException import NotFoundErrorModel, ValidationErrorModel
from src.domain.usecases.list_cards_use_case.action import ListAllCardsV1UseCase
from src.domain.usecases.list_cards_use_case.input import ListAllCardsInput
from src.api.V1.models.CardListOutputModel import ListCardsOutput
from fastapi import FastAPI
from src.api.resources import APIResources

router = APIRouter(
    tags=["cards"],
    responses={
        HTTPStatus.UNPROCESSABLE_ENTITY.value: {"model": ValidationErrorModel},
        HTTPStatus.NOT_FOUND.value: {"model": NotFoundErrorModel},
    },
)

@router.get(
    "/cards/{tax_id}",
    summary="Listar Cartões",
    description="Lista todos os cartões do cliente pelo número do documento (CPF)",
    response_model=ListCardsOutput,
)
async def get_cards_by_tax_id(    
    tax_id: str = Path(...),    
):
    resources = APIResources()
    usecase = ListAllCardsV1UseCase(logProvider=resources.logger, 
                                    cardsProvider=resources.card_api)
    imput = ListAllCardsInput()
    imput.tax_id = tax_id
    cards = usecase.search_customer_cards(imput)
    return cards