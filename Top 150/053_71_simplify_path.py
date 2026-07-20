class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        result = []

        for i in path:
            if i == "" or i == ".":
                continue
            if i == "..":
                if result:
                    result.pop()
            else:
                result.append(i)

        return "/" + "/".join(result)