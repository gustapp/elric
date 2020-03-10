
import pandas as pd
from os import path


class KnowledgeBaseLoader(object):

    @staticmethod
    def read_file(file, columns):
        return pd.read_csv(file, sep='\t', header=None, skiprows=[0], names=columns)

    @classmethod
    def load_entities(loader, directory):
        return loader.read_file(path.join(directory, 'entity2id.txt'), ['entity', 'id'])

    @classmethod
    def load_relations(loader, directory):
        return loader.read_file(path.join(directory, 'relation2id.txt'), ['relation', 'id'])

    @classmethod
    def load_facts(loader, directory):
        return loader.read_file(path.join(directory, 'train2id.txt'), ['head', 'tail', 'relation'])
