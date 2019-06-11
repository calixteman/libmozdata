# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import unittest

from libmozdata.wiki_parser import WikiParser

TABLE_1 = [
    [
        "Quarter",
        "Soft Freeze",
        "Merge Date",
        "Central",
        "Beta",
        "Release Date",
        "Release",
        "ESR",
    ],
    [
        "Q1",
        "2019-03-11",
        "2019-03-18",
        "Firefox 68",
        "Firefox 67",
        "2019-03-19",
        "Firefox 66",
        "Firefox 60.6",
    ],
    [
        "Q2",
        "2019-05-06",
        "2019-05-13",
        "Firefox 69",
        "Firefox 68",
        "2019-05-14",
        "Firefox 67",
        "Firefox 60.7",
    ],
    [
        "Q3",
        "2019-07-01",
        "2019-07-08",
        "Firefox 70",
        "Firefox 69",
        "2019-07-09",
        "Firefox 68",
        "Firefox 60.8; 68.0",
    ],
    [
        "Q3",
        "2019-08-26",
        "2019-09-02",
        "Firefox 71",
        "Firefox 70",
        "2019-09-03",
        "Firefox 69",
        "Firefox 60.9; 68.1",
    ],
    [
        "Q4",
        "2019-10-14",
        "2019-10-21",
        "Firefox 72",
        "Firefox 71",
        "2019-10-22",
        "Firefox 70",
        "Firefox 68.2",
    ],
    [
        "Q4",
        "2019-12-02",
        "2019-12-09",
        "Firefox 73",
        "Firefox 72",
        "2019-12-10",
        "Firefox 71",
        "Firefox 68.3",
    ],
]

TABLE_2 = [
    ["Soft Freeze", "Merge Date", "Central", "Beta", "Release Date", "Release", "ESR"],
    [
        "2019-01-21",
        "2019-01-28",
        "Firefox 67",
        "Firefox 66",
        "2019-01-29",
        "Firefox 65",
        "Firefox 60.5",
    ],
    [
        "2018-12-03",
        "2018-12-10",
        "Firefox 66",
        "Firefox 65",
        "2018-12-11",
        "Firefox 64",
        "Firefox 60.4",
    ],
    [
        "2018-10-15",
        "2018-10-22",
        "Firefox 65",
        "Firefox 64",
        "2018-10-23",
        "Firefox 63",
        "Firefox 60.3",
    ],
]

TABLE_3 = [
    ["Merge Date", "Central", "Beta", "Release Date", "Release", "ESR"],
    [
        "2018-09-04",
        "Firefox 64",
        "Firefox 63",
        "2018-09-05",
        "Firefox 62",
        "Firefox 60.2",
    ],
    [
        "2018-06-25",
        "Firefox 63",
        "Firefox 62",
        "2018-06-26",
        "Firefox 61",
        "Firefox 52.9; 60.1",
    ],
    [
        "2018-05-07",
        "Firefox 62",
        "Firefox 61",
        "2018-05-09",
        "Firefox 60",
        "Firefox 52.8; 60.0",
    ],
    [
        "2018-03-12",
        "Firefox 61",
        "Firefox 60",
        "2018-03-13",
        "Firefox 59",
        "Firefox 52.7",
    ],
    [
        "2018-01-22",
        "Firefox 60",
        "Firefox 59",
        "2018-01-23",
        "Firefox 58",
        "Firefox 52.6",
    ],
    [
        "2017-11-13",
        "Firefox 59",
        "Firefox 58",
        "2017-11-14",
        "Firefox 57",
        "Firefox 52.5",
    ],
    [
        "2017-09-21",
        "Firefox 58",
        "Firefox 57",
        "2017-09-28",
        "Firefox 56",
        "Firefox 52.4",
    ],
    [
        "2017-08-02",
        "Firefox 57",
        "Firefox 56",
        "2017-08-08",
        "Firefox 55",
        "Firefox 52.3",
    ],
    [
        "2017-06-12",
        "Firefox 56",
        "Firefox 55",
        "2017-06-13",
        "Firefox 54",
        "Firefox 52.2",
    ],
    [
        "2017-04-18",
        "Firefox 55",
        "Firefox 54",
        "2017-04-19",
        "Firefox 53",
        "Firefox 45.9; 52.1",
    ],
]

TABLE_4 = [
    ["Merge Date", "Central", "Aurora", "Beta", "Release Date", "Release", "ESR"],
    [
        "2017-03-06",
        "Firefox 55",
        "Firefox 54",
        "Firefox 53",
        "2017-03-07",
        "Firefox 52",
        "Firefox 45.8; 52.0",
    ],
    [
        "2017-01-23",
        "Firefox 54",
        "Firefox 53",
        "Firefox 52",
        "2017-01-24",
        "Firefox 51",
        "Firefox 45.7",
    ],
    ["", "", "", "", "2016-12-13", "Firefox 50.1.0", "Firefox 45.6"],
    [
        "2016-11-14",
        "Firefox 53",
        "Firefox 52",
        "Firefox 51",
        "2016-11-15",
        "Firefox 50",
        "Firefox 45.5",
    ],
    [
        "2016-09-19",
        "Firefox 52",
        "Firefox 51",
        "Firefox 50",
        "2016-09-20",
        "Firefox 49",
        "Firefox 45.4",
    ],
    [
        "2016-08-01",
        "Firefox 51",
        "Firefox 50",
        "Firefox 49",
        "2016-08-02",
        "Firefox 48",
        "Firefox 45.3",
    ],
    [
        "2016-06-06",
        "Firefox 50",
        "Firefox 49",
        "Firefox 48",
        "2016-06-07",
        "Firefox 47",
        "Firefox 45.2",
    ],
    [
        "2016-04-25",
        "Firefox 49",
        "Firefox 48",
        "Firefox 47",
        "2016-04-26",
        "Firefox 46",
        "Firefox 38.8; 45.1",
    ],
    [
        "2016-03-07",
        "Firefox 48",
        "Firefox 47",
        "Firefox 46",
        "2016-03-08",
        "Firefox 45",
        "Firefox 38.7; 45.0",
    ],
    [
        "2016-01-25",
        "Firefox 47",
        "Firefox 46",
        "Firefox 45",
        "2016-01-26",
        "Firefox 44",
        "Firefox 38.6",
    ],
    [
        "2015-12-14",
        "Firefox 46",
        "Firefox 45",
        "Firefox 44",
        "2015-12-15",
        "Firefox 43",
        "Firefox 38.5",
    ],
    [
        "2015-10-29",
        "Firefox 45",
        "Firefox 44",
        "Firefox 43",
        "2015-11-03",
        "Firefox 42",
        "Firefox 38.4",
    ],
    [
        "2015-09-21",
        "Firefox 44",
        "Firefox 43",
        "Firefox 42",
        "2015-09-22",
        "Firefox 41",
        "Firefox 38.3",
    ],
    [
        "2015-08-10",
        "Firefox 43",
        "Firefox 42",
        "Firefox 41",
        "2015-08-11",
        "Firefox 40",
        "Firefox 38.2",
    ],
    [
        "2015-06-29",
        "Firefox 42",
        "Firefox 41",
        "Firefox 40",
        "2015-06-30",
        "Firefox 39",
        "Firefox 31.8; 38.1",
    ],
    ["", "", "", "", "2015-06-02", "Firefox 38.0.5", ""],
    [
        "2015-05-11*",
        "Firefox 41",
        "Firefox 40",
        "Firefox 39",
        "2015-05-12*",
        "Firefox 38",
        "Firefox 31.7; 38.0",
    ],
    [
        "2015-03-30*",
        "Firefox 40",
        "Firefox 39",
        "Firefox 38",
        "2015-03-31*",
        "Firefox 37",
        "Firefox 31.6",
    ],
    [
        "2015-02-23",
        "Firefox 39",
        "Firefox 38",
        "Firefox 37",
        "2015-02-24",
        "Firefox 36",
        "Firefox 31.5",
    ],
    [
        "2015-01-12*",
        "Firefox 38",
        "Firefox 37",
        "Firefox 36",
        "2015-01-13*",
        "Firefox 35",
        "Firefox 31.4",
    ],
    [
        "2014-11-28*",
        "Firefox 37",
        "Firefox 36",
        "Firefox 35",
        "2014-12-01*",
        "Firefox 34",
        "Firefox 31.3",
    ],
    [
        "2014-10-13",
        "Firefox 36",
        "Firefox 35",
        "Firefox 34",
        "2014-10-14",
        "Firefox 33",
        "Firefox 31.2",
    ],
    [
        "2014-09-02*",
        "Firefox 35",
        "Firefox 34",
        "Firefox 33",
        "2014-09-02",
        "Firefox 32",
        "Firefox 24.8; 31.1",
    ],
    [
        "2014-07-21",
        "Firefox 34",
        "Firefox 33",
        "Firefox 32",
        "2014-07-22",
        "Firefox 31",
        "Firefox 24.7; 31.0",
    ],
    [
        "2014-06-09",
        "Firefox 33",
        "Firefox 32",
        "Firefox 31",
        "2014-06-10",
        "Firefox 30",
        "Firefox 24.6",
    ],
    [
        "2014-04-28",
        "Firefox 32",
        "Firefox 31",
        "Firefox 30",
        "2014-04-29",
        "Firefox 29",
        "Firefox 24.5",
    ],
    [
        "2014-03-17",
        "Firefox 31",
        "Firefox 30",
        "Firefox 29",
        "2014-03-18",
        "Firefox 28",
        "Firefox 24.4",
    ],
    [
        "2014-02-03*",
        "Firefox 30",
        "Firefox 29",
        "Firefox 28",
        "2014-02-04*",
        "Firefox 27",
        "Firefox 24.3",
    ],
    [
        "2013-12-09",
        "Firefox 29",
        "Firefox 28",
        "Firefox 27",
        "2013-12-10",
        "Firefox 26",
        "Firefox 24.2",
    ],
    [
        "2013-10-28",
        "Firefox 28",
        "Firefox 27",
        "Firefox 26",
        "2013-10-29",
        "Firefox 25",
        "Firefox 17.0.10; 24.1",
    ],
    [
        "2013-09-16",
        "Firefox 27",
        "Firefox 26",
        "Firefox 25",
        "2013-09-17",
        "Firefox 24",
        "Firefox 17.0.9; 24.0",
    ],
    [
        "2013-08-05",
        "Firefox 26",
        "Firefox 25",
        "Firefox 24",
        "2013-08-06",
        "Firefox 23",
        "Firefox 17.0.8",
    ],
    [
        "2013-06-24",
        "Firefox 25",
        "Firefox 24",
        "Firefox 23",
        "2013-06-25",
        "Firefox 22",
        "Firefox 17.0.7",
    ],
    [
        "2013-05-13",
        "Firefox 24",
        "Firefox 23",
        "Firefox 22",
        "2013-05-14",
        "Firefox 21",
        "Firefox 17.0.6",
    ],
    [
        "2013-04-01",
        "Firefox 23",
        "Firefox 22",
        "Firefox 21",
        "2013-04-02",
        "Firefox 20",
        "Firefox 17.0.5",
    ],
    [
        "2013-02-19*",
        "Firefox 22",
        "Firefox 21",
        "Firefox 20",
        "2013-02-19",
        "Firefox 19",
        "Firefox 17.0.3",
    ],
    [
        "2013-01-07*",
        "Firefox 21",
        "Firefox 20",
        "Firefox 19",
        "2013-01-08*",
        "Firefox 18",
        "Firefox 10.0.12; 17.0.2",
    ],
    [
        "2012-11-19",
        "Firefox 20",
        "Firefox 19",
        "Firefox 18",
        "2012-11-20",
        "Firefox 17",
        "Firefox 10.0.11; 17.0",
    ],
    [
        "2012-10-08",
        "Firefox 19",
        "Firefox 18",
        "Firefox 17",
        "2012-10-09",
        "Firefox 16",
        "Firefox 10.0.8",
    ],
    [
        "2012-08-27",
        "Firefox 18",
        "Firefox 17",
        "Firefox 16",
        "2012-08-28",
        "Firefox 15",
        "Firefox 10.0.7",
    ],
    [
        "2012-07-16",
        "Firefox 17",
        "Firefox 16",
        "Firefox 15",
        "2012-07-17",
        "Firefox 14",
        "Firefox 10.0.6",
    ],
    [
        "2012-06-05",
        "Firefox 16",
        "Firefox 15",
        "Firefox 14",
        "2012-06-05",
        "Firefox 13",
        "Firefox 10.0.5",
    ],
    [
        "2012-04-24",
        "Firefox 15",
        "Firefox 14",
        "Firefox 13",
        "2012-04-24",
        "Firefox 12",
        "Firefox 10.0.4",
    ],
    [
        "2012-03-13",
        "Firefox 14",
        "Firefox 13",
        "Firefox 12",
        "2012-03-13",
        "Firefox 11",
        "Firefox 10.0.3",
    ],
    [
        "2012-01-31",
        "Firefox 13",
        "Firefox 12",
        "Firefox 11",
        "2012-01-31",
        "Firefox 10",
        "Firefox 10.0",
    ],
    [
        "2011-12-20",
        "Firefox 12",
        "Firefox 11",
        "Firefox 10",
        "2011-12-20",
        "Firefox 9",
        "",
    ],
    [
        "2011-11-08",
        "Firefox 11",
        "Firefox 10",
        "Firefox 9",
        "2011-11-08",
        "Firefox 8",
        "",
    ],
    [
        "2011-09-27",
        "Firefox 10",
        "Firefox 9",
        "Firefox 8",
        "2011-09-27",
        "Firefox 7",
        "",
    ],
    [
        "2011-08-16",
        "Firefox 9",
        "Firefox 8",
        "Firefox 7",
        "2011-08-16",
        "Firefox 6",
        "",
    ],
    ["2011-07-05", "Firefox 8", "Firefox 7", "Firefox 6", "", "", ""],
    ["", "", "", "", "2011-06-21", "Firefox 5", ""],
    ["2011-05-24", "Firefox 7", "Firefox 6", "", "", "", ""],
    ["2011-05-17", "", "", "Firefox 5", "", "", ""],
    ["2011-04-12", "Firefox 6", "Firefox 5", "", "", "", ""],
]


class WikiParserTest(unittest.TestCase):
    def test_parser(self):
        with open("tests/html/Calendar.html", "r") as In:
            html = In.read()
        parser = WikiParser(tables=list(range(0, 20)))
        try:
            parser.feed(html)
        except StopIteration:
            tables = parser.get_tables()

        self.assertEqual(len(tables), 4)

        self.assertEqual(tables[0], TABLE_1)
        self.assertEqual(tables[1], TABLE_2)
        self.assertEqual(tables[2], TABLE_3)
        self.assertEqual(tables[3], TABLE_4)


if __name__ == "__main__":
    unittest.main()
