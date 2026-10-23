# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf4 = [""] * 4
        self.pos = 0       # Next unread position in buf4
        self.count = 0     # Number of valid characters in buf4

    def read(self, buf: List[str], n: int) -> int:
        copied = 0

        while copied < n:
            # Refill only after using all buffered characters.
            if self.pos == self.count:
                self.count = read4(self.buf4)
                self.pos = 0

                if self.count == 0:
                    break

            buf[copied] = self.buf4[self.pos]
            copied += 1
            self.pos += 1

        return copied