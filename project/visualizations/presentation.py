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
                    'Analyzing the impact COVID deaths had on the performance of different pharmaceutical stocks'], className='sublist-item'),
            html.Li(children=[
                    'Analyzing the relationship between drug overdoses and pharmaceutical market trends - any significance?'], className='sublist-item'),
        ], className='list'),
        html.Li(children=[
                'Vaccine producers will perform significantly better when compared to non-vaccine producing counterparts.'], className='list-item'),
        html.Li(children=[
                'Overdoses are seen as negligible to pharmaceutical companies’ bottom line (or stock price)'], className='list-item'),
    ]),

    ###########
    # Chart 1 #
    ###########
    html.H3(children='Visualization 1', className='vis-header'),
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
    html.H3(children='Visualization 2', className='vis-header'),
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
    html.H3(children='Visualization 3', className='vis-header'),
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
    html.H3(children='Visualization 4', className='vis-header'),
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
    html.H3(children='Visualization 5', className='vis-header'),
    html.Iframe(srcDoc=open("vis5.html").read(), id='graph5',
                className='final-chart'),
    html.Ul(children=[
        html.Li(children=['sample item'], className='list-item'),
        html.Li(children=['sample item'], className='list-item'),
        html.Li(children=['sample item'], className='list-item'),
    ]),

    ########################
    # Conclusion & Results #
    ########################
    html.H3(children='Conclusion & Results', className='vis-header'),
    html.Div(children=[
        html.Div(children=[
            html.Ul(children=[
                html.Li(children=[
                    'We cannot determine with confidence that pharmaceutical companies react in a specific way to any type of news. The market is seemingly speculative and reacts in unique ways. '], className='list-item'),
                html.Ul(children=[
                    html.Li(children=[
                        'Correlation & Confidence ->'], className='sublist-item'),
                ], className='list'),
                html.Li(children=[
                    'Nature of "Priced in"'], className='list-item'),
                html.Li(children=[
                    "If COVID reactions can't be explained, how can something else?"], className='list-item'),
            ]),
            html.Img(src='../assets/stonks.png', className='joke-pics'),
            html.Img(src='../assets/notstonks.png', className='joke-pics'),
        ], className='conclusion-list'),
        html.Img(src='../assets/covid-stats.png', className='result-image'),
    ], className='conclusion-container'),

], className='chart-wrapper')

if __name__ == '__main__':
    app.run_server(debug=True)
