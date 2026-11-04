class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            for c in s:
                encodedString += str(ord(c)) + " "
            encodedString += " | "
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        decodedString = ""
        i = 0
        while i < len(s):
            if s[i] == "|":
                decodedStrings.append(decodedString)
                decodedString = ""
            elif s[i] != " ":
                ordNumber = ""
                while i < len(s) and s[i].isdigit():
                    ordNumber += s[i]
                    i += 1
                decodedString += chr(int(ordNumber))
            i += 1
        return decodedStrings
