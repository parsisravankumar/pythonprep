"""18.The distance between two cities in Km. is input through the keyboard. Write a
program to convert and print the result in meters and centimetres"""
distance_in_kms = float(input("enter the kms"))
distance_in_meters = distance_in_kms * 1000
distance_in_centimetres = distance_in_kms * 100000
print("The distance between the two cities is:")
print("Meters:", distance_in_meters, "m")
print("Centimeters:", distance_in_centimetres, "cm")

