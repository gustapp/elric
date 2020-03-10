
import pandas as pd
from os import path


def read_file(file, columns):
    return pd.read_csv(file, sep='\t', header=None, skiprows=[0], names=columns)


class KnowledgeBaseLoader(object):

    def load_entities(directory):
        return read_file(path.join(directory, 'entity2id.txt'), ['entity', 'id'])

    def load_relations(directory):
        return read_file(path.join(directory, 'relation2id.txt'), ['relation', 'id'])

    def load_facts(directory):
        return read_file(path.join(directory, 'train2id.txt'), ['head', 'tail', 'relation'])
