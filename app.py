from flask import Flask, request, render_template

app = Flask(__name__)
entries = []

@app.route('/', methods=['GET', 'POST'])
def diary():
    if request.method == 'POST':
        date = request.form['date']
        content = request.form['content']
        entries.append({'date': date, 'content': content})
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
