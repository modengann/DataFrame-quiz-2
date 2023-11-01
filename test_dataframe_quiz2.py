import pandas as pd
import unittest
import dataframe_quiz2 as quiz_script  # Replace 'your_script_name' with the name of your script

class TestQuizMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pd.DataFrame({
            'Age': [34, 29, 40, 28, 38],
            'Salary': [75000, 62000, 90000, 58000, 84000],
            'Role': ['Manager', 'Designer', 'Engineer', 'Marketer', 'Data Scientist'],
            'Country': ['USA', 'Canada', 'UK', 'Australia', 'USA']
        }, index = ['Frank', 'Megan', 'Phil', 'Sophie', 'Oscar'])

    def test_get_role(self):
        expected_output = pd.Series(['Manager', 'Designer', 'Engineer', 'Marketer', 'Data Scientist'], name="Role", index = ["Frank","Megan", "Phil", "Sophie", "Oscar"])

        result = quiz_script.get_role(self.df)
        pd.testing.assert_series_equal(result, expected_output)

    def test_get_fifth_entry(self):
        expected_output = pd.Series([38, 84000, 'Data Scientist', 'USA'], index=self.df.columns, name="Oscar")
        result = quiz_script.get_fifth_entry(self.df)
        pd.testing.assert_series_equal(result, expected_output)

    def test_get_phil_info(self):
        expected_data = {'Age': 40, 'Salary': 90000, 'Role': 'Engineer', 'Country': 'UK'}
        expected_output = pd.Series(expected_data, name = "Phil")
        result = quiz_script.get_phil_info(self.df)
        pd.testing.assert_series_equal(result, expected_output)

    def test_get_age_country(self):
        expected_data = {'Age': [34, 29, 40, 28, 38], 'Country': ['USA', 'Canada', 'UK', 'Australia', 'USA']}
        expected_output = pd.DataFrame(expected_data, index = ["Frank","Megan", "Phil", "Sophie", "Oscar"])
        result = quiz_script.get_age_country(self.df)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_get_role_megan_oscar(self):
        expected_output = pd.Series(['Designer', 'Data Scientist'], name="Role", index=["Megan","Oscar"])
        result = quiz_script.get_role_megan_oscar(self.df)
        pd.testing.assert_series_equal(result, expected_output)
    
    def test_get_age_salary_of_middle_three(self):
        expected_data = {'Age': [29, 40, 28], 'Salary': [62000, 90000, 58000]}
        expected_output = pd.DataFrame(expected_data, index=["Megan", "Phil", "Sophie"])
        result = quiz_script.get_age_salary_of_middle_three(self.df)
        pd.testing.assert_frame_equal(result, expected_output)

if __name__ == "__main__":
    unittest.main()
