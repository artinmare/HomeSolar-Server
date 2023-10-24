def side_effect_test():
    def side_function(new_data: dict):
        new_data["side_effect"] = "Working Side Effect"

    data = {
        "Default": 123
    }

    side_function(data)

    print(data)


class TestClass:
    def __init__(self):
        self._calculated_data = None

    @property
    def calculated_data(self):
        return self._calculated_data

    @calculated_data.setter
    def calculated_data(self, func):
        self._calculated_data = func

    def run(self):
        data = "Test Data"

        if self.calculated_data is not None:
            self.calculated_data(data)


def assign_function_to_class():
    test = TestClass()
    test.run()

    def calculated_data(data):
        print(data)

    test.calculated_data = calculated_data
    test.run()


if __name__ == "__main__":
    side_effect_test()
    assign_function_to_class()
