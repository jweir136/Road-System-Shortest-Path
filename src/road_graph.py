import csv

class Edge:
    def __init__(self, start: str, end: str, distance: float):
        self.start = start
        self.end = end
        self.distance = distance

    def __repr__(self):
        return "[start: {}, end: {}, distance: {}]".format(self.start, self.end, self.distance)

class RoadwayGraph:
    def __init__(self, csv_filepath: str):
        self.adjDict: dict(str, list(Edge)) = {}

        with open(csv_filepath, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                x, y, start, end, node_id, distance = row

                if not start in self.adjDict:
                    self.adjDict[start] = [Edge(start, end, distance)]
                else:
                    self.adjDict[start].append(Edge(start, end, distance))

    def add_road(self, start: str, end: str, distance: float, one_way=False):
        if not start in self.adjDict:
            self.adjDict[start] = [Edge(start, end, distance)]
        else:
            self.adjDict[start].append(Edge(start, end, distance))

        if one_way == False:
            if not end in self.adjDict:
                self.adjDict[end] = [Edge(end, start, distance)]
            else:
                self.adjDict[end].append(Edge(end, start, distance))

if __name__ == "__main__":
    r = RoadwayGraph("test-data/Karachi/Karachi_Edgelist.csv")
    print(r.adjDict)