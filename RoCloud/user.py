from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .client import Client

class BaseUser:
    def __init__(self, client: Client, id: int):
        self._client: Client = client
        self.id: int = id

    def get_full_user(self): pass