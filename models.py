import json
from os import waitpid
#from wtforms.compat import with_metaclass

class Posts:
    def __init__(self):
        try:
            with open("posts.json", "r") as f:
                self.posts = json.load(f)
        except FileExistsError:
            self.posts = []

    def all(self):
        return self.posts
    
    def get(self, id):
        return self.posts[id-1]

    def create(self, data):
        self.posts.append(data)
        self.save_all()

    def save_all(self):
        with open('posts.json', "w") as f:
            json.dump(self.posts, f)

    def update(self, id, data):
        post = self.get(id)
        if post:
            index = self.posts.index(post) # ta linijka wyrzuca błąd 'out of range'
            self.posts[index] = data
            # self.posts[id-1] = data
            # self.save_all()
            return True
        return False
posts = Posts()