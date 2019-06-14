from src.core.test import BaseTest


class TestModule1Resources(BaseTest):
    def test_testresourceview(self):
        message = {'message': 'here on get'}
        
        result = self.simulate_get('/api/v1/test', headers=self.headers)

        self.assertEqual(result.json, message)