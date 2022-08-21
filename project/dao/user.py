from project.dao.model.user import User
from project.tools.security import generate_password_hash, compose_passwords


class UserDAO:
    def __init__(self, session):
        self.session = session

    def patch_user(self, email, req):  # обновление необязательных полей в профиле пользователя
        user = self.find_user(email)
        if 'name' in req:
            user.name = req.get('name')
        if 'surname' in req:
            user.surname = req.get('surname')
        if 'favorite_genre' in req:
            user.favorite_genre = req.get('favorite_genre')
        self.session.add(user)
        self.session.commit()

    def find_user(self, email):  # метод возвращает одного пользователя по email
        return self.session.query(User).filter(User.email == email).first()

    def put_password(self, email, req):  # обновление пароля password_1 - старый пароль, password_2 - новый пароль
        input_password = req.get('password_1')
        new_password = req.get('password_2')
        user = self.find_user(email)
        user_password = user.password
        if compose_passwords(user_password, input_password):  # проверит введённый пароль на соответствие в базе
            user.password = generate_password_hash(new_password)
            self.session.add(user)
            self.session.commit()


    def create(self, data):  # создание пользователя
        user = User(password=generate_password_hash(data.get('password')),
                    email=data.get('email'),
                    name=data.get('name', None),
                    surname=data.get('surname', None),
                    favorite_genre=data.get('favorite_genre', None))
        # user = User(**data)
        self.session.add(user)
        self.session.commit()
