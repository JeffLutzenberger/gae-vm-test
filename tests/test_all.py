import urllib
import urllib2
import test_config
import unittest
import main


class TestGAEPlayground(unittest.TestCase):

    def setUp(self):
        self.my_model = main.MySimpleModel(title="my simple model",
                                           sub_title="my simple subtitle",
                                           subject="my simple subject",
                                           body=str('x' * int(1e4)))
        self.num_transaction_records = 10


    def test_backend(self):
        response = urllib2.urlopen(test_config.base_url + '/backend-test')
        self.assertIsNotNone(response)
        code = response.getcode()
        self.assertEqual(code, 200)
        response.close()


if __name__ == '__main__':
    unittest.main()
