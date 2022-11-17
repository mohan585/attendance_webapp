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
import api_post,re,api_post_cse_b,api_post_it


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


it_le = "^[2]{1}[1]{1}[Tt]{1}[9]{1}[5]{1}[Aa]{1}[1]{1}[2]{1}[0-2]{1}[0-9]{1}$"
it = "^[2]{1}[0]{1}[Tt]{1}[9]{1}[1]{1}[Aa]{1}[1]{1}[2]{1}[0-5]{1}[0-9]{1}$"
cse_le = "^[2]{1}[1]{1}[Tt]{1}[9]{1}[5]{1}[Aa]{1}[0]{1}[5]{1}[0-3]{1}[0-9]{1}$"
cse_b = "^[2]{1}[0]{1}[Tt]{1}[9]{1}[1]{1}[Aa]{1}[0]{1}[5]{1}([6-9]{1}|[Aa]{1})[0-9]{1}$"
hk = "^[2]{1}[0]{1}[Hh]{1}[Kk]{1}[1]{1}[Aa]{1}[0]{1}[5]{1}[0-5]{1}[0-9]{1}$"
regular = "^[2]{1}[0]{1}[Tt]{1}[9]{1}[1]{1}[Aa]{1}[0]{1}([5]{1}[0-5]{1}[0-9]{1}|560)$"

def isValidPin(pin,pattern):
    p = re.compile(pattern)

    if (pin == ''):
        return False
    
    m = re.match(p, pin)
    
    if m is None:
        return False
    else:
        return True



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
    
    if isValidPin(pin,regular) or isValidPin(pin,hk):
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

        time_last = api_post.time_checker()
        time_last = time_last[0]

        heads = ("Subjects","Attended","Total")
    elif isValidPin(pin,cse_b) or isValidPin(pin,cse_le):
        total_data = api_post_cse_b.total_return()
        total_data1 = api_post_cse_b.total_return()
        total_data2 = api_post_cse_b.list_converter(total_data1)

        for i in total_data:
            if i["subjects"] == "TOTAL":
                total_periods = i["values"]



        data = api_post_cse_b.pin_checker(pin)
        data = data[0]
        data1 = api_post_cse_b.pin_checker(pin)
        data1 = data1[0]
        data1.pop("key")
        data1.pop("Name")
        data1.pop("Percent")
        data1.pop("Pin")
        data1.pop("Status")
        data1.pop("TOTAL")
        data1.pop("data")


        total_data_3 = api_post_cse_b.total_adder(total_data2,list(data1.items()))

        time_last = api_post_cse_b.time_checker()
        time_last = time_last[0]

        heads = ("Subjects","Attended","Total")
    elif isValidPin(pin,it) or isValidPin(pin,it_le):
        total_data = api_post_it.total_return()
        total_data1 = api_post_it.total_return()
        total_data2 = api_post_it.list_converter(total_data1)

        for i in total_data:
            if i["subjects"] == "TOTAL":
                total_periods = i["values"]

        data = api_post_it.pin_checker(pin)
        data = data[0]
        data1 = api_post_it.pin_checker(pin)
        data1 = data1[0]
        data1.pop("key")
        data1.pop("Name")
        data1.pop("Percent")
        data1.pop("Pin")
        data1.pop("Status")
        data1.pop("TOTAL")
        data1.pop("data")

        total_data_3 = api_post_it.total_adder(total_data2,list(data1.items()))

        time_last = api_post_it.time_checker()
        time_last = time_last[0]

        heads = ("Subjects","Attended","Total")
        
    return render_template('result.html',sign_up="sign-up-mode",last_update=time_last["date_time"], name=data["Name"],pin=data["Pin"],headings=heads,data=total_data_3,percent=data["Percent"],present=data["TOTAL"],total_present=total_periods)


if __name__ == "__main__":
    app.run(threaded=True, port=5000)