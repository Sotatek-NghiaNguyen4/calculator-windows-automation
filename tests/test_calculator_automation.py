import unittest
from app.calculator_automation import Calculator
from parameterized import parameterized

test_data_programmer_mode = [(7), (11), (100), (1000)]
test_data_standard_mode = [
    (1, "+", 2),
    (3, "-", 1),
    (10, "*", 3),
]


class CalculatorAutomationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calculator = Calculator()

    @classmethod
    def tearDownClass(cls):
        cls.calculator.close_calculator()

    @parameterized.expand(test_data_standard_mode)
    def test_standard_mode(self, a, operator, b):
        self.calculator.select_mode("Standard")
        result = self.calculator.perform_calculation(a, operator, b)
        expected_result = str(eval(f"{a} {operator} {b}"))
        self.assertEqual(
            expected_result,
            result,
            f"Standard mode calculation failed for {a} {operator} {b}",
        )

    @parameterized.expand(test_data_programmer_mode)
    def test_programmer_mode(self, num):
        self.calculator.click_to_navigate()
        self.calculator.click_to_mode("Programmer Calculator")
        self.calculator.enter_number(num)

        self.validate_programmer_results(num)

        self.calculator.click_to_display_values("HEX")
        hex_result = self.calculator.get_display_value("HEX")
        self.assertEqual(
            hex(num).upper()[2:], hex_result, "HEX display value is incorrect"
        )

        self.calculator.click_to_display_values("DEC")
        dec_result = self.calculator.get_display_value("DEC")
        self.assertEqual(
            str(num), dec_result.replace(",", ""), "DEC display value is incorrect"
        )

        self.calculator.click_to_display_values("OCT")
        oct_result = self.calculator.get_display_value("OCT")
        expected_oct = self.calculator.add_space(oct(num)[2:])
        self.assertEqual(expected_oct, oct_result, "OCT display value is incorrect")

        self.calculator.click_to_display_values("BIN")
        bin_result = self.calculator.get_display_value("BIN")
        expected_bin = self.calculator.binary_format(num)
        self.assertEqual(
            expected_bin, bin_result.replace(" ", ""), "BIN display value is incorrect"
        )
