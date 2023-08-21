import openai
from flask import Flask, render_template, request, jsonify

# Replace 'YOUR_OPENAI_API_KEY' with your actual API key
api_key = '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'
openai.api_key = api_key

app = Flask(__name__)

def get_medical_answer(question):
    prompt = f"Question: {question}\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        stop=["\n"]
    )
    return response.choices[0].text.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_question = request.form['user_question']
        answer = get_medical_answer(user_question)
        return jsonify({'bot_response': answer})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=8443)
