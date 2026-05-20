# import sys

# def geoHash(latitude, longitude, accuracy):
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
#     if len(sys.argv) != 4:
#         print("Usage: python3 geohashing.py <latitude> <longitude> <accuracy>")
#         sys.exit(1)
#     geoHash(sys.argv[1], sys.argv[2], sys.argv[3])

import sys
from datetime import datetime
from antigravity import geohash


def validate_coordinate(value, name, minimum, maximum):
    try:
        value = float(value)
    except ValueError:
        print(f"{name} must be a float")
        return None

    if not minimum <= value <= maximum:
        print(f"{name} must be between {minimum} and {maximum}")
        return None

    return value


def validate_datedow(value):
    try:
        date_part, dow_part = value.rsplit("-", 1)

        datetime.strptime(date_part, "%Y-%m-%d")
        float(dow_part)

    except ValueError:
        print("datedow format must be YYYY-MM-DD-dow")
        return None

    return value.encode("utf-8")


def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <latitude> <longitude> <datedow>")
        return

    latitude = validate_coordinate(sys.argv[1], "latitude", -90, 90)
    if latitude is None:
        return

    longitude = validate_coordinate(sys.argv[2], "longitude", -180, 180)
    if longitude is None:
        return

    datedow = validate_datedow(sys.argv[3])
    if datedow is None:
        return

    geohash(latitude, longitude, datedow)


if __name__ == "__main__":
    main()