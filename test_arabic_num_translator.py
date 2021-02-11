# testing arabic num translator

import arabic_num_translator


class TestArabicToRomanTranslator:
    def test_8(self):
        assert "VIII" == arabic_num_translator.arabic_to_roman(8)

    def test_2021(self):
        assert "MMXXI" == arabic_num_translator.arabic_to_roman(2021)

    def test_1993(self):
        assert "MCMIXIII" == arabic_num_translator.arabic_to_roman(1993)
