from flask import Flask, render_template, request
import networkx as nx 


app = Flask(__name__)


"""
Node = 'Hi! About which field do you wanr to know ?'
neighbour = G.successors(Node) 
options = []
for itr in neighbour :
    options.append(itr)
"""
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<usid>/get")
def get_bot_response(usid):
	try : 
		userText = request.args.get('msg')\
		G = nx.read_adjlist((str(usid)+".tsv"), delimiter= '\t', create_using=nx.DiGraph())
		Next_questions = G.successors(userText)
		for itr in Next_questions :
			Node = itr
		output = str(Node) 
		output += "<br>"
		Neighbour = G.neighbors(Node) 
		options = []
		for itr in Neighbour :
			output += str(itr) + "<br>" 
			options.append(itr)
		print(output)
		return str(output)
	except :
		return str("Please enter a valid option")

if __name__ == "__main__":
    app.run()
