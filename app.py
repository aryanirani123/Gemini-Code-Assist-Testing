import json
from flask import Flask, render_template

app = Flask(__name__)

def load_event_data():
    """Loads event data from the JSON file."""
    try:
        with open('event_data.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Error: event_data.json not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Could not decode event_data.json.")
        return None

@app.route('/')
def index():
    event_data = load_event_data()
    event_info = event_data.get('eventInfo', {}) if event_data else {}
    talks = event_data.get('talks', []) if event_data else []
    return render_template('index.html', event_info=event_info, talks=talks)

if __name__ == '__main__':
    app.run(debug=True)