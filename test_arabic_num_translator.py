# testing arabic num translator

import arabic_num_translator


class TestArabicToRomanTranslator:
    def test_8(self):
        assert "VIII" == arabic_num_translator.arabic_to_roman(8)
