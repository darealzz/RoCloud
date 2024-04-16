from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from dateutil.parser import parse as parse_datetime

from .user import BaseUser
from .utils import BASE_VERSION_TWO
from .utils.session import Session

from .utils.general_functions import _parse_path
if TYPE_CHECKING:
    from .client import Client


class Group:
    def __init__(self, client: Client, data: dict):  
        self._client: Client = client

        self.path: str = data.get('path')
        self.create_time: datetime = parse_datetime(data.get('createTime'))
        self.update_time: datetime = parse_datetime(data.get('updateTime'))
        self.id: int = int(data.get('id'))
        self.display_name: str = data.get('displayName')
        self.description: str = data.get('description')
        self.member_count: int = int(data.get('memberCount'))
        self.public_entry_allowed: bool = data.get('publicEntryAllowed')
        self.locked: bool = data.get('locked')
        self.verified: bool = data.get('verified')

        owner_id_or_none = _parse_path(data.get('owner', ''))
        self.owner: Optional[int] = BaseUser(client, owner_id_or_none) if owner_id_or_none else None

    def get_members(self, *, limit=None, role_id=None):
        response = self._session.get(BASE_VERSION_TWO, f'/')
        return Group(self, response.json())

    def get_join_requests(): pass
    def get_roles(): pass
    def get_shout(): pass

        
class GroupJoinRequest:
    pass

class GroupMembership:
    pass

class GroupRole:
    pass

class GroupShout:
    pass