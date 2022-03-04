# https://realpython.com/python-interface/
# https://www.geeksforgeeks.org/python-interface-module/


class ParserInterface:

    def load_data_source(self):
        pass

    def extract_text(self):
        pass


class PdfParser(ParserInterface):
    def load_data_source(self):
        print("Loading : In PDF ")

    def extract_text(self):
        print("Extracting: In PDF")


class CSVParser(ParserInterface):
    def load_data_source(self):
        print("Loading : In CSV ")
    def extract_text(self):
        print("Extracting: In CSV")

pdf = PdfParser()
pdf.load_data_source()
pdf.extract_text()
csv = CSVParser()
csv.load_data_source()
csv.extract_text()