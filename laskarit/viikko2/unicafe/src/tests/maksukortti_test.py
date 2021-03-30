import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(1)
        self.assertEqual(str(self.maksukortti), "saldo: 0.11")
    
    def test_vahentaa_oikein(self):
        self.maksukortti.ota_rahaa(1)
        self.assertEqual(str(self.maksukortti), "saldo: 0.09")
    
    def test_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(20)
        if self.assertEqual(str(self.maksukortti), "saldo: 0.1"):
            return True
        else:
            return False
    

