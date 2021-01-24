from flask import Flask, render_template, request

app = Flask(__name__)
 
@app.route("/")
@app.route("/index")

def hello():
    work_exp = [ { 'position': "nu am lucrat", 'company': "la tata la magazin", 'period': "16 ani" } ]
    education = [{'unde': 'lcb', 'perioada': "12 ani"}, {'unde': 'acs', 'perioada': "1 semestru"}]
    return render_template('index.html', title='CV Surcel Ioan-Eduard', work=work_exp, edu=education)


@app.route("/contact", methods = ['POST', 'GET'])

def contact():
        if request.method == "POST":
            req = request.form
            nume = req.get("nume")
            mail = req.get("email")
            text = req.get("text")
            print(nume)
            print(mail)
            print(text)
            f = open('contact-mail.txt', 'a')
            f.write(nume)
            f.write('\n')
            f.write(mail)
            f.write('\n')
            f.write(text)
            f.write('\n')
        return render_template('contact.html')
 
if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)