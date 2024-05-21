
stack = None

def parse_string(str):
    left_bracket = ['(','{','[']
    right_bracket = [')','}',']']
    #print(f'String: {str}')

    stack = []

    if str[0] in right_bracket:
        return False

    for s in str:
        #print(s)
        s_tmp = None
        if s in right_bracket and len(stack) == 0:
            return False

        if s in left_bracket:
            stack.append(s)
        elif s in right_bracket:
            s_tmp = stack[-1]
            if s_tmp in left_bracket and left_bracket.index(s_tmp) == right_bracket.index(s):
                stack.pop()
            else:
                return False
        else:
            continue
    #print(stack)
    return True if len(stack)==0 else False


if __name__ == "__main__":
    test_str = [
            '))((',
            '( ) { [ ] ( ) ( ) { } } }',
            '( ( ( )',
            '( }',
            '( ){[ 1 ]( 1 + 3 )( ){ }}',
            '( 23 ( 2 - 3);',
            '( 11 }']

    for i in test_str:
        if parse_string(i):
            print(f"Стрічка '{i}' є симетричною")
        else:
            print(f"Стрічка '{i}' не є симетричною")
