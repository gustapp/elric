class KnowledgeBaseDictionarizer(object):

    def __create_dict(self, df, key):
        return df.set_index(key).T.to_dict()

    def entity2id(self, df):
        return self.__create_dict(df, 'entity')

    def id2entity(self, df):
        return self.__create_dict(df, 'id')

    def relation2id(self, df):
        return self.__create_dict(df, 'relation')
