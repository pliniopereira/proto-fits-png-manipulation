import pyfits


def set_headers(file_name):
    file_name = str(file_name)
    try:
        image = pyfits.open(file_name)
        prihdr = image[0].header
        prihdr['DPI'] = '000'  # ???
        prihdr['BINNING'] = '000'
        prihdr['BIT-DEP'] = '000'  # ???
        prihdr['CCD-GAIN'] = '000'  # ???
        prihdr['CCD-TEMP'] = '000'
        prihdr['CCDSTEMP'] = '000'
        prihdr['CCDTYPE'] = '000'
        prihdr['IMAGETYP'] = '000'
        prihdr['EXPOSURE'] = '000'
        prihdr['FLT-NAME'] = '000'
        prihdr['FLT-POS'] = '000'
        prihdr['FLT-WAVE'] = '000'
        prihdr['FW-TEMP'] = '000'
        prihdr['FILE-NAM'] = '000'
        prihdr['LATITUDE'] = '000'
        prihdr['LONGITUD'] = '000'
        prihdr['MO-ELEV'] = '000'
        prihdr['MO-PHASE'] = '000'
        prihdr['R-SPEED'] = '000'  # ???
        prihdr['SHTRCCD'] = '000'
        prihdr['SHTRLENZ'] = '000'
        prihdr['SITE-ID'] = '000'
        prihdr['START-T'] = '000'
        prihdr['SUN-ELEV'] = '000'
        prihdr['VERSION'] = '000'
        for keys, values in prihdr.items():
            print(str(keys) + ": " + str(values))
        print("\n\n")
    except Exception as e:
        print(e)
