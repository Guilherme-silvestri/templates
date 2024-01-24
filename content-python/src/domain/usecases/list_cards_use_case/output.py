from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel

class ButtonRule(BaseModel):
    name: str
    visible: bool

class CardOutput(BaseModel):
    id: str
    company_name: str
    is_expired: bool
    expiration_date: str
    status: str
    button_rules: List[ButtonRule]
    card: str
    password_created: bool
    created_at: str
    better_shop_day: float
    total_limit: float
    used_limit: float
    company_id: int
    card_type: str
    provisional_card_link: str
    is_provisional: bool
    closing_invoice_date: str
    invoice_expiration_date: str


class ListCardsOutput(BaseModel):
    message: List[Any]
    notice: List[Any]
    data: Optional[Union[List[CardOutput], Dict]]
    token: Optional[str]