from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from flask_restful import Resource, Api
import api_post

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='fawkes', password='1234'))
users.append(User(id=2, username='mm', password='4321'))



app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user


  
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('home'))

        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)

    return redirect(url_for('login'))

@app.route('/')
@app.route('/home')
def home():
    if not g.user:
        return redirect(url_for('login'))
    
    return render_template("index.html")



@app.route('/result',methods=['POST', 'GET'])
def result():
    if not g.user:
        return redirect(url_for('login'))
    
    output = request.form.to_dict()
    pin = output['pin']
    pin = pin.upper()
    
    total_data = api_post.total_return()
    total_data1 = api_post.total_return()
    total_data2 = api_post.list_converter(total_data1)

    for i in total_data:
        if i["subjects"] == "TOTAL":
            total_periods = i["values"]
            

    
    data = api_post.pin_checker(pin)
    data = data[0]
    data1 = api_post.pin_checker(pin)
    data1 = data1[0]
    data1.pop("key")
    data1.pop("Name")
    data1.pop("Percent")
    data1.pop("Pin")
    data1.pop("Status")
    data1.pop("TOTAL")
    data1.pop("data")
    

    total_data_3 = api_post.total_adder(total_data2,list(data1.items()))


    
    heads = ("subject","Attended","Total")

    return render_template('result.html',sign_up="sign-up-mode", name=data["Name"],pin=data["Pin"],headings=heads,data=total_data_3,percent=data["Percent"],present=data["TOTAL"],total_present=total_periods)


if __name__ == "__main__":
    app.run(threaded=True, port=5000)