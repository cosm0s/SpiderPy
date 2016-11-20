import unittest
import utils.ReadProperties as ReadProperties

class TestReadProperties(unittest.TestCase):

    def setUp(self):
        config = ReadProperties.ConfigParser()
        self.prop = config.read_config('..')

    def test_read_properties(self):
        self.assertTrue(len(self.prop) > 0)

    def test_thread_max(self):
        self.assertIsNotNone(self.prop.get('thread', 'max'))

if __name__ == '__main__':
    unittest.main()