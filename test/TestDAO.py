import unittest
import mongomock
from core.domain import Data
import persistence.DAO as DAO


class TestUrlDao(unittest.TestCase):

    def setUp(self):
        self.client = mongomock.MongoClient()

    def test_mongoclient(self):
        self.assertIsNotNone(self.client)

    def test_insert_and_find(self):
        data_dao = DAO.DataDao(self.client, 'data')
        insert_id = self.insert_data(data_dao)
        result = data_dao.find_one_by_id(insert_id)

        self.assertIsNotNone(result.get('root'))
        self.assertEqual('root-value', result.get('root'))

    def test_delete(self):
        data_dao = DAO.DataDao(self.client, 'data')
        insert_id = self.insert_data(data_dao)
        result = data_dao.find_one_by_id(insert_id)

        self.assertIsNotNone(result.get('root'))
        self.assertEqual('root-value', result.get('root'))

        data_dao.delete_by_id(insert_id)

        self.assertIsNone(data_dao.find_one_by_id(insert_id))

    #   TODO
    # def test_update(self):
    #     data_dao = Dao.DataDao(self.client, 'data')
    #     insert_id = self.insert_data(data_dao)
    #     result = data_dao.find_one_by_id(insert_id)
    #
    #     self.assertIsNotNone(result.get('root'))
    #     self.assertEqual('root-value', result.get('root'))

    @staticmethod
    def insert_data(data_dao):
        data = Data.Data('root-value', 'type-value', 'data-value')
        insert_id = data_dao.insert_one(data.to_db_collection())
        return insert_id.inserted_id
