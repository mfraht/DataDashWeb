# pip install dash
# to run: python dashDemo2.py
# View on your browser at http://127.0.0.1:8050/
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# app = dash.Dash(__name__)
app = dash.Dash("app")

df = pd.DataFrame(data={
    "weekDays": ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "avgSales": [1560, 1350, 850, 740, 834, 787, 940]
})

fig = px.pie(df, names="weekDays", values="avgSales")  # Pie chart figure

app.layout = html.Div(
    children=[
        html.H1(children='Average week day sales'),
        html.Div(children=[
            'Example Pie chart demo DIV ',
            html.B(style={"color": "red"},
                   children='This is sample average sales data for each week day.')
        ]),
        dcc.Graph(
            id='my-graph',
            figure=fig
        )
    ])

# if __name__ == '__main__':
app.run_server(debug=True)
