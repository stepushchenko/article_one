from playwright.sync_api import Page
import config


class IndexPage:
    _BUTTON_GOOGLE_SEARCH = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']"
    _LINK_ENGLISH_LANG = "//a[contains(text(), 'English')]"

    def open_index_page(self, page: Page) -> None:  # noqa
        page.goto(config.url.DOMAIN)

    def press_link_english_lang(self, page: Page):
        page.locator(self._LINK_ENGLISH_LANG).click()

    def get_text_from_google_search_button(self, page: Page) -> None:
        return page.locator(self._BUTTON_GOOGLE_SEARCH).get_attribute('value')
