import math


def latlon_to_web_mercator(lat, lon):
    r_major = 6378137.0  # Raggio equatoriale della Terra in metri
    x = lon * math.radians(r_major)
    scale = math.tan(math.pi / 4 + math.radians(lat) / 2)
    y = r_major * math.log(scale)
    return x, y


def CoordToPx(lat, lon, img_width, img_height, min_lat, max_lat, min_lon, max_lon):
    x_min, y_min = latlon_to_web_mercator(min_lat, min_lon)
    x_max, y_max = latlon_to_web_mercator(max_lat, max_lon)
    x0, y0 = latlon_to_web_mercator(lat, lon)

    w = x_max - x_min
    h = y_max - y_min

    rw = img_width / w
    rh = img_height / h

    if (rw > rh):
        x = (x0 - x_min) * rh
        y = img_height - (y0 - y_min) * rh
        x_offset = int((img_width - w * rh) / 2)
        y_offset = int((img_height - h * rh) / 2)
    else:
        x = (x0 - x_min) * rw
        y = img_height - (y0 - y_min) * rw
        x_offset = int((img_width - w * rw) / 2)
        y_offset = int((img_height - h * rw) / 2)

    return x + x_offset, y - y_offset


