import unittest
import requests
import mock
from wtsize import wtsize

class WTSizeTestCase(unittest.TestCase):
    '''WTSize unit test case'''

    def setUp(self):
        pass

    def test_output_format_auto_unit(self):
        '''Test that output format is valid.'''
        self.assertEqual(wtsize.format_(0), '0.0 B')
        self.assertEqual(wtsize.format_(20), '20.0 B')
        self.assertEqual(wtsize.format_(1024), '1.0 KiB')
        self.assertEqual(wtsize.format_(862182613), '822.24 MiB')
        self.assertEqual(wtsize.format_(9799471047), '9.13 GiB')
        self.assertEqual(wtsize.format_(8527105793758), '7.76 TiB')
        self.assertEqual(wtsize.format_(8461047105717938), '7.51 PiB')
        self.assertEqual(wtsize.format_(10000000000000000000), '')

    def test_output_format_manual_unit(self):
        '''Test that output format can be chosen by passing unit.'''
        self.assertEqual(wtsize.format_(0, 'KiB'), '0.0 KiB')
        self.assertEqual(wtsize.format_(20, 'KiB'), '0.02 KiB')
        self.assertEqual(wtsize.format_(9799471047, 'MiB'), '9345.5 MiB')
        self.assertEqual(wtsize.format_(8527105793758, 'GiB'), '7941.49 GiB')
        self.assertEqual(wtsize.format_(8461047105717938, 'TiB'), '7695.28 TiB')
        self.assertEqual(wtsize.format_(8461047105717938, 'B'), '8461047105717938.0 B')

    @mock.patch.object(requests, 'head')
    def test_header_missing(self, mock_request):
        '''Test handling of missing Content-Length header'''
        mock_response = mock.Mock()
        mock_response.headers = {} # empty headers so Content-Length is not found
        mock_request.return_value = mock_response

        self.assertEqual(
            wtsize.wtsize({'URL': 'https://127.0.0.1/some_test_file.zip', '--unit': None}),
            'Unable to get file size (no Content-Length header).'
        )
