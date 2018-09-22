from PIL import Image
from PIL.ExifTags import TAGS
import piexif
from datetime import *
import cv2

def convert(fname, offset, sign): 
    # filename and date format

    # datetime is stored like 2017:12:15 17:57:26 hence the format string is like
    fformat = "%Y:%m:%d %H:%M:%S"

    #image object with given filename
    img = Image.open(fname)
    print("Editing:", img)
    # exif information as a dict of dicts. each value is of datatype byte
    info = piexif.load(img.info['exif'])

    # convert the date taken byte into string using decode function. 36867 is
    # the tag for date taken
    dt = info['Exif'][36867].decode()

    # convert date string into datetime object.
    dtobj = datetime.strptime(dt, fformat)

    #add given offset
    if(sign == '-'):
        offset = (i * -1 for i in offset)
    h, m, s = offset
    dtobj += timedelta(hours = h, minutes = m, seconds = s)

    #convert back into string using the same format
    dt = dtobj.strftime(fformat)

    # set the datetime of photo as encoded byte using encode()
    info['Exif'][36867] = dt.encode()

    # final touch. save file with given exif information.
    exif_data = piexif.dump(info)
    img.save("%s" % fname, exif = exif_data)
