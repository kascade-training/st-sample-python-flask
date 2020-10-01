#!/usr/bin/env python
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'{"hello": "STMicroelectronics"}\n')

    def test_hello_hello(self):
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'{"hello": "STMicroelectronics"}\n')

    def test_hello_name(self):
        name = 'Ahmed'
        rv = self.app.get('/hello/{name}')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn("{name}", rv.data)

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
