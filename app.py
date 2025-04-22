from flask import Flask, request, render_template_string

app = Flask(__name__)
entries = []

TEMPLATE = '''
<h1>My Dream Diary</h1>
<form method="POST">
    <label>Date: <input type="text" name="date"></label><br><br>
    <label>Content:</label><br>
    <textarea name="content" rows="5" cols="30"></textarea><br>
    <button type="submit">Add Entry</button>
</form>

<h2>All Entries</h2>
{% for entry in entries %}
    <p><strong>Date:</strong> {{ entry.date }}<br>
    <strong>Content:</strong> {{ entry.content }}</p>
{% else %}
    <p>No entries yet.</p>
{% endfor %}
'''

@app.route('/', methods=['GET', 'POST'])
def diary():
    if request.method == 'POST':
        date = request.form['date']
        content = request.form['content']
        entries.append({'date': date, 'content': content})
    return render_template_string(TEMPLATE, entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
