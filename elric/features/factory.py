
from elric.data.__knowledge_base import loader, dictionarizer
from os import path


class DataSetFactory(object):
    root = "/"
    path = path.join(root, 'data')


class KnowledgeBaseFactory(DataSetFactory):

    path = path.join(DataSetFactory.path, "knowledge graphs")

    def load_graph(name):

        kg_path = path.join(KnowledgeBaseFactory.path, name)

        entities = loader.load_entities(kg_path)

        entity2id = dictionarizer.entity2id(entities)
        id2entity = dictionarizer.id2entity(entities)

        relations = loader.load_relations(kg_path)

        relation2id = dictionarizer.relation2id(relations)

        return {
          'entities': { 'entity2id': entity2id, 'id2entity': id2entity },
          'relations': { 'relation2id': relation2id },
          'facts': loader.load_facts(kg_path)
        }

