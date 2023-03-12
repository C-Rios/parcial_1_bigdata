from apps import downloadHTML

from unittest.mock import patch, Mock
from unittest import TestCase


class Test_downloadHTML(TestCase):
    @patch('apps.urllib.request.urlopen')
    def test_download_html(self,
                           mock_urlopen):
        url = ('https://casas.mitula.com.co/'
               'searchRE/tipo-Casa/q-Chapinero--Bogota')

        expected_string = ("<!DOCTYPE html><html><head>"
                           "<title>Test Page</title></head>"
                           "<body><h1>Hello World!</h1></body>"
                           "</html>")

        mock_response = Mock()
        mock_response.read.return_value = expected_string.encode('UTF-8')
        mock_urlopen.return_value = mock_response

        result = downloadHTML(url)

        mock_urlopen.assert_called_once_with(url)

        self.assertIn("<!DOCTYPE html>", result)
        self.assertIn("</html>", result)
