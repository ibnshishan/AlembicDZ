from models import User, Post
from database import session


# def add_student(name: str, age: int):
#     student = Student(name=name, age=age)
#     session.add(student)
#     session.commit()
#     session.close()
#     print('Student ')

def add_user(name: str, email: str):
    user = User(name=name, email=email)
    session.add(user)
    session.commit()


def add_post(title: str, content: str, user_id: int):
    post = Post(title=title, content=content, user_id=user_id)
    session.add(post)
    session.commit()
    return post


def get_user():
    users = session.query(User).all()

    for user in users:
        print(user.name, user.email)


def get_post():
    posts = session.query(Post).all()

    for post in posts:
        print(post.title, post.content, post.user_id)


def update_user_email(user_id, new_email):
    user = session.query(User).filter_by(User.id == user_id).first()
    if user:
        user.email = new_email
        session.commit()


def delete_user(user_id: int):
    user = session.query(User).filter(id == user_id).first()
    if user:
        session.delete(user)
        session.commit()


def delete_post(post_id: int):
    post = session.query(Post).filter(id == post_id).first()
    if post:
        session.delete(post)
        session.commit()
