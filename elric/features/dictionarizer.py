class KnowledgeBaseDictionarizer(object):

    @staticmethod
    def create_dict(df, key):
        return df.set_index(key).T.to_dict()

    @classmethod
    def entity2id(dictionarizer, df):
        return dictionarizer.create_dict(df, 'entity')

    @classmethod
    def id2entity(dictionarizer, df):
        return dictionarizer.create_dict(df, 'id')

    @classmethod
    def relation2id(dictionarizer, df):
        return dictionarizer.create_dict(df, 'relation')
