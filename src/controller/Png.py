from PIL import Image


def return_info(file_name):
    file_name = str(file_name)
    try:
        image = Image.open(file_name)
        dictionary = image.info
        for keys, values in dictionary.items():
            print(str(keys) + ": " + str(values))
        image.show
    except Exception as e:
        print(e)
