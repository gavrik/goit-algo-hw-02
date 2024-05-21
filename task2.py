from collections import deque

dq = deque()

def fill_deque(str):
    for s in str.lower():
        if s != ' ':
            dq.append(s)

def test_palindrom(is_debug=False):
    is_palindrome = False
    if is_debug:
        print(dq)
    while dq:
        s_right = dq.pop()
        s_left = dq.popleft() if dq else s_right

        if is_debug:
            print(f"{s_left}:{s_right}")

        if s_right == s_left:
            is_palindrome = True
            continue
        else:
            is_palindrome = False
            break

    return is_palindrome
        

if __name__ == "__main__":
    print("Put the string:")
    str = input()
    fill_deque(str)
    if test_palindrom():
        print("Стрічка є паліндромом")
    else:
        print("Стрічка не є паліндромом")
