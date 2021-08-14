# pip install dash
# to run: python dashDemo1.py
# View on your browser at http://127.0.0.1:8050/
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# app = dash.Dash(__name__)
app = dash.Dash("app")

fig = px.bar([2, 3, 1, 10])  # Bar chart figure

app.layout = html.Div(children=[
    html.H1(children='This is my bar chart'),
    html.Div(children='Example bar chart demo DIV'),
    dcc.Graph(
        id='bar-graph',
        figure=fig
    )
])

# if __name__ == '__main__':
app.run_server(debug=True)
