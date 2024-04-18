from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import Client

class BaseObject:
    id = None
    
    def __repr__(self) -> str:
        attributes = ''
        for key, value in self.__dict__.items():
            if key[0] != '_':
                attributes += f'{key}={value}'
                
        return f'<{self.__class__.__name__} {attributes}>'

    @classmethod
    def _from_path(cls, client: Client, path: str): 
        return cls(client, int(path.split('/')[-1]))