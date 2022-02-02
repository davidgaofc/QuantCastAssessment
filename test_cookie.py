import unittest

from most_active_cookie import loadFile, processData

manual_data = [['AtY0laUfhglK3lC7','2018-12-09','14:19:00+00:00'],
            ['SAZuXPGUrfbcn5UA','2018-12-09', '10:13:00+00:00'],
            ['5UAVanZf6UtGyKVS','2018-12-09', '07:25:00+00:00'],
            ['AtY0laUfhglK3lC7','2018-12-09', '06:19:00+00:00'],
            ['SAZuXPGUrfbcn5UA','2018-12-08','22:03:00+00:00'],
            ['4sMM2LxV07bPJzwf','2018-12-08','21:30:00+00:00'],
            ['fbcn5UAVanZf6UtG','2018-12-08', '09:30:00+00:00'],
            ['4sMM2LxV07bPJzwf','2018-12-07','23:30:00+00:00']]
manual_dict = {'AtY0laUfhglK3lC7': 2, 'SAZuXPGUrfbcn5UA': 1, '5UAVanZf6UtGyKVS': 1}

class MyTestCase(unittest.TestCase):

    def test_load(self):
        self.assertEqual(loadFile('test.csv'),manual_data)
        self.assertEqual(loadFile('test2.csv'),[])
    def test_process(self):
        self.assertEqual(processData('2018-12-09',manual_data), manual_dict)
        self.assertEqual(processData('2018-12-09',[]),{})


if __name__ == '__main__':
    unittest.main()
