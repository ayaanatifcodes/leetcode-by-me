class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = 0
        read = 0
        while read < n:
            ch = chars[read]
            start = read
            while read < n and chars[read] == ch:
                read += 1
            cnt = read - start
            chars[write] = ch
            write += 1
            if cnt > 1:
                for d in str(cnt):
                    chars[write] = d
                    write += 1
        return write
