from utilities.excel import validate_excel, clear_dataframe

class ExcelHandler:
    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name

    def validate(self) -> bool:
        return validate_excel(self.file_path, self.file_name)

    def clear(self):
        clear_dataframe()
