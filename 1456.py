
def maxVowels(s: str, k: int) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    left, right = 0, k - 1

    count = len([char for char in s[left:right + 1] if char in vowels])
    max_count = count

    while right < len(s) - 1:
        right += 1
        if s[right] in vowels:
            count += 1

        if s[left] in vowels:
            count -= 1
        left += 1

        if count == k:
            return count
        
        if count > max_count:
            max_count = count
        
    return max_count



if __name__ == '__main__':
    print(maxVowels('zpuerktejfp', 3))