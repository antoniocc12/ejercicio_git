app = Flask(__name__)
@app.route("/")
def landing_page():
return render_template('index.html')
if __name__ == '__main__':app.run(host='0.0.0.0',port=1991, debug=True)
