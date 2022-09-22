import csv
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    #raise NotImplementedError()
    m = []
    with open(csv_file_path, 'r') as read_j:
        csv_reader = csv.reader(read_j)
        for row in csv_reader:
            r = row
            for i in range(0,len(r)):
                x = r[i]
                if ord(x[0]) in range(49,58):
                    x = int(x)
                    r[i] = x
            m.append(r)
        return m
    
