from os import getenv
import shimoku_api_python as Shimoku
import datetime as dt

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
s.set_board('Demo Board')
s.set_menu_path('Modal Test')
s.plt.set_modal(modal_name='Test modal', open_by_default=True, width=90, height=90)

modal_header = s.html_components.create_h1_title_with_modal(
    title='Modal title', subtitle='Modal subtitle',
    background_color='var(--chart-C5)'
)
s.plt.html(html=modal_header, order=0)

s.plt.set_tabs_index(tabs_index=('Test', 'Tab 1'), order=1)
s.plt.html(html=modal_header, order=0)

data_ = [
    {'date': dt.date(2021, 1, 1), 'x': 5, 'y': 5, 'filtA': 'A', 'filtB': 'Z', 'name': 'Ana'},
    {'date': dt.date(2021, 1, 2), 'x': 6, 'y': 5, 'filtA': 'B', 'filtB': 'Z', 'name': 'Laura'},
    {'date': dt.date(2021, 1, 3), 'x': 4, 'y': 5, 'filtA': 'A', 'filtB': 'W', 'name': 'Audrey'},
    {'date': dt.date(2021, 1, 4), 'x': 7, 'y': 5, 'filtA': 'B', 'filtB': 'W', 'name': 'Jose'},
    {'date': dt.date(2021, 1, 5), 'x': 3, 'y': 5, 'filtA': 'A', 'filtB': 'Z', 'name': 'Jorge'},
]

s.plt.table(
    title="Test-table",
    data=data_,
    order=2,
)
s.plt.pop_out_of_tabs_group() 
s.plt.pop_out_of_modal()

s.plt.modal_button(order=0, modal='Test modal', label='Open modal')