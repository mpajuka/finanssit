import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(700)
        
    def test_kassapaatteen_rahojen_ja_lounaiden_maara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_kateisosto_edullinen_riittava_kateinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(700), 460) 
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(self.kassapaate.edulliset, 1) 
        
    def test_kateisosto_edullinen_vajaa_kateinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 0) 
        
    def test_kateisosto_maukas_riittava_kateinen(self): 
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(700), 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)
        self.assertEqual(self.kassapaate.maukkaat, 1)
         
    def test_kateisosto_maukas_vajaa_kateinen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_korttiosto_maukas_riittava_saldo(self): 
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(self.kortti.saldo_euroina(), 3)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_korttiosto_maukas_vajaa_saldo(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), False)
        self.assertEqual(self.kortti.saldo_euroina(), 3)
        self.assertEqual(self.kassapaate.maukkaat, 1)
     
    def test_korttiosto_edullinen_riittava_saldo(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(self.kortti.saldo_euroina(), 4.6)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_korttiosto_edullinen_vajaa_saldo(self): 
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), False)
        self.assertEqual(self.kortti.saldo_euroina(), 2.2)
        self.assertEqual(self.kassapaate.edulliset, 2)
        
    def test_positiivisen_summan_lataaminen_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005)
        self.assertEqual(self.kortti.saldo_euroina(), 12)
        
    def test_negatiivisen_summan_lataaminen_kortille(self): 
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kortti.saldo_euroina(), 7)