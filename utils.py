import json

DATA_PATH = "data/data.json"
COMMENTS_PATH = "data/comments.json"
BOOKMARKS_PATH = "data/bookmarks.json"


def load_json(data):
    """
    Загружает данные из файла формата JSON.
    """
    with open(data, "r", encoding="utf8") as file:
        return json.load(file)


def get_posts_all():
    """
    Загружает посты.
    """
    return load_json(DATA_PATH)


def get_posts_by_user(user_name):
    """
    Возвращает посты определенного пользователя.
    """
    load_user = load_json(DATA_PATH)
    user_post = []
    for user in load_user:
        if user_name in user["poster_name"]:
            user_post.append(user)
    return user_post


def get_comments_by_post_id(post_id):
    """
    Возвращает комментарии определенного поста.
    """
    load_comment = load_json(COMMENTS_PATH)
    comment_posts = []
    for comment in load_comment:
        if post_id == comment["post_id"]:
            comment_posts.append(comment)
    return comment_posts


def search_for_posts(query):
    """
    Возвращает список постов по ключевому слову.
    """
    load_posts = load_json(DATA_PATH)
    res = []
    for post in load_posts:
        if query is None:
            return res
        if query.lower() in post["content"].lower():
            res.append(post)
    return res


def get_post_by_pk(pk):
    """
    Возвращает один пост по его идентификатору.
    """
    load_post = load_json(DATA_PATH)
    for post in load_post:
        if pk == post["pk"]:
            return post
    return {}


def add_bookmarks(post_id):
    """
    Добавляет закладку в избранное.
    """
    load_post = load_json(DATA_PATH)
    load_bookmarks = load_json(BOOKMARKS_PATH)

    with open(BOOKMARKS_PATH, "w", encoding="utf8") as file:
        for post in load_post:
            if post_id == post["pk"]:
                load_bookmarks.append(post)
                json.dump(load_bookmarks, file, ensure_ascii=True)


def remove_bookmarks(post_id):
    """
    Удаляет закладку из избранного.
    """
    load_bookmarks = load_json(BOOKMARKS_PATH)
    with open(BOOKMARKS_PATH, "w") as file:
        for bookmark in range(len(load_bookmarks)):
            if post_id == load_bookmarks[bookmark]["pk"]:
                load_bookmarks.pop(bookmark)
                json.dump(load_bookmarks, file, ensure_ascii=True)
