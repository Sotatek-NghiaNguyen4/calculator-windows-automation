import time
import pyautogui
import uiautomation as automation


class Calculator:
    def __init__(self):
        automation.uiautomation.SetGlobalSearchTimeout(15)
        pyautogui.press("win")
        pyautogui.write("Calculator")
        pyautogui.press("enter")
        self.calculator_window = automation.WindowControl(
            searchDepth=2, Name="Calculator"
        )
        time.sleep(1)

    def close_calculator(self):
        pyautogui.hotkey("alt", "f4")

    def perform_calculation(self, operand1, operator, operand2):
        self._enter_number(operand1)
        self._enter_operator(operator)
        self._enter_number(operand2)
        self._get_result()

    def click_to_navigate(self):
        self._click_button("Open Navigation")

    def click_to_mode(self, mode):
        self._click_list_item(mode)

    def click_to_display_values(self, display_values):
        self._click_text(display_values)

    def get_calculator_result(self):
        result_control = self.calculator_window.PaneControl(
            automationId="TextContainer"
        )
        return result_control.Name

    def _enter_number(self, number):
        for char in str(number):
            pyautogui.press(char)

    def _enter_operator(self, operator):
        pyautogui.press(operator)

    def _get_result(self):
        pyautogui.press("=")

    def _click_button(self, name):
        self.calculator_window.ButtonControl(Name=name).Click()

    def _click_list_item(self, name):
        self.calculator_window.ListItemControl(Name=name).Click()

    def _click_text(self, name):
        self.calculator_window.TextControl(Name=name).Click()

    @staticmethod
    def format_binary(num):
        binary_string = bin(num)[2:]
        return f"{int(binary_string):04b}"

    @staticmethod
    def add_spaces_to_binary(binary_str):
        return " ".join(binary_str[i : i + 4] for i in range(0, len(binary_str), 4))
