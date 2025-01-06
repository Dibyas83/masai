import csv
import json


def cjs():
    d= { "phy":70,"chem":80,"skills":["python","django","machine learning"]}
    with open("csyes.csv","a") as f1:
        writer =csv.writer(f1)
        writer.writerow(["chem",60])
        f1.close()

    with open("csyes.csv","r") as f1:
        reader = csv.DictReader(f1)
        dat =list(reader)
        #print(dat)
        #for row in reader:
            #print(row)
        for row in dat[1:]:

            sb,scre = row
            su = int(scre)
            if su > 50:
                print(f"{sb},{scre}")

    with open("data.json","w") as f3:
        json.dump(d,f3,indent=4)

    with open("csyes.csv","r") as f3:
        loaded_per = json.load(f4)

    for skill in loaded_per["skills"]:
        print(skill)


cjs()





















