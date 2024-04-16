from .group import Group
from .utils import BASE_VERSION_TWO
from .utils.session import Session


class Client:
    def __init__(self, api_key: str):
        self._session = Session(api_key)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}>'

    def get_group(self, id: int) -> Group:
        response = self._session.get(BASE_VERSION_TWO, f'/groups/{id}')
        return Group(self, response.json())
    
    def get_universe(): pass
    def get_place(): pass
    def get_instance(): pass
    def get_subscription(): pass
    def get_user(): pass
    def get_inventory(): pass
    def get_notification(): pass
    def get_assets(): pass
    def get_data_store(): pass
    def get_messages(): pass
    def publish_place(): pass


# q = Client('KMhOKiRcLUucnXBPNZmEkzmxPrlL0zebdHKjMpbZaPEWw1M4')
# q.get_group(1)
# q.get_group('asd')


# # for i in range(500)
# x = q._request('GET', f'cloud/v2/groups/13183519')
# print(x.headers)
# print(x.json())
# print(x.status_code)
