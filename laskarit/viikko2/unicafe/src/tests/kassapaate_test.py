import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_raha_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lounaat_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kateisella_rahat(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_syo_edullisesti_kateisella_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_kateisella_rahat_takaisin(self):
        rahat = str(self.kassapaate.syo_edullisesti_kateisella(500))
        self.assertEqual(rahat, '260')
    
    def test_syo_maukkaasti_kateisella_rahat(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_syo_maukkaasti_kateisella_rahat_takaisin(self):
        rahat = str(self.kassapaate.syo_maukkaasti_kateisella(500))
        self.assertEqual(rahat, '100')
  
    
    def test_syo_maukkaasti_kateisella_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat,1)
    
    def test_veloitetaan_kortilta_oikein_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        if self.assertEqual(str(self.maksukortti), "saldo: 7.6"):
            return True
    
    def test_kortilta_edullinen_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_veloitetaan_kortilta_oikein_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        if self.assertEqual(str(self.maksukortti), "saldo: 6.0"):
            return True
    
    def test_kortilta_maukas_maara(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kortilla_ei_tarpeeksi_rahaa_edulliseen(self):
        self.maksukortti.ota_rahaa(900)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        if self.assertEqual(str(self.maksukortti), "saldo: 1.0"):
            return False
    
    def test_kortilla_ei_tarpeeksi_rahaa_maukkaaseen(self):
        self.maksukortti.ota_rahaa(900)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        if self.assertEqual(str(self.maksukortti), "saldo: 1.0"):
            return False
    
    def test_rahamaara_ei_muutu_kun_ostetaan_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(str(self.maksukortti), "saldo: 11.0")