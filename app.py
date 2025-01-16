from flask import Flask, render_template, request, jsonify
from khalil_7osni_alayoubi_super_agent import Khalil7osniAlayoubiSuperAgent, BaseAgent

app = Flask(__name__)
khalil_7osni_alayoubi = Khalil7osniAlayoubiSuperAgent()

# Register agents
agent1 = BaseAgent("Demand Forecaster")
agent2 = BaseAgent("Supplier Finder")
khalil_7osni_alayoubi.register_agent(1, agent1)
khalil_7osni_alayoubi.register_agent(2, agent2)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = khalil_7osni_alayoubi.delegate_task(1, user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5002, debug=True)
