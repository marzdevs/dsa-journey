def opposite_end(s: str) -> bool:
    Left = 0
    Right = len(s) - 1

    while Left < Right:
        if s[Left] != s[Right]:
            return False
        if s[Left] == s[Right]:
            Left += 1
            Right -= 1

    return True

