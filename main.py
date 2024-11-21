import asyncio
from services.project_service import ProjectService


async def main():
    print("Initializing Trello Board...")
    lists = await ProjectService.initialize_board()
    for lst in lists:
        print(f"- {lst.name} (ID: {lst.id})")


if __name__ == "__main__":
    asyncio.run(main())
