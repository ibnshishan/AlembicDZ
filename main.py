# from database import SessionLocal, session
# import crud
#
# # Добавляем пользователей
# user1 = crud.add_user( "Алиса", "alice@example.com")
# user2 = crud.add_user( "Боб", "bob@example.com")
# user3 = crud.add_user( "Клара", "clara@example.com")
#
# # Добавляем посты
# crud.add_post( "Привет", "Это мой первый пост!", user1.id)
# crud.add_post( "Второй пост", "Контент здесь", user1.id)
# crud.add_post( "Пост Боба", "Проверка связи", user2.id)
# crud.add_post( "Пост Клары", "Содержимое...", user3.id)
# crud.add_post( "Ещё один", "Текст поста", user1.id)
#
# # Получаем всех пользователей
# print(crud.get_user())
#
# # Обновляем email
# crud.update_user_email( user2.id, "newbob@example.com")
#
# # Удаляем пост
# crud.delete_post(1)
#
# session.close()
import crud

crud.add_user('MOvsar', 'blackstar013.bs@gmail.com')
