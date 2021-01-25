# testing roman num translator

import roman_num_translator


class TestRomanToArabicTranslator:
    def test_16(self):
        assert 16 == roman_num_translator.roman_to_arabic("XVI")

    def test_2019(self):
        assert 2019 == roman_num_translator.roman_to_arabic("MMXIX")
