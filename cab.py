
wthresh = 32

def cab(t, w, h, d, n, p, drw, f, o):
    global wthresh
    # t = type, w = width, h = height, d= depth, n = number shelves, d = number drawers, f = number finished ends, o = open cab defaults to y
    # returns mos = open side, mfe = finished ends, mosh = open shelves, motb = top and bottom, labor = shop labor
    uot = 0.00 #top
    uotw = 0.00 #top wide
    uob = 0.00 #bottom
    uobw = 0.00 #bottom wide
    uoe = 0.00 #end
    uof = 0.00 #fin end
    uos = 0.00 #shelf
    uosw = 0.00 #shelf wide

    if t == 1:
        if o == 1:
            if f == 0:
                uoe = (2 * h * d) / 144.00 #end
            if f == 1:
                uoe = (h * d) / 144.00 #end
                uof = (h * d) / 144.00 #fin end
            if f == 2:
                uof = (2 * h * d) / 144.00
            if f > 2:
                print "error invalid number of finished ends selected, must be between 0-2"
            if w < wthresh:
                uot = w * d / 144.00 #top
                uob = w * d / 144.00 #bottom
                uos = n * (w * d / 144.00) #shelves
            if w > wthresh:
                uotw = w * d / 144.00 #wide top
                uobw = w * d / 144.00 #wide bottom
                uosw = n * (w * d / 144.00) #wide shelves

            return uot, uotw, uob, uobw, uoe, uof, uos,uosw

cab(1,45,17,15,2,0,0,1,1)

'''uot top
uotw top wide
uob bottom
uobw bottom wide
uoe end
uof fin end
uos shelf
uosw shelf wide'''