"""UC-XXXX-XXXX · Use-Case PoC — Plotly Dash PoC.

Run: python app.py   (from the poc/ directory), then open http://127.0.0.1:8050
Reads its own data/sample.csv, so it runs offline. Not production data.
Layout follows the Plotly Dash minimal app (https://dash.plotly.com/minimal-app).
"""
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, callback, dcc, html

df = pd.read_csv("data/sample.csv", parse_dates=["period"])
LINES = sorted(df["category"].unique())

app = Dash(__name__)
app.title = "UC-XXXX-XXXX · Use-Case PoC"
server = app.server  # gunicorn entrypoint

app.layout = html.Div(
    className="wrap",
    children=[
        html.H1("Use-Case PoC"),
        html.P("PoC for UC-XXXX-XXXX · PLANT · process — proof-of-concept, not production data.", className="sub"),
        dcc.Dropdown(LINES, LINES, multi=True, id="lines"),
        html.Div(
            className="charts",
            children=[dcc.Graph(id="trend"), dcc.Graph(id="by-line")],
        ),
    ],
)


@callback(Output("trend", "figure"), Output("by-line", "figure"), Input("lines", "value"))
def update(lines):
    kept = df[df["category"].isin(lines or LINES)]
    trend = kept.groupby("period", as_index=False)["value"].sum()
    by_cat = kept.groupby("category", as_index=False)["value"].sum()
    return (
        px.line(trend, x="period", y="value", title="Trend"),
        px.bar(by_cat, x="category", y="value", title="By line"),
    )


if __name__ == "__main__":
    app.run(debug=True)
