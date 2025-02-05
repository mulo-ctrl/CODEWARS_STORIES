def win_or_lose(matches):
    return sum(3 if int(x) > int(y) else 1 if int(x) == int(y) else 0 for x, y in (match.split(":") for match in matches))

matches = ["3:1", "2:2", "0:1", "4:0", "1:1", "2:1", "0:0", "1:3", "3:2", "1:0"]
print(win_or_lose(matches))
git push origin main