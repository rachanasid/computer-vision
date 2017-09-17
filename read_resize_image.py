import cv2
import sys


def read_image(img_name):
    return cv2.imread(img_name)


def display_image(img):
    cv2.imshow('image', img)
    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()


def add_scalar_to_image(img, value):
    b, g, r = cv2.split(img)
    b = cv2.add(b, value)
    g = cv2.add(g, value)
    r = cv2.add(r, value)
    res = cv2.merge((b, g, r))
    return res


def resize_image(img, value):
    return cv2.resize(img, None, fx=value, fy=value, interpolation=cv2.INTER_CUBIC)


if __name__ == "__main__":
    try:
        arg1 = sys.argv[1]
    except IndexError:
        print "Usage: read_resize_image.py <arg1>"
        sys.exit(1)

    img = read_image(arg1)
    # display_image(img)

    # add scalar 100 to image
    new_img = add_scalar_to_image(img, 100)
    # display_image(new_img)

    # resize image to 50%
    resized_img = resize_image(img, 0.5)
    # display_image(resized_img)
