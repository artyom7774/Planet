import json


class Translate:
    def __init__(self, leng):
        self.leng = leng

    def translate(self, word):
        if self.leng == "EN":
            return word

        if word == "":
            return word

        if word == "*":
            return word

        with open(f"DATA/files/bundles/{self.leng.lower()}.json", encoding="utf-8") as file:
            var = json.load(file)
            if var.get(word) is not None:
                return var[word]

            else:
                return word
