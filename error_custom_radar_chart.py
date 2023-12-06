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
s.set_menu_path('catalog', 'Custom Radar Chart')

# https://echarts.apache.org/examples/en/editor.html?c=line-style
raw_options: str = """
{
  title: {
    text: 'Basic Radar Chart'
  },
  legend: {
    data: ['Allocated Budget', 'Actual Spending']
  },
  radar: {
    // shape: 'circle',
    indicator: [
      { name: 'Sales', max: 6500 },
      { name: 'Administration', max: 16000 },
      { name: 'Information Technology', max: 30000 },
      { name: 'Customer Support', max: 38000 },
      { name: 'Development', max: 52000 },
      { name: 'Marketing', max: 25000 }
    ]
  },
  series: [
    {
      name: 'Budget vs spending',
      type: 'radar',
      data: [
        {
          value: [4200, 3000, 20000, 35000, 50000, 18000],
          name: 'Allocated Budget'
        },
        {
          value: [5000, 14000, 28000, 26000, 42000, 21000],
          name: 'Actual Spending'
        }
      ]
    }
  ]
};
"""

s.plt.free_echarts(
    raw_options=raw_options,
    order=2, rows_size=2, cols_size=12,
)