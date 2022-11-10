import pandas

class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        df = pandas.read_csv('/home/sutclw/PycharmProjects/DictionaryApp/data.csv')
        print(self.term)
        return tuple(df.loc[df['word'] == self.term]['definition'])

