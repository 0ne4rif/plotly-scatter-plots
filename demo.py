import plotly
import plotly.graph_objects as go
import pandas as pd

csv_file = 'Time.csv'
df = pd.read_csv(csv_file)

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['date'], y=df['confirmed'], mode='line+markers', name='Positive'))
fig.add_trace(go.Scatter(x=df['date'], y=df['released'], mode='markers', name='Released'))
fig.add_trace(go.Scatter(x=df['date'], y=df['deceased'], mode='line', name='Deceased'))
fig.update_layout(
    title="Covid-19 Cases in South Korea",
    xaxis_title="Date",
    yaxis_title="Number of Cases",
)
fig.show()
plotly.offline.plot(fig, filename="CaseReport.html")