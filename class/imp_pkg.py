
def imp_func():
    print("Very confidential data")
    print("This is a function inside pkg_sample")

def vimp_func():
    print("This contains very important data")

PI_VALUE = 3.141527


if __name__ == "__main__":
    imp_func()
    print(__name__)
