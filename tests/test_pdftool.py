from pdftool import invalid_size
from pdfrw import PdfReader

class TestInvalidSize:
    def test_incorrectly_sized_page_from_job_book_11x17(self):
        reader = PdfReader('fixtures\\job_book_11x17_wrong_size.pdf')
        assert invalid_size(reader.pages[0])

    def test_incorrectly_sized_page_from_job_book_letter(self):
        reader = PdfReader('fixtures\\job_book_letter_wrong_size.pdf')
        assert invalid_size(reader.pages[0])

    def test_incorrectly_sized_report(self):
        reader = PdfReader('fixtures\\report_wrong_size.pdf')
        for page in reader.pages:
            assert invalid_size(page)

    def test_correctly_sized_report(self):
        reader = PdfReader('fixtures\\report_correct_size.pdf')
        for page in reader.pages:
            assert not invalid_size(page)

    def test_incorrectly_sized_field_photo(self):
        reader = PdfReader('fixtures\\field_photo_original_size.pdf')
        assert invalid_size(reader.pages[0])

    def test_correctly_sized_field_photo(self):
        reader = PdfReader('fixtures\\field_photo_resized.pdf')
        assert not invalid_size(reader.pages[0])