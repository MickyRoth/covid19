# Aktuelle Covid19 Zahlen Deutschland

import requests

url="https://api.covid19api.com/country/germany"

r=requests.get(url)
if r.status_code==200:
    print("HTTP 200 OK\n")
    #print(r.encoding)
    #print(r.headers)
    antwort=r.json()
    #print(antwort[0])
    confirmed=[]
    dead=[]
    recovered=[]
    active=[]
    new=[]

    for i in range(-1,-8,-1):
        confirmed.append(antwort[i]["Confirmed"])
        dead.append(antwort[i]["Deaths"])
        recovered.append(antwort[i]["Recovered"])
        active.append(antwort[i]["Active"])
        new.append(antwort[i]["Confirmed"] - antwort[i-1]["Confirmed"])
    datum=antwort[-1]["Date"][2:10]
    datum=datum[6:8]+"."+datum[3:5]+"."+datum[0:2]
    print("Covid19-Zahlen der letzten Woche(Deutschland):\n")
    print("Datum: {}|   -1t  |   -2t  |   -3t  |   -4t  |   -5t  |  -6t".format(datum))
    print("---------------+--------+--------+--------+--------+--------+-------")
    print("Fälle:  {:6} | {:6} | {:6} | {:6} | {:6} | {:6} | {:6}".format(confirmed[0],confirmed[1],confirmed[2],confirmed[3],confirmed[4],confirmed[5],confirmed[6]))
    print("Tote:   {:6} | {:6} | {:6} | {:6} | {:6} | {:6} | {:6}".format(dead[0],dead[1],dead[2],dead[3],dead[4],dead[5],dead[6]))
    print("Gesund: {:6} | {:6} | {:6} | {:6} | {:6} | {:6} | {:6}".format(recovered[0],recovered[1],recovered[2],recovered[3],recovered[4],recovered[5],recovered[6]))
    print("Krank:  {:6} | {:6} | {:6} | {:6} | {:6} | {:6} | {:6}".format(active[0],active[1],active[2],active[3],active[4],active[5],active[6]))
    print("Neue:   {:6} | {:6} | {:6} | {:6} | {:6} | {:6} | {:6}".format(new[0],new[1],new[2],new[3],new[4],new[5],new[6]))

else: print("api.covid19api.com antwortet nicht")
