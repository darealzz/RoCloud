from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from dateutil.parser import parse as parse_datetime

from .user import BaseUser
from .utils import BASE_VERSION_TWO
from .utils.session import Session
from .utils.base_object import BaseObject

if TYPE_CHECKING:
    from .client import Client

class BaseGroup(BaseObject):
    def __init__(self, client: Client, id: int):        
        self._client = client
        self.id = id
    
    async def extend(self):
        return await self._client.get_group(self.id)
    
        
class Group(BaseGroup):
    def __init__(self, client: Client, data: dict):
        
        id = int(data.get('id'))
          
        super().__init__(client, id)
        
        self._client: Client = client
        
        self.id: int = id
        self.path: str = data.get('path')
        self.create_time: datetime = parse_datetime(data.get('createTime'))
        self.update_time: datetime = parse_datetime(data.get('updateTime'))
        self.display_name: str = data.get('displayName')
        self.description: str = data.get('description')
        self.member_count: int = int(data.get('memberCount'))
        self.public_entry_allowed: bool = data.get('publicEntryAllowed')
        self.locked: bool = data.get('locked')
        self.verified: bool = data.get('verified')

        owner = data.get('owner')
        self.owner: Optional[int] = BaseUser._from_path(client, owner) if owner else None

        
class JoinRequest:
    pass

class Membership:
    pass

class Role:
    pass

class Shout:
    pass