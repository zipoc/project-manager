from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    trello_api_key: str = Field(..., env="TRELLO_API_KEY")
    trello_api_token: str = Field(..., env="TRELLO_API_TOKEN")
    trello_board_id: str = Field(..., env="TRELLO_BOARD_ID")
    trello_list_id: str = Field(None, env="TRELLO_LIST_ID")

    class Config:
        env_file = ".env"

settings = Settings()
