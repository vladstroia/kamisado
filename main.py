#color map
colorm=[[8, 7, 6, 5, 4, 3, 2, 1],
        [3, 8, 5, 2, 7, 4, 1, 6],
        [2, 5, 8, 3, 6, 1, 4, 7],
        [5, 6, 7, 8, 1, 2, 3, 4],
        [4, 3, 2, 1, 8, 7, 6, 5],
        [7, 4, 1, 6, 3, 8, 5, 2],
        [6, 1, 4, 7, 2, 5, 8, 3],
        [1, 2, 3, 4, 5, 6, 7, 8]]

#game map
gm=[[16, 15, 14, 13, 12, 11, 10, 9],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]]

gx=0
gy=0
dmax=18
it=0
col=["0","M","V","R","G","P","T","A","O","m","v","r","g","p","t","a","o"]
gpm=0
gpnm=0

def inboard(x,y):
    if x >= 0 and x < 8 and y >= 0 and y < 8:
        return True
    return False

def genmoves(m,p,t,moves):
    for i in [-1,0,1]:
        x=p[0] + i
        y=p[1] + t
        while inboard(x,y) is True and m[y][x] == 0:
            moves.append([x,y])
            x += i
            y += t

def over(m):
    for i in range (8):
        if m[0][i]>0 and m[0][i]<9:
            return True
        if m[7][i]>8:
            return True
    return False

def tie(m, p, t, pp):
    moves=[]
    genmoves(m,p,t,moves)
    if not moves:
        nextp=pp[colorm[p[0]][p[1]] + 4 - 4 * t]
        del moves[:]
        genmoves(m,nextp,-1*t,moves)
        if not moves:
            return True
    return False

def printm(m):
    for i in range (8):
        for ii in range(8):
            print (col[m[i][ii]],end=" ")
        print ("")

def applymove(m,pp,move,p,pn):
    m[move[1]][move[0]] = m[p[1]][p[0]]
    m[p[1]][p[0]] = 0
    pp[pn][0] = move[0]
    pp[pn][1] = move[1]

def reversemove(m,pp,move,p,pn):
    m[p[1]][p[0]] = pn
    m[move[1]][move[0]] = 0
    pp[pn][0] = p[0]
    pp[pn][1] = p[1]

#static evaluation
def static(m,p,rt):
    sc=0
    t=-1
    for y in [0, 7]:
        t=t*-1
        for x in range(8):
            for i in [-1,0,1]:
                cx=x
                cy=y
                while inboard(cx, cy) is True and m[cy][cx] == 0:
                    cx += i
                    cy += t
                if inboard(cx,cy) and t==1 and m[cy][cx] > 0 and m[cy][cx] < 9:
                    if rt != t:
                        if p[0]==cx and p[1]==cy:
                            return 20
                    sc-=rt
                if inboard(cx,cy) and t==-1 and m[cy][cx] > 8:
                    if rt != t:
                        if p[0]==cx and p[1]==cy:
                            return 20
                    sc+=rt
    return sc
def score(m,pp,p,t,pn,pha,bet,d):

    global gx,gy,dmax,gpnm

    if over(m):
        return -20
    if tie(m,p,t,pp):
        return 0
    if d==dmax:
        return static(m,p,t)

    moves=[]
    genmoves(m,p,t,moves)
    moves.sort(key=lambda x: -t*x[1])
    for move in moves:


        applymove(m,pp,move,p,pn)

        nextpn=colorm[move[1]][move[0]] + 4 - 4 * t
        nextp=pp[nextpn][:]

        csc= -score(m,pp,nextp,-1 * t,nextpn,-bet,-pha,d + 1)
        if csc > pha:
            pha=csc
            if d == 0:
                gx=move[0]
                gy=move[1]
                gpnm = m[move[1]][move[0]]
        reversemove(m,pp,move,p,pn)
        if pha >= bet:
            break
    if not moves:
        if d == 0:
            gx=p[0]
            gy=p[1]
        nextpn = colorm[p[1]][p[0]] + 4 - 4 * t
        nextp = pp[nextpn][:]
        pha = max(pha, -score(m, pp, nextp,-1 * t, nextpn, -bet, -pha, d + 1))
    return pha

#game piece positions
gpp=[[[0]],[0,7],[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],[7,0],[6,0],[5,0],[4,0],[3,0],[2,0],[1,0],[0,0]]

ct=1
gt=1
gpha= -100

printm(gm)
moves=[]
gpn=1
gp=gpp[gpn][:]
if gt != ct:
    gpn=int(input())
    while gpn < 1 or gpn > 8:
        gpn = int(input())
    gp=gpp[gpn][:]
while over(gm) is False and tie(gm , gp, gt, gpp) is False:
    printm(gm)
    if gt != ct:
        del moves[:]
        genmoves(gm,gp,gt,moves)
        print ( chr(ord('A') + gp[0]), 8 - gp[1])
        if not moves:
            str(input())
            gpn = colorm[gp[1]][gp[0]] + 4 - 4 * gt
            gp = gpp[gpn][:]
        else:
            gx = str(input())
            gx = ord(gx) - ord('A')
            gy = int(input())
            gy = 8 - gy
            while [gx, gy] in moves is False:
                gx = str(input())
                gx = ord(gx) - ord('A')
                gy = int(input())
                gy = 8 - gy
            applymove(gm, gpp, [gx, gy], gp, gpn)
            gpn = colorm[gy][gx] + 4 - 4 * gt
            gp = gpp[gpn].copy()


    else:
        del moves[:]
        genmoves(gm, gp, gt, moves)
        if it == 0:
            for i in range(4):
                gp = gpp[9+i][:]
                dmax=16
                gpha = max(gpha, score(gm, gpp, gp, gt, 9+i,gpha,100,0))
            gpm=gpp[gpnm][:]
            print(gpnm)
            applymove(gm, gpp, [gx, gy], gpm, gpnm)

            print("\n\n\n\n\nComputer move: ", chr(ord('A') + gx), 8 - gy)
            gpn = colorm[gy][gx] + 4 - 4 * gt
            gp = gpp[gpn][:]
        else:
            dmax=17
            while(dmax > 0 and score(gm, gpp, gp, gt, gpn,-100,100,0) == -20):
                dmax-=1
            print("\n\n\n\n\nComputer move: ",chr(ord('A') + gx) , 8 - gy)
            applymove(gm,gpp,[gx,gy],gp,gpn)
            gpn = colorm[gy][gx] + 4 - 4 * gt
            gp = gpp[gpn][:]
    gt=-1*gt
    it+=1
printm(gm)
if over(gm):
    if gt == 1:
        if ct == 1:
            print("Plyer won !")
        else:
            print("Player 1 won !")
    if gt == -1:
        if ct == 1:
            print("Computer won !")
        else:
            print("Player 2 won !")
else:
    print("Draw !")
