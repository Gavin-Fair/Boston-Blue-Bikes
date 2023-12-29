import csv
import math
from matplotlib import pyplot as plt


def main():

    def getCoordinates(station):
        for j in stationsDict:
            if j.__contains__(station):
                coordinates = (stationsDict[stationsDict.index(j)][station])
                coordinates = (coordinates[0], coordinates[1])
                return coordinates

    def haversine_distance(start, end):
        EARTH_RADIUS = 3959
        lat1 = start[0]
        long1 = start[1]
        lat2 = end[0]
        long2 = end[1]
        lat1 = math.radians(lat1)
        long1 = math.radians(long1)
        lat2 = math.radians(lat2)
        long2 = math.radians(long2)
        delta_lat = lat2 - lat1
        delta_long = long2 - long1
        a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_long / 2) ** 2
        haversine = EARTH_RADIUS * 2 * math.asin(math.sqrt(a))
        return haversine

    with open('stations.csv', 'r') as f:
        next(f)
        reader = csv.reader(f)
        stationsDict = []
        for i in reader:
            stationsDict.append({i[0]: [float(i[1]), float(i[2])]})

    with open('trips.csv', 'r') as f:
        next(f)
        reader = csv.reader(f)
        tripsDict = []
        distances = []
        speeds = []

        for i in reader:
            distances.append(haversine_distance(getCoordinates(i[3]), getCoordinates(i[4])))
            speeds.append((haversine_distance(getCoordinates(i[3]), getCoordinates(i[4]))) / (int(i[0]) / 3600))
            tripsDict.append({'duration': int(i[0]), 'start_day': int(i[1]), 'start_day_name': i[2],
                              'start_station': i[3], 'end_station': i[4], 'bike_id': int(i[5]),
                              'dist': haversine_distance(getCoordinates(i[3]), getCoordinates(i[4])),
                              'mph': (haversine_distance(getCoordinates(i[3]), getCoordinates(i[4]))) / (
                                      int(i[0]) / 3600)})


    def plot():
        plt.subplot(2, 1, 1)
        plt.hist(distances, bins=100, ec="black")
        plt.title("How far people travel on blue bikes in Boston")
        plt.xlabel("Distances in Miles")
        plt.ylabel("Frequency of occurrence")

        plt.subplot(2, 1, 2)
        plt.hist(speeds, bins=100, ec="black")
        plt.title("How fast people travel on blue bikes in Boston")
        plt.xlabel("Speed of bike in mph")
        plt.ylabel("Frequency of occurrence")

        plt.tight_layout()
        plt.show()

    plot()


if __name__ == "__main__":
    main()
