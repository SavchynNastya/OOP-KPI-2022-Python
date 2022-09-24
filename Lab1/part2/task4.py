class FileProcessing:
    def __init__(self, file):
        self._name = file.name
        self._text = file.readlines()
        self._lines = len(self._text)
        self._characters = 0
        self._words = 1
        self._sentences = 0

    def count_characters(self):
        for i in range(self._lines):
            for ch in self._text[i]:
                self._characters += 1
        return self._characters

    def count_words(self):
        for i in range(self._lines):
            for ch in self._text[i]:
                if ch.isspace():
                    self._words += 1
        return self._words

    def count_sentences(self):
        for i in range(self._lines):
            for ch in self._text[i]:
                if ch == ".":
                    self._sentences += 1
        return self._sentences

    def get_info(self):
        file.close()
        if not self._text:
            print("File is empty!")
        else:
            print(f"Characters in '{self._name}' - {self.count_characters()}\n"
                  f"Words in '{self._name}' - {self.count_words()}\n"
                  f"Sentences in '{self._name}' - {self.count_sentences()}\n")


def main():
    try:
        f = input("Enter the name of file(with path and extension): ")  # for_task4.txt
        file = open(rf"{f}", "r")
        file_processing = FileProcessing(file)
        file_processing.get_info()
    except IOError:
        print("There's no such file")


if __name__ == "__main__":
    main()
