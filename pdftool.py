from pdfrw import PdfReader
import argparse
from math import isclose

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='filename of the PDF to process')
    args = parser.parse_args()

    reader = PdfReader(args.filename)
    for page_num, page in enumerate(reader.pages):
        l, t, r, b = [float(n) / 72 for n in page.MediaBox]
        width = r - l
        height = b - t
        if isclose(width, 8.5) and isclose(height, 11):
            print(f'Page {page_num+1:>3}   valid: Letter - Portrait')
        elif isclose(width, 11) and isclose(height, 8.5):
            print(f'Page {page_num+1:>3}   valid: Letter - Landscape')
        elif isclose(width, 17) and isclose(height, 11):
            print(f'Page {page_num+1:>3}   valid: 11x17 - Landscape')
        elif isclose(width, 11) and isclose(height, 17):
            print(f'Page {page_num+1:>3}   valid: 11x17 - Portrait')
        else:
            print(f'Page {page_num+1:>3} invalid: {width:2.5}x{height:2.5}')