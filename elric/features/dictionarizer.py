class KnowledgeBaseDictionarizer(object):

    def __create_dict(df, key):
        return df.set_index(key).T.to_dict()

    def entity2id(df):
        return KnowledgeBaseDictionarizer.__create_dict(df, 'entity')

    def id2entity(df):
        return KnowledgeBaseDictionarizer.__create_dict(df, 'id')

    def relation2id(df):
        return KnowledgeBaseDictionarizer.__create_dict(df, 'relation')
