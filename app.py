from flask import Flask, request, render_template
from summarizer import summarize_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    submitted_text = ''
    if request.method == 'POST':
        text = request.form.get('text')
        length_option = request.form.get('length')
        if text and length_option:
            submitted_text = text
            result = summarize_text(text, length_option)
    return render_template('index.html', result=result, submitted_text=submitted_text)

if __name__ == '__main__':
    app.run(debug=False)