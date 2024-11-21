from connectors.trello_connector import TrelloConnector


class ProjectService:
    @staticmethod
    async def initialize_board():
        required_lists = ["TO DO", "IN PROGRESS", "DONE"]
        existing_lists = await TrelloConnector.get_lists()
        existing_names = [lst.name for lst in existing_lists]

        for lst in required_lists:
            if lst not in existing_names:
                await TrelloConnector.create_list(lst)
        return await TrelloConnector.get_lists()
