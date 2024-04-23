import dash
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div(children=[

    ################
    # Introduction #
    ################
    html.H1(children='Exploring the Intersection of COVID-19, Overdoses, and Pharmaceutical Market Dynamics ', className='header'),
    html.H3(children='Group 21: Karston Kuciemba, Ananya Kaalva, & Carolyn Pyun',
            className='subheader'),


    ######################
    # Purpose of Project #
    ######################
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

    ###########
    # Chart 1 #
    ###########
    html.Iframe(srcDoc=open("vis1.html").read(), id='graph1',
                className='chart'),
    html.Ul(children=[
        html.Li(children=[
                'There are 2 key notes in this - Moderna (MRNA) and Eli Lilly & Co (LLY)'], className='list-item'),
        html.Ul(children=[
            html.Li(children=[
                    'Both vaccine producers, seemingly produced marginally significant returns when compared to their competitors in the industry even before they were announced to release a vaccine'], className='sublist-item'),
            html.Li(children=[
                    'Other vaccine producers, such as Pfizer (PFE) and JNJ, did not have near the result as the other producers, which leads me to question the significance that COVID had on these results'], className='sublist-item'),
        ], className='list'),
        html.Li(children=['sample item'], className='list-item'),
    ]),


    ###########
    # Chart 2 #
    ###########
    html.Iframe(srcDoc=open("vis2.html").read(), id='graph2',
                className='special-chart'),
    html.Ul(children=[
        html.Li(children=['sample item'], className='list-item'),
        html.Li(children=['sample item'], className='list-item'),
        html.Li(children=['sample item'], className='list-item'),
    ]),

    ###########
    # Chart 3 #
    ###########
    html.Iframe(srcDoc=open("vis3.html").read(), id='graph3',
                className='chart'),
    html.Ul(children=[
        html.Li(children=['sample item'], className='list-item'),
        html.Li(children=['sample item'], className='list-item'),
        html.Li(children=['sample item'], className='list-item'),
    ]),

    ###########
    # Chart 4 #
    ###########
    html.Iframe(srcDoc=open("vis4.html").read(), id='graph4',
                className='special-chart'),
    html.Ul(children=[
        html.Li(children=['sample item'], className='list-item'),
        html.Li(children=['sample item'], className='list-item'),
        html.Li(children=['sample item'], className='list-item'),
    ]),


    ###########
    # Chart 5 #
    ###########
    html.Iframe(srcDoc=open("vis5.html").read(), id='graph5',
                className='final-chart'),
    html.Ul(children=[
        html.Li(children=['sample item'], className='list-item'),
        html.Li(children=['sample item'], className='list-item'),
        html.Li(children=['sample item'], className='list-item'),
    ]),
], className='chart-wrapper')

if __name__ == '__main__':
    app.run_server(debug=True)
