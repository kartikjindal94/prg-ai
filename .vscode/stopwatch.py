hh=mm=sec=0
while hh<12:
    mm=0
    while mm<60:
        sec=0
        while sec<60:
            print(f"{hh}:{mm}:{sec}")
            sec+=1
        mm+=1
    hh+=1