# import sys

# def geohash(latitude, longitude, accuracy):
#     try:
#         longitude = float(longitude)
#         latitude = float(latitude)
#         accuracy = int(accuracy)

#         result = ''
#         minLongitude = -180
#         maxLongitude = 180
#         minLatitude = -90
#         maxLatitude = 90

#         base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
#         isLongitude = True
#         while accuracy:
#             bitlen = 5
#             bits = 0

#             while bitlen:
#                 if isLongitude:
#                     mid = (minLongitude + maxLongitude) / 2

#                     if longitude >= mid:
#                         bits = bits * 2 + 1
#                         minLongitude = mid
#                     else:
#                         bits = bits * 2
#                         maxLongitude = mid
#                     isLongitude = False
#                 else:
#                     mid = (minLatitude + maxLatitude) / 2

#                     if latitude >= mid:
#                         bits = bits * 2 + 1
#                         minLatitude = mid
#                     else:
#                         bits = bits * 2
#                         maxLatitude = mid
#                     isLongitude = True
#                 bitlen -= 1

#             result += base32[bits]
#             accuracy -= 1

#         print(result)

#     except ValueError:
#         print("Wrong argument")
#         sys.exit(1)

# if __name__ == '__main__':
#     print("Usage: python3 geohashing.py <latitude> <longitude> <accuracy>")
#     sys.exit(1)

#     geoHash(sys.argv[1], sys.argv[2], sys.argv[3])

#!/usr/bin/python3

import sys
import antigravity


def main():
    if (len(sys.argv) == 4):
        try:
            latitude = float(sys.argv[1])
        except:
            return print("latitude required type: float")
        try:
            longitude = float(sys.argv[2])
        except:
            return print("longitude required type: float")
        try:
            datedow = sys.argv[3].encode('utf-8')
        except:
            return print("datedow required type: string")
        antigravity.geohash(latitude, longitude, datedow)
    else:
        print("3 arguments required(latitude, longitude, datedow)")


if __name__ == '__main__':
    main()