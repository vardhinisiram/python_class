from flask import Flask, render_template, request, send_file

from random_dog import ret_dog_image

app = Flask(__name__)

@app.route("/")
def hello_world():
	return render_template("form.html")

@app.route("/validate", methods = ["GET", "POST"]) 
def check():
	# uname = request.args.get("uname")
	# passwd = request.args.get("pass")
	uname = request.form.get("uname")
	passwd = request.form.get("pass")

	# print(request.args.get("uname"), request.	args.get("pass"))
	print(request.base_url, request.data, request.form)
	print(request.headers)
	# print(request.form["uname"], request.form["pass"])
	if uname == "apple" and passwd == "apple":
		return render_template("calc.html")
	else:
		return "<h1> Wrong user </h1>"

@app.route("/dog_download")
def dog_download():
	result_file = ret_dog_image()
	return send_file(result_file, as_attachment=True)

if __name__ == '__main__':
	app.run(host='0.0.0.0' , port=5000)