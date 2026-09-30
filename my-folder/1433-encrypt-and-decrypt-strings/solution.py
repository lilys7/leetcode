class Encrypter:

    def __init__(self, keys: list[str], values: list[str], dictionary: list[str]):
        self.mapping = {k:v for k,v in zip(keys, values)}
        #pre encrypt the dictionary
        self.encrypted_dict = defaultdict(int)
        for elt in dictionary:
            res = self.encrypt(elt)
            if res != "":
                #if the encryption is successful, add one to the value @ key
                self.encrypted_dict[res] += 1
   

    def encrypt(self, word1: str) -> str:
        res = ""
        for ch in word1:
            if ch in self.mapping:
                res+= self.mapping[ch]
            else:
                return ""
        return res

    def decrypt(self, word2: str) -> int:
        return self.encrypted_dict[word2] if word2 in self.encrypted_dict else 0


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
