# pip install dash
# to run: python dashDemo3Data.py
# View on your browser at http://127.0.0.1:8050/
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components import Br
from numpy import append
import plotly.express as px
import dash_table
import pandas as pd
from readDB import ReadMongoData as db

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app = dash.Dash("app")

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = db.getBookingDetails()

# Convert the Decimal128 columns to float to work for the dash_table.DataTable
df[["BasePrice", "AgencyCommission"]] = df[[
    "BasePrice", "AgencyCommission"]].astype(str).astype(float)

# # Summary for sales
# df_base_price = df.groupby(["BasePrice"]).sum()[
#     ["RegionId", "TripStart"]]
fig = px.scatter(df, x="TripStart", y="BasePrice", color="RegionId")
fig1 = px.pie(df, values="BasePrice", names="RegionId", color="RegionId")
fig2 = px.pie(df, values="AgencyCommission", names="RegionId", color="RegionId")
fig3 = px.bar(df, x="TripStart", y="AgencyCommission", color="RegionId")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

fig3.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(children=[
    html.Div([
        html.A(href='/', children='Sales Performance Data'),
        html.H1(children='Travel Experts Sales data',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }),
        html.Div(children='TravelExperts Booking details table with a bar chart of showing the sales per trip start.',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }),
        html.Br(),
        html.Div([
            dash_table.DataTable(
                id='mytable',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                page_size=10
            ),
        ]),
    ], className='row'),

    html.Div([
        html.Div([
            html.H3(children='Scatter plot Chart Showing sales per region',
            ),
            html.Br(),
            dcc.Graph(id='graph1', figure=fig)
        ], className='six columns'),

        html.Div([
            # html.A(href='/', children='Sales Performance Data'),
            html.H3(children='Pie Chart shows Sales Distribution',
                style={
                    # 'textAlign': 'center',
                    # 'color': colors['text']
                }),
            html.Br(),
                dcc.Graph(id='graph2', figure=fig1)
        ], className='six columns'),
    ], className='row'),

    html.Div([
        html.Div([
            html.H4(children='Pie Chart shows Agency Commission Distribution',
            ),
            html.Br(),
            dcc.Graph(id='graph3', figure=fig2)
        ], className='six columns'),

        html.Div([
            # html.A(href='/', children='Sales Performance Data'),
            html.H4(children='Bar Chart Showing Agency Commission per region',
                style={
                    # 'textAlign': 'center',
                    # 'color': colors['text']
                }),
            html.Br(),
                dcc.Graph(id='graph4', figure=fig3)
        ], className='six columns'),
    ], className='row'),
])
        


# if __name__ == '__main__':
app.run_server(debug=True)