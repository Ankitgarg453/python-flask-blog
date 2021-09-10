import fileinput
import json,os, math
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime

with open('config.json', 'r') as rf:
    params = json.load(rf)['params']

local_server = params['local_server']
app = Flask(__name__)
app.secret_key = 'super_secret_key'
app.config['UPLOAD_FOLDER'] = params['file_upload_path']
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_pass']
)
mail = Mail(app)

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)

class Secflaskdbtbl_contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phn_nmbr = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(12), nullable = True)
    email = db.Column(db.String(82), nullable=False)

class Firstflaskdbtbl(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    sub_title = db.Column(db.String(25), nullable=False)
    slug = db.Column(db.String(12), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(12), nullable = True)
    img_file = db.Column(db.String(15), nullable=True)

@app.route("/")
def home():
    posts = Firstflaskdbtbl.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['no_of_posts']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(params['no_of_posts']) : (page-1)*int(params['no_of_posts'])+int(params['no_of_posts']) ]

    if (page == 1):
        prev = '#'
        next = '/?page='+str(page+1)
    elif (page == last):
        prev = '/?page=' + str(page - 1)
        next = '#'
    else:
        prev = '/?page=' + str(page - 1)
        next = '/?page='+str(page+1)
    return render_template('index.html', params = params, posts = posts, prev = prev, next = next)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Secflaskdbtbl_contacts(name = name, phn_nmbr = phone, msg = message, date = datetime.now(), email = email)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from' + name,
                          sender=email,
                          recipients= [params['gmail_user']],
                          body=message + '\n' + phone
                          )
    return render_template('contact.html',params = params)

@app.route("/about")
def about():
    return render_template('about.html', params = params)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/edit/<string:sno>", methods=['GET','POST'])
def edit(sno):
    if ('user_name' in session and session['user_name'] == params['username']):
        if (request.method == 'POST'):
            box_title = request.form.get('title')
            subtitle = request.form.get('stitle')
            slug = request.form.get('slug')
            content = request.form.get('content')
            imgfile = request.form.get('img_file')
            date = datetime.now()
            if sno == '0':
                new_post = Firstflaskdbtbl(title = box_title,sub_title = subtitle,slug = slug,content = content,img_file=imgfile, date=date)
                db.session.add(new_post)
                db.session.commit()
            else:
                update_post = Firstflaskdbtbl.query.filter_by(sno = sno).first()
                update_post.title = box_title
                update_post.sub_title = subtitle
                update_post.slug = slug
                update_post.content = content
                update_post.img_file = imgfile
                update_post.date = date
                db.session.commit()
                return redirect('/edit/'+sno)
        post_date = Firstflaskdbtbl.query.filter_by(sno = sno).first()
        return render_template('edit.html', params = params, post =  post_date, sno=sno)
    return redirect('/login')

@app.route("/delete/<string:sno>", methods=['GET','POST'])
def delete(sno):
    if ('user_name' in session and session['user_name'] == params['username']):
        post = Firstflaskdbtbl.query.filter_by(sno = sno).first()
        db.session.delete(post)
        db.session.commit()
        return redirect('/dashboard')
    return redirect('/login')

@app.route("/dashboard", methods=['GET','POST'])
def dashboard():
    if ('user_name' in session and session['user_name'] == params['username']):
        postdata = Firstflaskdbtbl.query.all()
        return render_template('dashboard.html',params = params, postdata = postdata)

    if (request.method=='POST'):
        uname = request.form.get('uname')
        p_user = request.form.get('pass')
        if (uname==params['username'] and p_user==params['userpass']):
            session['user_name'] = uname
            postdata = Firstflaskdbtbl.query.all()
            return render_template('dashboard.html',params = params, postdata = postdata)
    return redirect('/login')

@app.route("/uploader", methods=['GET','POST'])
def uploader():
    if ('user_name' in session and session['user_name'] == params['username']):
        if (request.method == 'POST'):
            file = request.files['file1']
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
            return "Uploaded Successfully"
    return redirect('/login')

@app.route("/logout")
def logout():
    session.pop('user_name')
    return redirect('/login')

@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Firstflaskdbtbl.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params = params, post=post)

# if __name__== '__main__':
app.run(debug = True)
