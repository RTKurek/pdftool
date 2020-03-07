import os

import pdftool
from pdfrw import PdfReader


class TestInvalidSize:
    def test_incorrectly_sized_page_from_job_book_11x17(self):
        reader = PdfReader(os.path.join('fixtures', 'job_book_11x17_wrong_size.pdf'))
        assert pdftool.invalid_size(reader.pages[0])

    def test_incorrectly_sized_page_from_job_book_letter(self):
        reader = PdfReader(os.path.join('fixtures', 'job_book_letter_wrong_size.pdf'))
        assert pdftool.invalid_size(reader.pages[0])

    def test_incorrectly_sized_report(self):
        reader = PdfReader(os.path.join('fixtures', 'report_wrong_size.pdf'))
        for page in reader.pages:
            assert pdftool.invalid_size(page)

    def test_correctly_sized_report(self):
        reader = PdfReader(os.path.join('fixtures', 'report_correct_size.pdf'))
        for page in reader.pages:
            assert not pdftool.invalid_size(page)

    def test_incorrectly_sized_field_photo(self):
        reader = PdfReader(os.path.join('fixtures', 'field_photo_original_size.pdf'))
        assert pdftool.invalid_size(reader.pages[0])

    def test_correctly_sized_field_photo(self):
        reader = PdfReader(os.path.join('fixtures', 'field_photo_resized.pdf'))
        assert not pdftool.invalid_size(reader.pages[0])


class TestResizePages:
    def test_correctly_sized_report_is_unchanged(self, tmpdir):
        reader = PdfReader(os.path.join('fixtures', 'report_correct_size.pdf'))
        writer = pdftool.resize_pages(reader)

        path = tmpdir.join('test.pdf').strpath
        writer.write(path)

        reader = PdfReader(path)
        for page in reader.pages:
            assert not pdftool.invalid_size(page)


    def test_incorrectly_sized_report_is_fixed(self, tmpdir):
        reader = PdfReader(os.path.join('fixtures', 'report_wrong_size.pdf'))
        writer = pdftool.resize_pages(reader)

        path = tmpdir.join('test.pdf').strpath
        writer.write(path)

        reader = PdfReader(path)
        for page in reader.pages:
            assert not pdftool.invalid_size(page)