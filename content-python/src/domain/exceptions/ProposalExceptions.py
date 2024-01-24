class BaseNotFoundException(Exception):
    def __init__(self, param: str, message: str):
        self.param = param
        self.message = message

class ProposalNotFoundException(BaseNotFoundException):
    def __init__(self, param: str):
        super().__init__(param, "Nenhuma proposta encontrada com o CPF informado")
