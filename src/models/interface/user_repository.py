from typing import Tuple
from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):

    @abstractmethod
    def registry_user(self, username: str, password: str) -> None: pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> Tuple[int, int, str]: pass

    @abstractmethod
    def get_order_by_user(self, username: str) -> Tuple[int, str, str, str]: pass
