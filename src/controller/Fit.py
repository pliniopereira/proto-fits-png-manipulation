import pyfits


def return_info(file_name):
    file_name = str(file_name)
    try:
        image = pyfits.open(file_name)
        prihdr = image[0].header
        for keys, values in prihdr.items():
            print(str(keys) + ": " + str(values))
        print("\n\n")
    except Exception as e:
        print(e)
