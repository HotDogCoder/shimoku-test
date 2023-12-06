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
s.set_menu_path('catalog', 'Custom Line Chart')

# https://echarts.apache.org/examples/en/editor.html?c=line-style
raw_options: str = """
    {
  xAxis: {
    type: 'category',
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      data: [120, 200, 150, 80, 70, 110, 130],
      type: 'line',
      symbol: 'triangle',
      symbolSize: 20,
      lineStyle: {
        color: '#5470C6',
        width: 4,
        type: 'dashed'
      },
      itemStyle: {
        borderWidth: 3,
        borderColor: '#EE6666',
        color: 'yellow'
      }
    }
  ]
};
"""

s.plt.free_echarts(
    raw_options=raw_options,
    order=2, rows_size=2, cols_size=12,
)