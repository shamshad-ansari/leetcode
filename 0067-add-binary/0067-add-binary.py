class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Need to check if carry number exist at that index before adding
        carry = 0
        m = len(a) - 1
        n = len(b) - 1
        result = []
        while n >= 0 or m >= 0 or carry > 0:
            n1 = a[m] if m>=0 else '0'
            n2 = b[n] if n>=0 else '0'
            if n1 == '1' and n2 == '1' and carry == 1:
                result.append('1')
                carry = 1
            elif carry == 1 and n1 == '0' and n2 =='0':
                result.append('1')
                carry = 0
            elif carry == 1 and (n1 == '1' or n2 =='1'):
                result.append('0')
                carry = 1
            elif n1 == '1' and n2 == '1' and carry == 0:
                result.append('0')
                carry = 1
            elif carry == 0 and (n1 == '1' or n2 =='1'):
                result.append('1')
                carry = 0
            else:
                result.append('0')
                carry = 0
            n -= 1
            m -=1
        return ''.join(result[::-1])