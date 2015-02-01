
wthresh = 32

def cab(t, e, w, h, d, n, p, drw, f, l):
    global wthresh
    # t = type, open, w = width, h = height, d= depth, n = number shelves, d = number drawers, f = number finished ends,
    # returns mos = open side, mfe = finished ends, mosh = open shelves, motb = top and bottom, labor = shop labor
    uot = 0.00 #top
    uotw = 0.00 #top wide
    uob = 0.00 #bottom
    uobw = 0.00 #bottom wide
    uoe = 0.00 #end
    uof = 0.00 #fin end
    uos = 0.00 #shelf
    uosw = 0.00 #shelf wide
    uct = 0.00 #top
    uctw = 0.00 #top wide
    ucb = 0.00 #bottom
    ucbw = 0.00 #bottom wide
    uce = 0.00 #end
    ucf = 0.00 #fin end
    ucs = 0.00 #shelf
    ucsw = 0.00 #shelf wide
    udr = 0.0 # doors
    hnges = 0 #hinges
    eeb = 0 #exposed edgebanding
    ceb = 0 #concealed edgebanding
    locks = 0 #locks

    if t == 1: #cab type 1 = upper
        if e == 1: # cab is open type
            if f == 0: # f is qty fin ends
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
            eeb = 2 * w + 2 * h + n * w + p * h

        if e == 0: #cab is closed type
            if f == 0: # f is qty fin ends
                uce = (2 * h * d) / 144.00 #end
            if f == 1:
                uce = (h * d) / 144.00 #end
                ucf = (h * d) / 144.00 #fin end
            if f == 2:
                ucf = (2 * h * d) / 144.00
            if f > 2:
                print "error invalid number of finished ends selected, must be between 0-2"
            if w < wthresh:
                uct = w * d / 144.00 #top
                ucb = w * d / 144.00 #bottom
                ucs = n * (w * d / 144.00) #shelves
            if w > wthresh:
                uctw = w * d / 144.00 #wide top
                ucbw = w * d / 14.00 #wide bottom
                ucsw = n * (w * d / 144.00) #wide shelves
            hnges = d * 2
            udr = w * h
            ceb = 2 * w + 2 * h + n * w + p * h
            eeb = 2 * w + (2 * d * h)

    return (uot, uotw, uob, uobw, uoe, uof, uos, uosw, uct, uctw, ucb, ucbw, uce, ucf, ucs, ucsw, hnges, udr)

cab(1, 0, 45, 17, 15, 2, 1, 0, 1, 1)

'''
uot top
uotw top wide
uob bottom
uobw bottom wide
uoe end
uof fin end
uos shelf
uosw shelf wide
uct
uctw = 0.00 #top wide
ucb = 0.00 #bottom
ucbw = 0.00 #bottom wide
uce = 0.00 #end
ucf = 0.00 #fin end
ucs = 0.00 #shelf
ucsw = 0.00 #shelf wide
hnges = 0 # qty hinges
udr = = door


'''