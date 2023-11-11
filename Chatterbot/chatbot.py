from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

botname = 'Mika'

chatbot = ChatBot(botname,
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                    logic_adapters=[#"chatterbot.logic.MathematicalEvaluation",
                                  # "chatterbot.logic.TimeLogicAdapter",

                                  # "chatterbot.logic.BestMatch",
                                  # "chatterbot.logic.UnitConversion",
                                  {
                                      'import_path': 'chatterbot.logic.BestMatch',
                                      'default_response': "Sorry! I don't understand",
                                      'maximum_similarity_threshold': 0.30
                                  },
                                  # {
                                  #     'import_path': 'chatterbot.logic.TimeLogicAdapter',
                                  # },

                                  {
                                      'import_path': 'chatterbot.logic.UnitConversion',
                                  },
                                  {
                                      'import_path': 'chatterbot.logic.MathematicalEvaluation',
                                  },
                                  {
                                      "import_path": "profanity_adapter.ProfanityAdapter",
                                  },
                  ],
                  database_uri='sqlite:///database.sqlite3'
                  )

trainer = ChatterBotCorpusTrainer(chatbot)
trainer2 = ListTrainer(chatbot)

trainer.train("chatterbot.corpus.english")
trainer2.train([
    "Hi, can I help you?",
    "Yes, tell me about HCMC Open University",
    "Established in 1990 and become a public university in 2006, Ho Chi Minh City Open University now appears to be one of the high-ranking public universities in Vietnam. It would be the first open university in Vietnam and be governed by the Ministry of Education and Training.Ho Chi Minh City Open University would have professional environment, multidisciplinary courses, and full responsibilities for training undergraduate and graduate students by offering them with formal training, continuing education and satellite training sites. Most prevalent courses would be taught by qualified local and international lecturers with an emphasis on applied research. As such, a number of seminars and conferences have been organized, providing students with a great opportunity to present their research findings and to access to the professional learning network."
])

# print(chatbot.get_response("what is computer?"))

# name = input("Enter your name: ")
# print("Hi", name, "! I'm Mika, your Machine Intelligent Knowledge AI.")
#
# while True:
#     query = input(name+": ")
#     print("Mika:", chatbot.get_response(query))

@app.route("/")
def home():
    return render_template("index.html", botname=botname)

@app.route("/get")
def get_bot_response():

	userInput=request.args.get('msg')
	return str(chatbot.get_response(userInput))

if __name__ == '__main__':
	app.run(port=5500)