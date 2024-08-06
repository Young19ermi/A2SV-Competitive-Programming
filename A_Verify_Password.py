
def is_strong_password(password):
    digits = ''.join([ch for ch in password if ch.isdigit()])
    letters = ''.join([ch for ch in password if ch.isalpha()])
    
   
    if digits != ''.join(sorted(digits)):
        return "NO"
    
    
    if letters != ''.join(sorted(letters)):
        return "NO"
    

    seen_letter = False
    for ch in password:
        if ch.isdigit() and seen_letter:
            return "NO"
        if ch.isalpha():
            seen_letter = True
    
    return "YES"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        password = data[index + 1]
        index += 2
        results.append(is_strong_password(password))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()


