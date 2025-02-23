import unittest
from api import app
from main import format_postcode, postcode_verify, outward_code_verify, inward_code_verify


class TestPostcodeFunctions(unittest.TestCase):

    def test_format_postcode_valid(self):
        self.assertEqual(format_postcode("   L-L-0-6X H   "), "LL0 6XH")
        self.assertEqual(format_postcode("CM10 1PT"), "CM10 1PT")
        self.assertEqual(format_postcode("M1 1AE"), "M1 1AE")

    def test_format_postcode_invalid_length(self):
        self.assertEqual(format_postcode("a"), "A")
        self.assertEqual(format_postcode("aa"), "AA")
        self.assertEqual(format_postcode("aaa"), "AAA")

    def test_postcode_verify_valid(self):
        self.assertEqual(postcode_verify("   C-M-0-6X H   "), "Postcode is valid: CM0 6XH")
        self.assertEqual(postcode_verify("BS 10 1-PT"), "Postcode is valid: BS10 1PT")

    def test_postcode_verify_invalid_length(self):
        with self.assertRaises(ValueError):
            postcode_verify("A")
            postcode_verify("AA")
            postcode_verify("AA9A 9AAA")

    def test_outward_code_verify_valid(self):
        try:
            outward_code_verify("AA9")
        except ValueError:
            self.fail("outward_code_verify raised ValueError unexpectedly!")

        try:
            outward_code_verify("AA99")
        except ValueError:
            self.fail("outward_code_verify raised ValueError unexpectedly!")

    def test_outward_code_verify_invalid(self):
        with self.assertRaises(ValueError):
            outward_code_verify("ZZ9")

        with self.assertRaises(ValueError):
            outward_code_verify("AA0")

    def test_inward_code_verify_valid(self):
        try:
            inward_code_verify("9AA")
        except ValueError:
            self.fail("inward_code_verify raised ValueError unexpectedly!")

    def test_inward_code_verify_invalid(self):
        with self.assertRaises(ValueError):
            inward_code_verify("AAA")

        with self.assertRaises(ValueError):
            inward_code_verify("999")


class TestPostcodeAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_format_postcode_api_valid(self):
        response = self.app.get('/format/L-L-0-6X%20H')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'formatted_postcode': 'LL0 6XH', 'status': 'success'})

    def test_format_postcode_api_invalid(self):
        response = self.app.get('/format/a')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['formatted_postcode'], 'A')

    def test_postcode_verify_api_valid(self):
        response = self.app.get('/verify/BS10 1PT')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Postcode is valid', 'status': 'success'})

    def test_postcode_verify_api_invalid(self):
        response = self.app.get('/verify/A')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Postcode length must be between 6 and 8 characters', response.json['message'])

        response = self.app.get('/verify/AA9 9AAA')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Not valid. The inward_code \'AAA\' does not matches pattern', response.json['message'])


if __name__ == '__main__':
    unittest.main()
