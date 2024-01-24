import abc
from typing import List

from models.proposal.account_request import proposal

class ProposalRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, proposal: proposal) -> proposal:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, proposal: proposal) -> proposal:
        raise NotImplementedError