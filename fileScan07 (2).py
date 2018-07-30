#! /usr/bin/env python3.4
# We only need to import this module
import os.path
import re
import time
import cv2
import matplotlib.pyplot as plt

def freq(instring,tally):
    if None==tally(instring):
        tally[instring]=1
    else:
        tally[instring]+=1
def extract(rex, str, failStr):
    m = re.search(rex, str)  # leading score
    if m:
        return m.group()
    else:
        return failStr
    
def playVideo(path):
    cap = cv2.VideoCapture(path)
    ret, frame = cap.read()
    while(1):
       ret, frame = cap.read()
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
           cap.release()
           cv2.destroyAllWindows()
           break
       cv2.imshow('frame',frame)

def tx(tag, string, failStr):
    x = re.split("_", string)
    z = failStr
    for w in x:
        # print(w)
        if -1 < w.find(tag):
            z = w[2:]
            return z
    if z is None: return failStr
    return z


def sec2YMDHMS(sec):
    t = time.gmtime(sec)
    f = "{:04d}/{:02d}/{:02d}_{:02d}:{:02d}:{:02d}"
    return f.format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)


def getShape(nl):
    shape = "NULL"
    if (-1 < nl.find("bbw")) or (-1 < nl.find("fat")):  shape = "BBW"
    if (-1 < nl.find("sbbw")):  shape = "SBBW"
    if "chub" in nl or "plump" in nl: shape = "Chub"
    if -1 < nl.find("curvy"): shape = "Curvy"
    if -1 < nl.find("slim"): shape = "Slim"
    # print (nl+">>>"+shape)
    return shape


def getHair(nl):
    hair = "NULL"
    if -1 < nl.find("blo"): hair = "Blo"
    if -1 < nl.find("bru"): hair = "Bru"
    if -1 < nl.find("bla"): hair = "Bla"
    if -1 < nl.find("red"): hair = "Red"
    return hair


def getVenue(nl):
    venue = "NULL"
    if "pool" in nl or "bath" in nl or "shower" in nl: venue = "H2O"
    if "beach" in nl or "sauna" in nl or "lake" in nl: venue = "H2O"
    if "massage" in nl: venue = "Massage"
    if "maid" in nl: venue = "Maid"
    if "office" in nl or "secretary" in nl: venue = "Office"
    if "realestate" in nl: venue = "RealEstate"
    if "casting" in nl: venue = "Casting"
    if "nurse" in nl: venue = "Nurse"
    if "kitchen" in nl: venue = "Kitchen"
    if "farm" in nl or -1 < nl.find("barn"): venue = "Farm"
    if "danc" in nl: venue = "Dance"
    if "party" in nl: venue = "Party"
    if -1 < nl.find("club"): venue = "Club"
    if "webcam" in nl: venue = "Webcam"
    if -1 < nl.find("roman") and not (-1 < nl.find("romanian")): venue = "Roman"
    return venue


def getAct(nl):
    act = "NULL"
    if "_dildo_" in nl: act = "Dildo"
    if "_solo_" in nl or -1 < nl.find("masterbat"): act = "Solo"
    if -1 < nl.find("_hj_"): act = "HJ"
    if -1 < nl.find("_tf_"): act = "TF"
    if -1 < nl.find("_bj_"): act = "BJ"
    if -1 < nl.find("_x_"): act = "FM"
    if -1 < nl.find("_fm"): act = "FM"
    if -1 < nl.find("_ff"): act = "FF"
    if -1 < nl.find("ffm"): act = "FFM"
    if -1 < nl.find("fmm"): act = "FMM"
    if -1 < nl.find("_mf_"): act = "FM"
    if "interview" in nl: act = "Intvw"
    return act


def getBonus(nl):
    bonus = "NULL"
    bonus = tx("b=", nl, "NULL")
    # print("bonus01: "+bonus)
    if -1 < bonus.find("B?"):
        if -1 < nl.find("natural"): bonus = "Nat"
        if -1 < nl.find("pneumo"): bonus = "Pneumo"
        if (-1 < nl.find("puff")):  bonus = "Puff"
        if (-1 < nl.find("perky")):  bonus = "Perky"
        if (-1 < nl.find("saggy")):  bonus = "Saggy"
        if -1 < nl.find("hb") and not (-1 < nl.find("bbw")): bonus = "HB"
        # print("bonus02: "+bonus)
    return bonus


def getComment(nl):
    comment = "NULL"
    comment = tx("c=", nl, "NULL")
    # print("comment01: "+comment)
    if -1 < comment.find("NULL"):
        if (-1 < nl.find("milf")) or (-1 < nl.find("mature")) or (-1 < nl.find("mom")):
            comment = "MILF"
        if (-1 < nl.find("granny")): comment = "MILF"
        if -1 < nl.find("preg"): comment = "Preg"
        if -1 < nl.find("joi"): comment = "JOI"
        if -1 < nl.find("ass"): comment = "Ass"
        if (-1 < nl.find("milk")) or (-1 < nl.find("lact")):  comment = "Lact"
        if (-1 < nl.find("cute")):  comment = "cute"
        if (-1 < nl.find("beatiful")):  comment = "Beautiful"
        if (-1 < nl.find("movie")):  comment = "Movie"
        if (-1 < nl.find("plot")):  comment = "Plot"
        if (-1 < nl.find("parody")):  comment = "Parody"
        # print("comment02: "+comment)
    return comment


def getNationality(nl):
    nat = "NULL"
    nat = tx("n=", nl, "NULL")
    if -1 < nat.find("NULL"):
        if -1 < nl.find("french"): nat = "fr"
        if "german" in nl or "annabeck" in nl: nat = "de"
        if -1 < nl.find("british") or -1 < nl.find("uk"): nat = "uk"
        if -1 < nl.find("italian"): nat = "it"
        if "slavic" in nl: nat = "sl"
        if -1 < nl.find("polish"): nat = "po"
        if "hitomi" in nl: nat = "jp"
        if -1 < nl.find("lat"): nat = "lat"
        if -1 < nl.find("czech"): nat = "ck"
        if -1 < nl.find("russian"): nat = "ru"
        if -1 < nl.find("israel"): nat = "il"
        if -1 < nl.find("turkish"): nat = "tk"
        if -1 < nl.find("eli") and not (-1 < nl.find("eliz")): nat = "sp"
        if -1 < nl.find("romanian"): nat = "ro"
        if -1 < nl.find("arriana") or -1 < nl.find("alice85jj"): nat = "ro"
        if -1 < nl.find("us"): nat = "us"
    return nat


def getScore(nl):
    return tx("s=", nl, "0000")


def getHeight(nl):
    return tx("h=", nl, "NULL")


def getWeight(nl):
    return tx("w=", nl, "NULL")

def getYear(nl):
    return tx("y=", nl, 0)

def getMeas(nl):  # if (num<40 && letter) then a=+1,b=+2..,f=+5
    m = tx("m=", nl, "NULL")
    num = re.split("-", m)+['0','0','0']
    if num[0] == "NULL": return [m, m, m]
    c = extract("[a-z|A-Z]", num[0], "")
    # print( m+" "+c+" "+nl)
    if c == "": return num
    num[0] = int(num[0]) + "$abcdefghijklmnopqrstuvwxyz".find(c)
    return [str(num[0]), str(num[1]), str(num[2])]


def getStats(h, w, mb, mw, mh):
    if h == "NULL" or h == "": h = 1
    if w == "NULL" or w == "": w = 1
    if mb == "NULL" or mb == "": mb = 1
    if mw == "NULL" or mw == "": mw = 1
    if mh == "NULL" or mh == "": mh = 1
    # print(w,type(w))
    h = float(h);
    w = float(w);
    mb = float(mb);
    mw = float(mw);
    mh = float(mh)
    if h>0:        bmi = (w / h ** 2)
    else: bmi=0
    if mw>0:        b2w, h2w = ( mb / mw, mh / mw)
    else:b2w,h2w=(0,0)
    return (bmi, b2w, h2w)


# The top argument for walk
topdir = 'f:\\ae'
# topdir = 'e:\\ae\\_inQueue'  #@@@@
# topdir = 'e:\\ae\\A'
ts = time.time()
f = open('f:\\ae\\_inQueue\\AE' + str(ts) + '.csv', 'w')
f.write(
    "Path\tFile\tBytes\tScore\tResolution\tHair\tShape\tBonus\tCom\tHeight\tWeight\tMB\tMW\tMH\tVenue\tAct\tNat\tAcc\tMod\tBMI\tBr/Waist\tHip/Waist\tYear\n")
# The extension to search for
mp4Ct = byteCt = folderCt = prefCt = 0
# score freq distribution buckets
buckets = [0 * x for x in range(64)]
print("Length scoreBuckets " + str(len(buckets)))
resBuckets = [0 * x for x in range(64)]
for b in range(0, 6):
    resBuckets += resBuckets
print("Length resBuckets " + str(len(buckets)))
tally={}
for dirpath, dirnames, files in os.walk(topdir):  # what is the order of returns from os.walk
    # print(0/(1-1))
    files.sort()
    
    pref = ""
    if len(files) > 0:
        folderCt += 1
        # files=files.sort()
        scoreP = "0000"
        if files[0].startswith("0_") and files[0].endswith(".txt"):  # assumes files[0] is prefix
            pref = files[0].lower()
            pref = pref.replace(".txt", "")
            # print("pref = "+pref)
            scoreP = getScore(pref)
            prefCt += 1
        for name in files:
            nl = name.lower()
            if nl.endswith(".mp4") or nl.endswith(".wmv") or nl.endswith(".mpg"):  # video file types
                mp4Ct += 1
                #print(dirpath+"\\"+name)  # was a comment
                #playVideo(dirpath+"\\"+name)
                if (mp4Ct % 1000 == 0): print(".mp4 count " + str(mp4Ct) + " prefCt " + str(prefCt))
                info = os.stat(os.path.join(dirpath, name))
                byteCt += info.st_size
                lastAccess = info.st_atime  # seconds
                lastAccessStr = (sec2YMDHMS(lastAccess))[:-9]
                lastMod = info.st_mtime
                lastModStr = (sec2YMDHMS(lastMod))[:-9]
                score = extract("^(\d\d\d\d)", name, scoreP)
                t = min(int(float(score) / 100), len(buckets) - 1)
                buckets[t] += 1
                resolution = extract("(\d)+[pP]", name, "0000p")[:-1]
                t = 20 * int(int(resolution) / 20)  # round to nearest 20
                if t >= len(resBuckets):
                    # print (resolution+" "+dirpath+" "+name)
                    t = 0
                resBuckets[t] += 1
                nl = nl.replace(" ", "")
                # print(pref)
                freq(shape,tally)
                s = nl + pref
                shape, bonus, comment = (getShape(s), getBonus(s), getComment(s))
                hair, height, weight, meas = (getHair(s), getHeight(s), getWeight(s), getMeas(s))
                stats = getStats(height, weight, meas[0], meas[1], meas[2])
                # if meas!="M?":print(meas)
                venue, act = (getVenue(s), getAct(s))
                nat = getNationality(dirpath.lower() + s)
                year = getYear(s)
                a = "\t"  # @@@@# a is tab char
                line = os.path.join(dirpath, a + name + a + str(info.st_size)) + a + score + a + resolution
                line = line + a + hair + a + shape + a + bonus + a + comment + a + height + a + weight
                # print(meas)
                line = line + a + meas[0] + a + meas[1] + a + meas[2]
                line = line + a + venue + a + act + a + nat
                line = line + a + str(lastAccessStr) + a + str(lastModStr) + a + str(stats[0]) + a + str(
                    stats[1]) + a + str(stats[2])+a+str(year)
                # print(line) # @@@@@
                f.write(line + "\n")  # python will convert \n to os.linesep
f.close()  # you can omit in most cases as the destructor will call it
print(tally)
print("Video files : " + str(mp4Ct))
print("Gbytes      : %9.3f" % (byteCt * 1e-9))
print("folderCt    : " + str(folderCt))
print("prefCt      : " + str(prefCt))
print("Length buckets " + str(len(buckets)))
plt.ion()  # interactive on
plt.figure(1)
plt.subplot(111)
plt.semilogx([i * 100 for i in range(len(buckets))], buckets, "bo"); plt.title("Video Scores"); plt.xlabel("Scores")
plt.ylabel("Freq")
plt.show()
print("i score freq")
"""for i in range(len(buckets)):
    if buckets[i]!=0:
        print(i,i*100,buckets[i])"""
print("i freqRes")
plt.figure(2)
plt.subplot(111)
plt.semilogy([i for i in range(len(resBuckets))], resBuckets, "bo")
plt.title("Resolutions")
plt.xlabel("Res")
plt.ylabel("Freq")
plt.show()
"""for i in range(len(resBuckets)):
    if (resBuckets[i]!=0) and (i>200):
        print(i,resBuckets[i])"""
