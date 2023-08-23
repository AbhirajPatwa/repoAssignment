arr = [["AI161E90", "BLR", "BOM", 5600],
       ["BR161F91", "BOM", "BBI", 6750],
       ["AI161F99", "BBI", "BLR", 8210],
       ["VS171E20", "JLR", "BBI", 5500],
       ["AS171G30", "HYD", "JLR", 4400],
       ["AI131F49", "HYD", "BOM", 3499]]

x = int(input("Enter input type:\n1. ID\n2. source city\n3. destination city\n"))-1
a = input("Enter search: ")
print("")
for i in range(len(arr)):
    if arr[i][x] == a:
        print(f"Flight ID: {arr[i][0]}")
        print(f"Source City: {arr[i][1]}")
        print(f"Destination City: {arr[i][2]}")
        print(f"Price: {arr[i][3]}")
        print("")
