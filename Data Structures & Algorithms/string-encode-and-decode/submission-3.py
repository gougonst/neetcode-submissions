class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            encodedString += str(len(s)) + "#" + s
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        i = 0
        while i < len(s):
            size = ""
            while i < len(s) and s[i] != "#":
                size += s[i]
                i += 1
            i += 1
            size = int(size)
            decodedStrings.append(s[i:i + size])
            i += size

        return decodedStrings
