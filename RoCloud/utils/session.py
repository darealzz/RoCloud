import requests

from . import VERSION_LOOKUP
from .exceptions import _error_code_to_exception


class Session(requests.Session):
    def __init__(self, api_key: str) -> None:
        super().__init__()
        self.api_key = api_key
        self.headers.update({'x-api-key': api_key, 'Content-Type': 'application/json'})

    def _request(self, method: str, base_url: str, endpoint: str, **kwargs):
        full_url = base_url + endpoint
        response = super().request(method, full_url, kwargs)

        if response.status_code == 200:
            return response
                
        reason = ''
        content_type = response.headers.get('content-type')
        if content_type == 'application/json':
            reason = response.json()['message']
        else:
            reason = response.reason or 'Unknown Error'
        
        exception = _error_code_to_exception(VERSION_LOOKUP[base_url], response.status_code)
        raise exception(reason)

    def get(self, base_url: str, endpoint: str, **kwargs):
        return self._request('GET', base_url, endpoint, **kwargs)

    def post(self, base_url: str, endpoint: str, **kwargs):
        return self._request('POST', base_url, endpoint, **kwargs)

    def patch(self, base_url: str, endpoint: str, **kwargs):
        return self._request('PATCH', base_url, endpoint, **kwargs)

    def delete(self, base_url: str, endpoint: str, **kwargs):
        return self._request('DELETE', base_url, endpoint, **kwargs)