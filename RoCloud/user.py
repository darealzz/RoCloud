from __future__ import annotations

from typing import TYPE_CHECKING

from .utils.base_object import BaseObject

if TYPE_CHECKING:
    from .client import Client

class BaseUser(BaseObject):
    def __init__(self, client: Client, id: int):        
        self._client = client
        self.id = id