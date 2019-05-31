def camelcase(s):
      # Complete this function
    cnt = 1
    for i in s:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            cnt += 1
    return cnt
