import re


class FileProcessing:
    def __init__(self, file_name):
        self.name = file_name

    def count_characters(self):
        count = 0
        file = open(self.name, 'r')
        for line in file:
            count += len(line) - line.count(' ') - line.count('\n')
        file.close()
        return count

    def count_words(self):
        count = 0
        file = open(self.name, 'r')
        for line in file:
            count += len(re.findall(r"[A-Za-z']+", line))
        file.close()
        return count

    def count_sentences(self):
        count = 0
        file = open(self.name, 'r')
        for line in file:
            count += len(re.findall(r"\w+[.?!]+", line))
        file.close()
        return count

    def get_info(self):
        return f"Characters in '{self.name}' - {self.count_characters()}\n"\
               f"Words in '{self.name}' - {self.count_words()}\n"\
               f"Sentences in '{self.name}' - {self.count_sentences()}\n"


def main():
    file_name = "for_task4.txt"
    try:
        file_processing = FileProcessing(file_name)
        print(file_processing.get_info())
    except FileNotFoundError:
        print("There's no such file")


if __name__ == "__main__":
    main()
