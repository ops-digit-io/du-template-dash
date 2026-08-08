# UC-XXXX-XXXX · Dash PoC

PoC for UC-XXXX-XXXX · PLANT · process — proof-of-concept, not production data.

Follows the [Plotly Dash minimal app](https://dash.plotly.com/minimal-app) — a
callback drives the charts from the line filter.

```bash
cd poc
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py            # http://127.0.0.1:8050
gunicorn app:server      # production (see Procfile)
```
