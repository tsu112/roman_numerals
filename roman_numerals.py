class Solution:
    # This calls the function and converts it into a interger
    def romanToInt(self, s: str) -> int:

        # This is providing a dictonary of what each value equals to
        roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}

        ans = 0  # This starts the anwser at 0

        # This cycles the i through the entire length of the roman numeral given
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                ans -= roman[s[i]]
            else:
                ans += roman[s[i]]

        return ans
