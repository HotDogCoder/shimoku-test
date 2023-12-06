from os import getenv
import shimoku_api_python as Shimoku

access_token = getenv('SHIMOKU_TOKEN')
universe_id: str = getenv('UNIVERSE_ID')
workspace_id: str = getenv('WORKSPACE_ID')

s = Shimoku.Client(
    access_token=access_token,
    universe_id=universe_id,
    verbosity='INFO',
    async_execution=False,
)

s.set_workspace(uuid=workspace_id)

s.boards.force_delete_board(name='Custom Board')

s.boards.force_delete_board(name='Default Board')

s.boards.force_delete_board(name='Demmo Board')