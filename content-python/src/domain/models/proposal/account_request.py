import datetime

class client:
    name: str
    tax_id: str
    document_type: str
    birth_date: datetime

class location:
    type: str
    coordinates: dict

class proposal:
    client: client
    geo_location: location
    status: str
