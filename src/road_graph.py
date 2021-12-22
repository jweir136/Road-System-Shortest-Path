import csv

class RoadwayGraph:
    def __init__(self, csv_filepath: str):
        self.adjDict: dict(str, list(Edge)) = {}
        self.coords = {}

        with open(csv_filepath, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                x, y, start, end, node_id, distance = row

                if not start in self.adjDict:
                    self.adjDict[start] = [(end, float(distance))]
                else:
                    self.adjDict[start].append((end, float(distance)))

                if not start in self.coords:
                    self.coords[start] = (x, y)

    def add_road(self, start: str, end: str, distance: float, one_way=False):
        if not start in self.adjDict:
            self.adjDict[start] = [(end, float(distance))]
        else:
            self.adjDict[start].append((end, float(distance)))

        if one_way == False:
            if not end in self.adjDict:
                self.adjDict[end] = [(start, float(distance))]
            else:
                self.adjDict[end].append((start, float(distance)))
            
    def shortest_path(self, start, end):
        def h(node):
            return 1
        
        def get_neighbors(v):
            return self.adjDict[v]

        open_list = set([start])
        closed_list = set([])
        g = {}
        g[start] = 0
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + h(v) < g[n] + h(n):
                    n = v;

            if n == None:
                return None

                 # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return reconst_path

            for (m, weight) in get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            
            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)
        
        return None

if __name__ == "__main__":
    r = RoadwayGraph("test-data/Karachi/Karachi_Edgelist.csv")
    print(r.shortest_path('1', '992'))