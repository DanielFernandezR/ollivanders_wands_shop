from logic import update_days


def test_dia_1():
    assert update_days(1) == ["+5 Dexterity Vest", 9, 19,
                         "Elixir of the Mongoose", 4, 6,
                         "Aged Brie", 1, 1,
                         "Sulfuras, Hand of Ragnaros", 0, 80,
                         "Sulfuras, Hand of Ragnaros", -1, 80,
                         "Backstage passes to a TAFKAL80ETC concert", 14, 21,
                         "Backstage passes to a TAFKAL80ETC concert", 9, 50,
                         "Backstage passes to a TAFKAL80ETC concert", 4, 50,
                         "Conjured Mana Cake", 2, 4]
