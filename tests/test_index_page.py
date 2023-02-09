import pytest
import pages


class TestFooter:

    def test_main_search_button_must_have_the_text_google_search(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.press_link_english_lang(page)
        actual_result = pages.index_page.get_text_from_google_search_button(page)
        assert actual_result == 'Google Search', 'Google Search button text is not correct'
