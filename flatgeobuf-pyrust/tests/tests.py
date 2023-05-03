import unittest
from json import dump, dumps
from os import path

from flatgeobuf_pyrust import from_fgb, to_fgb


class TestFlatGeoBuf(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path_to_file = path.relpath("./data/countries.fgb")
        with open(path_to_file, "rb") as fh:
            cls.fgb_contents = fh.read()

        cls.data = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {},
                    "geometry": {
                        "coordinates": [
                            [
                                [28.996966545463096, 41.04243561228222],
                                [28.996950186172654, 41.04243561228222],
                                [28.996950186172654, 41.04231337858042],
                                [28.996966545463096, 41.04231337858042],
                                [28.996966545463096, 41.04243561228222],
                            ]
                        ],
                        "type": "Polygon",
                    },
                },
                {
                    "type": "Feature",
                    "properties": {},
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [28.99903292438503, 41.04339873944504],
                                [28.998976383057393, 41.04339664445732],
                                [28.998920386264366, 41.04339037967041],
                                [28.998865473295968, 41.04338000541885],
                                [28.99881217300361, 41.04336562161425],
                                [28.99876099870656, 41.04334736678307],
                                [28.998712443248092, 41.043325416732465],
                                [28.998666974248906, 41.043299982857],
                                [28.99862502960344, 41.043271310102696],
                                [28.9985870132626, 41.04323967460787],
                                [28.99855329134349, 41.04320538104367],
                                [28.998524188603497, 41.04316875967978],
                                [28.99849998531284, 41.043130163203514],
                                [28.99848091455561, 41.04308996332316],
                                [28.998467159985307, 41.04304854718816],
                                [28.998458854056462, 41.0430063136604],
                                [28.99845607674941, 41.04296366947304],
                                [28.998458854800425, 41.04292102531331],
                                [28.998467161444644, 41.042878791867395],
                                [28.998480916674247, 41.04283737586527],
                                [28.99849998800935, 41.04279717616377],
                                [28.99852419177425, 41.04275857990543],
                                [28.998553294866646, 41.04272195879015],
                                [28.998587017002762, 41.042687665495734],
                                [28.99862503341687, 41.042656030281464],
                                [28.998666977989075, 41.04262735780771],
                                [28.998712446771258, 41.04260192420203],
                                [28.99876100187732, 41.04257997440004],
                                [28.99881217570012, 41.04256171978679],
                                [28.998865475414608, 41.04254733616102],
                                [28.998920387723704, 41.042536962042355],
                                [28.998976383801363, 41.04253069733729],
                                [28.99903292438503, 41.0425286023772],
                                [28.999089464968698, 41.04253069733729],
                                [28.999145461046353, 41.042536962042355],
                                [28.999200373355453, 41.04254733616102],
                                [28.999253673069944, 41.04256171978679],
                                [28.999304846892745, 41.04257997440004],
                                [28.999353401998807, 41.04260192420203],
                                [28.99939887078099, 41.04262735780771],
                                [28.999440815353193, 41.042656030281464],
                                [28.9994788317673, 41.042687665495734],
                                [28.999512553903415, 41.04272195879015],
                                [28.999541656995806, 41.04275857990543],
                                [28.999565860760715, 41.04279717616377],
                                [28.999584932095818, 41.04283737586527],
                                [28.999598687325413, 41.042878791867395],
                                [28.99960699396964, 41.04292102531331],
                                [28.99960977202065, 41.04296366947304],
                                [28.999606994713602, 41.0430063136604],
                                [28.999598688784754, 41.04304854718816],
                                [28.999584934214454, 41.04308996332316],
                                [28.99956586345722, 41.043130163203514],
                                [28.999541660166567, 41.04316875967978],
                                [28.99951255742657, 41.04320538104367],
                                [28.99947883550746, 41.04323967460787],
                                [28.999440819166622, 41.043271310102696],
                                [28.999398874521155, 41.043299982857],
                                [28.99935340552197, 41.043325416732465],
                                [28.999304850063503, 41.04334736678307],
                                [28.999253675766447, 41.04336562161425],
                                [28.999200375474093, 41.04338000541885],
                                [28.999145462505695, 41.04339037967041],
                                [28.99908946571267, 41.04339664445732],
                                [28.99903292438503, 41.04339873944504],
                            ]
                        ],
                    },
                },
            ],
        }

    def test_decoded(self):
        json_str = from_fgb(self.fgb_contents)
        self.assertEqual(type(json_str), list)
        self.assertEqual(len(json_str), 179)

        with open("decoded.json", "w") as fh:
            dump(json_str, fh, indent=2)

    def test_encoded(self):
        data_bytes = bytes(dumps(self.data), encoding="utf-8")
        encoded = to_fgb(data_bytes, "polygon")
        self.assertTrue(encoded)
