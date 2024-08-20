class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [*s]
        vowels = ['a', 'e', 'i', 'o', 'u']

        left = 0
        right = len(s) - 1

        while not left >= right:
            if s[left].lower() in vowels:
                if s[right].lower() in vowels:
                    leftV = s[left]
                    rightV = s[right]

                    s[left] = rightV
                    s[right] = leftV

                    left+= 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        
        return ''.join(s)

