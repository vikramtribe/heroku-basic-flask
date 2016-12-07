from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():

    return render_template('index.html')

@app.route('/', methods=['POST'])
def form_go():

	topic = request.form['topic']
	genre = request.form['genre']
	print(genre)
	#country = request.form['country']
	#print(country)
	#length = request.form['length']
	#print(length)

	#return "<html><p>" + topic + "</p></html>"
	return topic

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

