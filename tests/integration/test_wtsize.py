import unittest
import requests
from wtsize import wtsize

class WTSizeIntegrationTestCase(unittest.TestCase):
    '''WTSize integration test case'''
    def setUp(self):
        pass

    def test_accurate_size_retrieval(self):
        '''Fetch headers of a known test file and assert size.'''
        sample_url = 'https://davidhamann.de/assets/images/log_plot.png'
        sample_options = {'URL': sample_url, '--unit': None}
        self.assertEqual(wtsize.wtsize(sample_options), '24.46 KiB')

    def test_accurate_size_retrieval_custom_unit(self):
        '''Fetch headers of a known test file and assert size with custom unit.'''
        sample_url = 'https://davidhamann.de/assets/images/log_plot.png'
        sample_options = {'URL': sample_url, '--unit': 'B'}
        self.assertEqual(wtsize.wtsize(sample_options), '25046.0 B')

    def test_connection_error(self):
        '''Test handling of connection errors.'''
        sample_url = 'https://not.a.valid.url.tld/some_file.zip'
        sample_options = {'URL': sample_url, '--unit': None}
        self.assertEqual(
            wtsize.wtsize(sample_options),
            'Bad url, network connection funky or SSL verification error.'
        )
