# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
class Solution:
    def __init__(self):
        self.buf4 = [""] * 4
        self.size = 0
        self.ptr = 0

    def read(self, buf: List[str], n: int) -> int:
        total = 0

        while total < n:
            if self.ptr == self.size:
                self.size = read4(self.buf4)
                self.ptr = 0

                if self.size == 0:
                    break

            while total < n and self.ptr < self.size:
                buf[total] = self.buf4[self.ptr]
                total += 1
                self.ptr += 1

        return total