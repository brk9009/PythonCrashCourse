import unittest
import python_repos as pr 

class PythonReposTestCase(unittest.TestCase):

    def setUp(self):
        """ Call all functions here."""
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.names, self.plot_dicts = pr.get_names_plot_dicts(self.repo_dicts)

    def test_status_code(self):
        """ Test that we get a valid response."""
        self.assertEqual(self.r.status_code, 200)

unittest.main()

