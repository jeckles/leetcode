'''

777

777

'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        zerosToAdd, products, num1, num2 = 0, [], list(num1), list(num2)
        i = len(num1) - 1
        while i >= 0:
            currProduct, zerosI, j, carry = [], 0, len(num2) - 1, 0
            while zerosI < zerosToAdd:
                currProduct.append(0)
                zerosI += 1
            while j >= 0:
                val, nextCarry = self.multiplyHelper(num1[i], num2[j], carry)
                currProduct.insert(0, val)
                carry = nextCarry
                if j == 0 and carry != 0:
                    currProduct.insert(0, carry)
                j -= 1
            zerosToAdd += 1
            products.append(currProduct)
            i -= 1
        products = [self.convertArrayToNum(x) for x in products]
        return sum(products)
        
    def multiplyHelper(self, num1, num2, c):
        num1, num2 = self.convertNum(num1), self.convertNum(num2)
        product = (num1 * num2) + c
        val, carry = product % 10, product // 10
        return (val, carry)
    
    def convertNum(self, num):
        if num == '0':
            return 0
        elif num == '1':
            return 1
        elif num == '2':
            return 2
        elif num == '3':
            return 3
        elif num == '4':
            return 4
        elif num == '5':
            return 5
        elif num == '6':
            return 6
        elif num == '7':
            return 7
        elif num == '8':
            return 8
        elif num == '9':
            return 9

    def convertArrayToNum(self, num):
        num = num[::-1] # reverse the list
        base, i, result = 10, 0, 0
        while i < len(num):
            val = num[i] * (base ** i)
            result += val
            i += 1
        return result


def main():
    sol = Solution()
    print(sol.multiply("0", "456"))

if __name__ == "__main__":
    main()
