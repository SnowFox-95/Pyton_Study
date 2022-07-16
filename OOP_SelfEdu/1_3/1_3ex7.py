class Notes:
    uid: int = 1005435
    title: str = "Шутка"
    author: str = "И.С. Бах"
    pages: int = 2


output = getattr(Notes, 'author')

print(output)
