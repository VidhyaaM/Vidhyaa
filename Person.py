class Person:
    name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'There is no such user'
        else:
            return self.name[user_id]


if __name__ == '__main__':
    person = Person()
    print('User Vithu added with id ', person.set_name('Vithu'))
    print('User Vidhyaa added with id ', person.set_name('Vidhyaa'))
    print('User associated with id  is ', person.get_name(1))
