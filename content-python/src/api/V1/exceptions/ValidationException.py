from pydantic import BaseModel

class ValidationErrorItemModel(BaseModel):
    field: str
    error: str

class NotFoundErrorItemModel(BaseModel):
    message: str
    param: str

class NotFoundErrorModel(BaseModel):
    errors: list[NotFoundErrorItemModel]

class ValidationErrorItemModel(BaseModel):
    field: str
    error: str

class ValidationErrorModel(BaseModel):
    errors: list[ValidationErrorItemModel]