from pdfrw import PdfReader, PdfWriter
import argparse


def isclose(a, b, tol=0.0001):
    return abs(a - b) < tol


def invalid_size(page):
    l, t, r, b = [float(n) / 72 for n in page.MediaBox]
    width = r - l
    height = b - t
    return not ((isclose(width, 8.5) and isclose(height, 11)) or
                (isclose(width, 11) and isclose(height, 8.5)) or
                (isclose(width, 17) and isclose(height, 11)) or
                (isclose(width, 11) and isclose(height, 17)))


def resize_pages(reader):
    writer = PdfWriter()
    for page in reader.pages:
        writer.addpage(page)
    return writer


def formatted_range(nums):
    seqStart = 0
    seqEnd = 0
    strs = []

    while seqStart < len(nums):
        while seqEnd < len(nums) - 1 and nums[seqEnd + 1] == nums[seqEnd] + 1:
            seqEnd += 1

        if seqEnd == seqStart:
            strs.append(str(nums[seqStart]))
        elif seqEnd == seqStart + 1:
            strs.append('{}, {}'.format(nums[seqStart], nums[seqEnd]))
        else:
            strs.append('{}-{}'.format(nums[seqStart], nums[seqEnd]))

        seqEnd += 1
        seqStart = seqEnd

    return ', '.join(strs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='filename of the PDF to process')
    args = parser.parse_args()

    reader = PdfReader(args.filename)
    invalid_page_nums = [i + 1 for (i, page) in enumerate(reader.pages)
                         if invalid_size(page)]
    if len(invalid_page_nums) == 0:
        print('Success! All pages are a valid size.')
    else:
        print('Failure! The following pages are a non-standard size:')
        print(formatted_range(invalid_page_nums))

