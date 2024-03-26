import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_kortin_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)
    
    def test_kortin_saldo_oikein_teksti(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_lataa_rahaa_palauttaa_oikean_saldon(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 15)
        
    def test_ota_rahaa_palauttaa_oikean_saldon(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5)
        
    def test_ota_rahaa_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)
        
    def test_saldon_riittaminen_palauttaa_oikean_arvon(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)