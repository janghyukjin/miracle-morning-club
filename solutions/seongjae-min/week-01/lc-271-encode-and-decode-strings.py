class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(s)
            result.append("구분")

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        return s.split("구분")[:-1]

