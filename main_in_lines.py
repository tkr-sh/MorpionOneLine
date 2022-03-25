p = print
p("Welcome to morpion in one line!")
b = [" "]*9
t = False
while True:
    p(f"Turn of player {t+1}")
    p("\n".join(("-"*7+"\n|"+"|".join(b[i*3:i*3+3])+"|"+["","","\n"+"-"*7][i])for i in range(3)))
    n = int(input(">"))

    if 0<=n<9 and b[n]==" ":
        p("Valid")
        t = not(t)
        b = b[:n]+["OX"[t]]+b[n+1:]
    else:
        p("You should put a number in [0;8] which isn't taken")

    if sum(b[int("00012362"[i])]==b[int("14345474"[i])]==b[int("28678586"[i])]=="OX"[t]for i in range(8))>0:
        p(f"Player {int(not(t))+1} won!\nEND OF THE GAME.")
        exit()
    elif b.count(" ")==0:
        p("TIE\nEND OF THE GAME.")
        exit()
