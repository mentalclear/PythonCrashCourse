import json
import urllib.request

def printResults(data):
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    count=theJSON["metadata"]["count"]
    print(str(count) + " events")

    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("----------------\n")

    for i in theJSON["features"]:
        if i["properties"]["mag"] >=2.0:
            print(str(i["properties"]["mag"], ["properties"]["place"]))


def main():

    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
    webUrl=urllib.request.urlopen(urlData)
    print("res " + str(webUrl.getcode()))


    if(webUrl.getcode()== 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("error")


if __name__ == '__main__':
    main()