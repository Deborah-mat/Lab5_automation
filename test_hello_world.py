import unittest
from hello_world import app, generate_html, greet

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        # Create test client
        self.app = app.test_client()
        self.app.testing = True

    # Test greet() output
    def test_greet_function(self):
        expected = 'Welcome to CI/CD 101 using GitHub Actions!'
        result = greet()
        self.assertEqual(result, expected)
        self.assertIsInstance(result, str)

    # Test generate_html() basic structure and message
    def test_generate_html_contains_message_and_structure(self):
        message = "Test Message"
        html = generate_html(message)

        self.assertIn(message, html)
        self.assertIn("<html>", html)
        self.assertIn("<body>", html)
        self.assertIn("<div", html)
        self.assertIn("GitHub_Actions_Featured_Image.jpg", html)

    # Test generate_html() with an empty string
    def test_generate_html_empty_message(self):
        html = generate_html("")
        self.assertIn("<br>", html)

    # Test /greeting route status and content
    def test_greeting_route(self):
        response = self.app.get('/greeting')

        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.content_type)
        self.assertIn(b'Welcome to CI/CD 101 using GitHub Actions!', response.data)
        self.assertIn(b'<html>', response.data)
        self.assertIn(b'<body>', response.data)

    # Test /greeting route contains image and formatting
    def test_greeting_route_contains_image(self):
        response = self.app.get('/greeting')
        text = response.data.decode()

        self.assertIn("GitHub_Actions_Featured_Image.jpg", text)
        self.assertIn("text-align:center", text)
        self.assertIn("font-size:80px", text)

if __name__ == '__main__':
    unittest.main()
