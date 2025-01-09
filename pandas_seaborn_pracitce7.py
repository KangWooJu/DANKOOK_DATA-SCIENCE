import matplotlib.pyplot as plt 
import plotly.graph_objects as go 
import pandas as pd 
import matplotlib.image as mpimg

def rader(df,fills,min_max,title=''):
    fig = go.Figure() 
    scores = df.iloc[i,:].to_list()
    scores.append(scores[0])
    fig.add_trace(go.Scatterpolar(
        r = scores,
        theta = categories,
        fill = fills[i],
        name = df.index[i]
    ))
    i += 1
    
    fig.update_layout(
        polar_radialaxis_visible = True,
        polar_radialaxis_range = min_max,
        showlegend = True,
        margin_t = 50,
    )
    
    