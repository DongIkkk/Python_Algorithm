def solution(s):
    p_count = s.count("p") + s.count("P")
    y_count = s.count("y") + s.count("Y")

    if p_count == y_count:
        return True
    else:
        return False