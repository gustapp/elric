
from elric.data_factory import DataSetFactory
from elric.features.__knowledge_base import loader, dictionarizer
from os import path


class KnowledgeBaseFactory(DataSetFactory):

    path = path.join(DataSetFactory.path, "knowledge graphs")

    @classmethod
    def load_graph(factory, name):

        kg_path = path.join(factory.path, name)

        entities = loader.load_entities(kg_path)

        entity2id = dictionarizer.entity2id(entities)
        id2entity = dictionarizer.id2entity(entities)

        relations = loader.load_relations(kg_path)

        relation2id = dictionarizer.relation2id(relations)

        return {
          'entities': {'entity2id': entity2id, 'id2entity': id2entity},
          'relations': {'relation2id': relation2id},
          'facts': loader.load_facts(kg_path)
        }
