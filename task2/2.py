import sys
ellipse_file = sys.argv[1]

with open(ellipse_file, 'r') as file:
    el_x, el_y = map(float, file.readline().split(' '))
    r1, r2 = map(float, file.readline().split(' '))


points = sys.argv[2]

with open(points, 'r') as file:
    for line in file:
        point_x = float(line.split(' ')[0])
        point_y = float(line.split(' ')[1])
        ellips = ((point_x - el_x)**2) / (r1**2) + ((point_y - el_y)**2)/(r2**2)

        if ellips == 1:  
            print(0)  
        elif ellips < 1:
            print(1)  
        else:
            print(2)  

