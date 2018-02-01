import json

def save(data, path):
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
        f.write(s)


def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        return json.loads(s)


class Model(object):
    @classmethod
    def db_path(cls):
        classname = cls.__name__
        path = '{data}.txt'.format(classname)
        return path

    @classmethod
    def all(cls):
        path = cls.db_path()
        models = load(path)
        ms = [cls.new(m) for m in models]
        return ms

    @classmethod
    def new(cls, form):
        m = cls(form)
        return m

    @classmethod
    def find_by(cls, **kwargs):
        k, v = '', ''
        for key, value in kwargs.items():
            k, v = key, value
        all = cls.all()
        for m in all:
            if v == m.__dict__[k]:
                return m
        return None

    @classmethod
    def find_all(cls, **kwargs):
        k, v = '', ''
        for key, value in kwargs.items():
            k, v = key, value
        all = cls.all()
        ms = []
        for m in all:
            if v == m.__dict__[k]:
                ms.append(m)
        return ms

    def __repr__(self):
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '< {}\n{} >\n'.format(classname, s)

    def save(self):
        models = self.all()
        first_index = 0
        if self.__dict__.get('id') is None:
            if len(models) > 1:
                self.id = models[-1].id + 1
            else:
                self.id = first_index
            models.append(self)
        else:
            index = -1
            # 此处使用枚举
            for i, m in enumerate(models):
                if m.id == self.id:
                    index = i
                    break

                if index > -1:
                    models[index] = self
        l = [m.__dict__ for m in models]
        path = self.db_path()
        save(l, path)

