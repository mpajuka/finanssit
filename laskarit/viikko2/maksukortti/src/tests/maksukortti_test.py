import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)
        
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()
        
        self.assertEqual(self.kortti.saldo_euroina(), 7.5)
        
    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()
        
        self.assertEqual(self.kortti.saldo_euroina(), 6.0)
        
    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti = Maksukortti(200)
        self.kortti.syo_edullisesti()

        self.assertEqual(self.kortti.saldo_euroina(), 2.0)
        
    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti = Maksukortti(200)
        self.kortti.syo_maukkaasti()
        
        self.assertEqual(self.kortti.saldo_euroina(), 2.0)
        
    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)

        self.assertEqual(self.kortti.saldo_euroina(), 35.0)

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)

        self.assertEqual(self.kortti.saldo_euroina(), 150.0)
        
    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kortti.lataa_rahaa(-200)
        
        self.assertEqual(self.kortti.saldo_euroina(), 10.0)
        
    def test_syo_edullisesti_kun_saldo_ruoan_hinnan_verran(self):
        self.kortti = Maksukortti(250)
        self.kortti.syo_edullisesti()
         
        self.assertEqual(self.kortti.saldo_euroina(), 0.0)
        
    def test_syo_maukkaasti_kun_saldo_ruoan_hinnan_verran(self):
        self.kortti = Maksukortti(400)
        self.kortti.syo_maukkaasti()
         
        self.assertEqual(self.kortti.saldo_euroina(), 0.0)