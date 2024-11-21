from typing import List, Optional
from pydantic import BaseModel
import httpx
from config.settings import settings


class TrelloList(BaseModel):
    id: str
    name: str


class TrelloConnector:
    BASE_URL = "https://api.trello.com/1"

    @staticmethod
    async def get_lists() -> List[TrelloList]:
        url = f"{TrelloConnector.BASE_URL}/boards/{settings.trello_board_id}/lists"
        params = {
            "key": settings.trello_api_key,
            "token": settings.trello_api_token,
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return [TrelloList(**lst) for lst in response.json()]

    @staticmethod
    async def create_list(name: str):
        url = f"{TrelloConnector.BASE_URL}/lists"
        params = {
            "key": settings.trello_api_key,
            "token": settings.trello_api_token,
            "name": name,
            "idBoard": settings.trello_board_id,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, params=params)
            response.raise_for_status()
            return response.json()
