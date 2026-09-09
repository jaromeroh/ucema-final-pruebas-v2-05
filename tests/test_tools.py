import unittest
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from tools import get_data

class ToolTests(unittest.TestCase):
    def test_aggregate_not_average_of_percentages(self):
        result=get_data(ROOT,'01')
        self.assertEqual(result['revenue_total'],2000)
        self.assertEqual(result['margin_total'],600)
        self.assertEqual(result['change_percent'],0)
    def test_loss_region(self):
        result=get_data(ROOT,'02')
        self.assertEqual(result['loss_regions'],['Norte'])
        self.assertEqual(result['change_percent'],-25)
    def test_zero_base_has_no_growth_percentage(self):
        self.assertIsNone(get_data(ROOT,'03')['change_percent'])

if __name__ == "__main__": unittest.main()
