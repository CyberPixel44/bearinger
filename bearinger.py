# Author: CyberPixel44 - KO6BQJ
# 73s!
import math
import sys
def initial_bearing(lat1, lon1, lat2, lon2):
    #convert lat and long from deg to rad
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    #calculate delta long
    dlon = lon2 - lon1
    #spherical law of cosines
    x = math.sin(dlon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(dlon))
    bearing = math.atan2(x, y)
    #convert bearing from rad to deg
    bearing = math.degrees(bearing)
    #normalize
    bearing = (bearing + 360) % 360
    return bearing

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  #earth radius in km
    #convert lat and long from deg to rad
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    #calculate delta latit and long
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    #haversine formula
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance_short = R * c  #short path distance in km
    distance_long = (math.pi * 2 * R) - (R * c)  #long path distance in km
    return [distance_short, distance_long]

def grid_square_to_coordinates(maidenhead):
    if len(maidenhead) < 4 or len(maidenhead) % 2 != 0:
        raise ValueError("Invalid Maidenhead grid square length")
    #convert Maidenhead grid square to coords
    lon = (ord(maidenhead[0].upper()) - ord('A')) * 20 - 180
    lat = (ord(maidenhead[1].upper()) - ord('A')) * 10 - 90
    lon += (ord(maidenhead[2]) - ord('0')) * 2
    lat += (ord(maidenhead[3]) - ord('0'))
    if len(maidenhead) >= 6:
        lon += (ord(maidenhead[4].lower()) - ord('a')) * 5 / 60
        lat += (ord(maidenhead[5].lower()) - ord('a')) * 2.5 / 60
    return lat, lon

if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        print("Bearinger - Bearing, short path and long path distance calculator for amateur radio operations")
        print("\nUsage: python bearinger.py [options] [mode]")
        print("Options:")
        print("-h, --help\t\t\t\tShow this help message and exit")
        print("-mi, --miles\t\t\t\tDisplay distance in miles (default in km)")
        print("\nModes:")
        print("-i, --interactive\t\t\tRun in interactive mode")
        print("-l, --latlong lat1 lon1 lat2 lon2\tCalculate bearing and distance using latitude and longitude")
        print("-g, --grid grid1 grid2\t\t\tCalculate bearing and distance using Maidenhead grid square")
        exit(0)

    if "-i" in sys.argv or "--interactive" in sys.argv:
        print("Running in interactive mode")
        print("\nSelect distance unit:")
        print("[1] Miles")
        print("[2] Kilometers")
        units = input("Enter your selection [1/2]: ")
        print("\nSelect input method:")
        print("[1] Latitude and Longitude")
        print("[2] Maidenhead Grid Square")
        selection = int(input("Enter your selection [1/2]: "))

        if selection == 1:
            lat1 = float(input("Enter latitude for Location 1: "))
            lon1 = float(input("Enter longitude for Location 1: "))
            lat2 = float(input("Enter latitude for Location 2: "))
            lon2 = float(input("Enter longitude for Location 2: "))
        elif selection == 2:
            grid_square1 = input("Enter Maidenhead grid square for Location 1: ")
            grid_square2 = input("Enter Maidenhead grid square for Location 2: ")
            lat1, lon1 = grid_square_to_coordinates(grid_square1)
            lat2, lon2 = grid_square_to_coordinates(grid_square2)
        else:
            print("Invalid selection")
            exit(1)

        bearing = initial_bearing(lat1, lon1, lat2, lon2)
        distance = haversine(lat1, lon1, lat2, lon2)

        print("\n----------- Results -----------")
        print(f"Bearing: {bearing:.2f} degrees")
        if units == "1":
            distance[0] *= 0.621371  # convert km to miles
            distance[1] *= 0.621371  # convert km to miles
            print(f"Short Path Distance: {distance[0]:.2f} miles")
            print(f"Long Path Distance: {distance[1]:.2f} miles")
        elif units == "2":
            print(f"Short Path Distance: {distance[0]:.2f} km")
            print(f"Long Path Distance: {distance[1]:.2f} km")

    if "-l" in sys.argv or "--latlong" in sys.argv:
        if "-l" in sys.argv:
            if len(sys.argv) < sys.argv.index("-l") + 5 or len(sys.argv) > sys.argv.index("-l") + 5:
                print("Invalid number of arguments for -l")
                print("Usage: python bearinger.py -l lat1 lon1 lat2 lon2")
                exit(1)
            try:
                lat1 = float(sys.argv[sys.argv.index("-l") + 1])
                lon1 = float(sys.argv[sys.argv.index("-l") + 2])
                lat2 = float(sys.argv[sys.argv.index("-l") + 3])
                lon2 = float(sys.argv[sys.argv.index("-l") + 4])
            except ValueError:
                print("Invalid input type for latitude or longitude")
                exit(1)
        elif "--latlong" in sys.argv:
            if len(sys.argv) < sys.argv.index("--latlong") + 5 or len(sys.argv) > sys.argv.index("--latlong") + 5:
                print("Invalid number of arguments for --latlong")
                print("Usage: python bearinger.py --latlong lat1 lon1 lat2 lon2")
                exit(1)
            try:
                lat1 = float(sys.argv[sys.argv.index("--latlong") + 1])
                lon1 = float(sys.argv[sys.argv.index("--latlong") + 2])
                lat2 = float(sys.argv[sys.argv.index("--latlong") + 3])
                lon2 = float(sys.argv[sys.argv.index("--latlong") + 4])
            except ValueError:
                print("Invalid input type for latitude or longitude")
                exit(1)
        bearing = initial_bearing(lat1, lon1, lat2, lon2)
        distance = haversine(lat1, lon1, lat2, lon2)
        print(f"Bearing: {bearing:.2f} degrees")
        if "-mi" in sys.argv or "--miles" in sys.argv:
            distance[0] *= 0.621371  # convert km to miles
            distance[1] *= 0.621371  # convert km to miles
            print(f"Short Path Distance: {distance[0]:.2f} miles")
            print(f"Long Path Distance: {distance[1]:.2f} miles")
        else:
            print(f"Short Path Distance: {distance[0]:.2f} km")
            print(f"Long Path Distance: {distance[1]:.2f} km")

    if "-g" in sys.argv or "--grid" in sys.argv:
        if "-g" in sys.argv:
            if len(sys.argv) < sys.argv.index("-g") + 3 or len(sys.argv) > sys.argv.index("-g") + 3:
                print("Invalid number of arguments for -g")
                print("Usage: python bearinger.py -g grid1 grid2")
                exit(1)
            grid_square1 = sys.argv[sys.argv.index("-g") + 1]
            grid_square2 = sys.argv[sys.argv.index("-g") + 2]

        elif "--grid" in sys.argv:
            if len(sys.argv) < sys.argv.index("--grid") + 3 or len(sys.argv) > sys.argv.index("--grid") + 3:
                print("Invalid number of arguments for --grid")
                print("Usage: python bearinger.py --grid grid1 grid2")
                exit(1)
            grid_square1 = sys.argv[sys.argv.index("--grid") + 1]
            grid_square2 = sys.argv[sys.argv.index("--grid") + 2]
            
        try:
            lat1, lon1 = grid_square_to_coordinates(grid_square1)
            lat2, lon2 = grid_square_to_coordinates(grid_square2)
        except ValueError:
            print("Invalid input type for grid square")
            exit(1)
            
        bearing = initial_bearing(lat1, lon1, lat2, lon2)
        distance = haversine(lat1, lon1, lat2, lon2)
        print(f"Bearing: {bearing:.2f} degrees")
        if "-mi" in sys.argv or "--miles" in sys.argv:
            distance[0] *= 0.621371  # convert km to miles
            distance[1] *= 0.621371  # convert km to miles
            print(f"Short Path Distance: {distance[0]:.2f} miles")
            print(f"Long Path Distance: {distance[1]:.2f} miles")
        else:
            print(f"Short Path Distance: {distance[0]:.2f} km")
            print(f"Long Path Distance: {distance[1]:.2f} km")
