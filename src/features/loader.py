
import pandas as pd
from os import path


class KnowledgeBaseLoader(object):

    def __read_file(self, file, columns):
        return pd.read_csv(file, sep='\t', header=None, skiprows=[0], names=columns)

    def load_entities(self, directory):
        return self.__read_file(path.join(directory, 'entity2id.txt'), ['entity', 'id'])

    def load_relations(self, directory):
        return self.__read_file(path.join(directory, 'relation2id.txt'), ['relation', 'id'])

    def load_facts(self, directory):
        return self.__read_file(path.join(directory, 'train2id.txt'), ['head', 'tail', 'relation'])
