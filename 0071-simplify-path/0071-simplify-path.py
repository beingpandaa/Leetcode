class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for name in path:
            # Add the current file/directory name, if it is an actual file/directory
            if name not in ['','.','..']:
                stack.append(name)
            # Remove the previously stored name (Going up one level)
            elif name=='..' and stack:
                stack.pop()
        # Add '/' in front since path always start with a single slash '/'
        return '/'+'/'.join(stack)