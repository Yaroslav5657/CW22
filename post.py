from app import app, db
from routes import login
from models import Post
from flask import render_template, flash, redirect, url_for
from forms import PostForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user


@app.route('/posts/')
def get_posts():
    if current_user.is_authenticated:
        posts = current_user.posts
        print(posts)
        return render_template("items.html", items=posts, tittle='Posts')
    return redirect(url_for(login.__name__))

@app.route('/posts/create', methods=('GET', 'POST'))
def create_post():
    if not current_user.is_authenticated:
        return redirect(url_for(login.__name__))
    
    form = PostForm()
    if form.validate_on_submit():
        post = Post(user_id=current_user.id, tittle=form.header.data, text=form.body.data )
        
        db.session.add(post)
        
        try:
            db.session.commit()
            flash(f"Post created {form.header.data}")
            return redirect(url_for(get_posts.__name__))
        except Exception as e:
            db.session.rollback()
            flash(f"Post wasn't created: {form.header.data}! {e}")

    return render_template("create_post.html", form=form)