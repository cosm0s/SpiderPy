import unittest
import os
import utils.ReadProperties as ReadProperties


class TestReadProperties(unittest.TestCase):

    def setUp(self):
        self.root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                     '..')
        config = ReadProperties.ConfigParser()
        self.prop = config.read_config(self.root_dir)

    def test_read_properties(self):
        self.assertTrue(len(self.prop) > 0)

    def test_thread_max(self):
        self.assertIsNotNone(self.prop.get('thread', 'max'))

    def test_properties_file(self):
        self.assertTrue(os.path.isfile(os.path.join(self.root_dir, 'conf', 'spiderpy.properties')))

if __name__ == '__main__':
    unittest.main()
