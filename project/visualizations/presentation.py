import dash
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Exploring the Intersection of COVID-19, Overdoses, and Pharmaceutical Market Dynamics ', className='header'),
    html.H3(children='Group 21: Karston Kuciemba, Ananya Kaalva, & Carolyn Pyun',
            className='subheader'),
    html.H3(children='Purpose & Hypothesis: ',
            className='section-header'),
    html.Ul(children=[
        html.Li(children=[
                'Explore the impact of COVID-19 & overdoses on the pharmaceutical industry through:'], className='list-item'),
        html.Ul(children=[
            html.Li(children=[
                    'Analyzing the impact on the performance of ETFs and different pharmaceutical stocks'], className='sublist-item'),
            html.Li(children=[
                    'Analyzing the relationship between drug overdoses and pharmaceutical market trends'], className='sublist-item'),
        ], className='list'),
        html.Li(children=[
                'Vaccine producers will perform significantly better when compared to non-vaccine producing counterparts.'], className='list-item'),
        html.Li(children=[
                'Overdoses are seen as negligible to pharmaceutical companies’ bottom line (or stock price)'], className='list-item'),
    ]),


    html.Iframe(srcDoc=open("vis1.html").read(), id='graph1',
                className='chart'),
    html.Ul(children=[
        html.Li(children=['item 23'], className='list-item'),
        html.Li(children=['item 23'], className='list-item'),
        html.Li(children=['item 23'], className='list-item'),
    ]),

    html.Iframe(srcDoc=open("vis2.html").read(), id='graph2',
                className='chart'),
    html.Ul(children=[
        html.Li(children=['item 2'], className='list-item'),
        html.Li(children=['item 23'], className='list-item'),
        html.Li(children=['item 23'], className='list-item'),
    ]),

    html.Iframe(srcDoc=open("vis3.html").read(), id='graph3',
                style={"height": "400px", "width": "800px"}),
    html.Ul(children=[
        html.Li(children=['item 23'], className='list-item'),
        html.Li(children=['item 23'], className='list-item'),
        html.Li(children=['item 23'], className='list-item'),
    ]),

    html.Iframe(srcDoc=open("vis4.html").read(), id='graph4',
                style={"height": "400px", "width": "800px"}),
    html.Ul(children=[
        html.Li(children=['item 23'], className='list-item'),
        html.Li(children=['item 23'], className='list-item'),
        html.Li(children=['item 23'], className='list-item'),
    ]),

    html.Iframe(srcDoc=open("vis5.html").read(), id='graph5',
                style={"height": "400px", "width": "800px"}),
    html.Ul(children=[
        html.Li(children=['item 23'], className='list-item'),
        html.Li(children=['item 23'], className='list-item'),
        html.Li(children=['item 23'], className='list-item'),
    ]),
], className='chart-wrapper')

if __name__ == '__main__':
    app.run_server(debug=True)
