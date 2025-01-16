import threading
import logging
from transformers import pipeline

# === הגדרות בסיסיות ===
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s', handlers=[logging.StreamHandler()])

class Khalil7osniAlayoubiSuperAgent:
    def __init__(self):
        self.agents = {}
        self.model = pipeline("fill-mask")  # Load the BERT model for masked language modeling
        self.responses = {
            "hi": "Hello! How can I assist you today?",
            "hiii": "Hi there! What can I do for you?",
            "hello": "Greetings! How may I help you?",
            "bye": "Goodbye! Have a great day!",
            "exit": "Exiting chat. Goodbye!",
            "how are you?": "I'm just a program, but thanks for asking!",
            "what's your name?": "I'm Khalil's assistant, here to help you!"
        }

    def register_agent(self, agent_id, agent_object):
        """רישום סוכן חדש"""
        self.agents[agent_id] = agent_object
        logging.info(f"Agent {agent_id} registered.")

    def monitor_agents(self):
        logging.info("Monitoring agents...")  # Ensure status is logged
        """ניטור פעילות הסוכנים"""
        for agent_id, agent_object in self.agents.items():
            status = agent_object.get_status()
            logging.info(f"Agent {agent_id} status: {status}")  # Ensure status is logged

    def delegate_task(self, agent_id, task):
        logging.info(f"Delegating task to Agent {agent_id}...")  # Ensure task delegation is logged
        """העברת משימה לסוכן מסוים"""
        if agent_id in self.agents:
            if task.lower() in self.responses:
                return self.responses[task.lower()]  # Return predefined response
            if task.lower() in self.responses:
                return self.responses[task.lower()]  # Return predefined response
            result = self.agents[agent_id].execute_task(task)
            logging.info(f"Task delegated to Agent {agent_id}. Result: {result}")
            # Example of using the BERT model for a task
            result = self.model(f"{task} <mask>")  # Using the model to predict with a mask token
            logging.info(f"Task prediction result: {result}")
            return result
        else:
            logging.warning(f"Agent {agent_id} not found.")

# === מחלקת סוכן בסיסית לדוגמה ===
class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.status = "Idle"

    def get_status(self):
        return self.status

    def execute_task(self, task):
        self.status = f"Executing {task}"
        # סימולציה של ביצוע משימה
        threading.Timer(2.0, self.complete_task).start()
        return f"Started {task}"

    def complete_task(self):
        self.status = "Idle"

# === דוגמה לשימוש בסוכן-על ===
if __name__ == "__main__":
    # יצירת סוכן-על
    khalil_7osni_al_ayoubi = Khalil7osniAlayoubiSuperAgent()

    # רישום סוכנים
    agent1 = BaseAgent("Demand Forecaster")
    agent2 = BaseAgent("Supplier Finder")
    khalil_7osni_al_ayoubi.register_agent(1, agent1)
    khalil_7osni_al_ayoubi.register_agent(2, agent2)

    # ניטור פעילות הסוכנים
    khalil_7osni_al_ayoubi.monitor_agents()

    # העברת משימות לסוכנים
    khalil_7osni_al_ayoubi.delegate_task(1, "Forecast next month's demand")
    khalil_7osni_al_ayoubi.delegate_task(2, "Find new suppliers")

    # ניטור נוסף לאחר המשימות
    threading.Timer(3.0, khalil_7osni_al_ayoubi.monitor_agents).start()

    # Chat functionality
    print("Chat with your agent! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = khalil_7osni_al_ayoubi.delegate_task(1, user_input)  # Delegate the user input as a task
        print(f"Agent: {response}")
