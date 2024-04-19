from __future__ import annotations

import asyncio
from typing import Type

import httpx
from httpx import AsyncClient

from . import VERSION_LOOKUP
from .exceptions import _error_code_to_exception

class Session:
    def __init__(self, api_key: str) -> None:
        super().__init__()  
        
        self.session = AsyncClient()
        self.loop = asyncio.get_event_loop()
        self.session.headers = {'x-api-key': api_key, 'Content-Type': 'application/json'}

    def __del__(self):
        self.loop.create_task(self.session.aclose())
    
    async def _request(self, method: str, base_url: str, endpoint: str, **kwargs) -> Type[httpx.Response]:
        
        full_url = base_url + endpoint
        
        response = await self.session.request(method, full_url, **kwargs)

        if response.status_code == 200:
            return response
                
        reason = ''
        content_type = response.headers.get('content-type')
        if content_type == 'application/json':
            reason = response.json()['message']
        else:
            reason = response.reason_phrase or 'Unknown Error'
        
        exception = _error_code_to_exception(VERSION_LOOKUP[base_url], response.status_code)
        raise exception(reason)


    async def get(self, base_url: str, endpoint: str, **kwargs):
        return await self._request('GET', base_url, endpoint, **kwargs)

    async def post(self, base_url: str, endpoint: str, **kwargs):
        return await self._request('POST', base_url, endpoint, **kwargs)

    async def patch(self, base_url: str, endpoint: str, **kwargs):
        return await self._request('PATCH', base_url, endpoint, **kwargs)

    async def delete(self, base_url: str, endpoint: str, **kwargs):
        return await self._request('DELETE', base_url, endpoint, **kwargs)