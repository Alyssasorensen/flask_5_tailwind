from flask import Flask, render_template

app = Flask(__name__)

# Sample data for the sections and descriptions
sections = [
    {"id": 1, "section_name": "0:05", "description": "Program director of the online MS in healthcare informatics talks about the program at UCF"},
]

@app.route('/')
def index():
    return render_template('index_tailwind.html', items=sections)

if __name__ == '__main__':
    app.run(debug=True)
