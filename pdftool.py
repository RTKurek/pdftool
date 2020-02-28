from pdfrw import PdfReader
import argparse

def isclose(a, b, tol=0.0001):
    return abs(a - b) < tol

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
            print('Page {:>3}   valid: Letter - Portrait'.format(page_num+1))
        elif isclose(width, 11) and isclose(height, 8.5):
            print('Page {:>3}   valid: Letter - Landscape'.format(page_num+1))
        elif isclose(width, 17) and isclose(height, 11):
            print('Page {:>3}   valid: 11x17 - Landscape'.format(page_num+1))
        elif isclose(width, 11) and isclose(height, 17):
            print('Page {:>3}   valid: 11x17 - Portrait'.format(page_num+1))
        else:
            print('Page {:>3} invalid: {:2.5}x{:2.5}'.format(page_num+1,
                                                             width, height))

