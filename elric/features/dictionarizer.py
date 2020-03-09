def __create_dict(self, df, key):
    return df.set_index(key).T.to_dict()


class KnowledgeBaseDictionarizer(object):

    def entity2id(df):
        return __create_dict(df, 'entity')

    def id2entity(df):
        return __create_dict(df, 'id')

    def relation2id(df):
        return __create_dict(df, 'relation')
