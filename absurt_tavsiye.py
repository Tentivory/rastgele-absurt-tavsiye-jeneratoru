#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Absürt Tavsiye Jeneratörü
Dünyanın en ciddiye alınan saçma tavsiye makinesi.
Çalıştır: python3 absurt_tavsiye.py
"""

import random
import time

tavsiyeler = [
    "Her sabah aynaya bak ve kendine 'Bugün bir penguen olacağım' de. Penguenler soğukta bile mutludur.",
    "Çay içerken kaşığı ters tut. Böylece evren seninle alay ederken sen de onunla alay etmiş olursun.",
    "Telefonunu 37 dakika boyunca yüzüstü bırak. Bu, dijital detoksun en absürt hali.",
    "Her gece yastığın altına bir hesap makinesi koy. Rüyaların daha matematiksel olsun.",
    "Birileriyle konuşurken her cümlenin sonuna 'ama aslında kediler yönetiyor' ekle.",
    "Sol ayağınla sağ ayakkabını giy. Dengeyi bozmak özgürlüğün ilk adımıdır.",
    "Buzdolabının içinde 5 dakika otur. Soğuk düşünmek iyidir, derler.",
    "Her gün birine rastgele 'Bugün hava çok felsefi' de. Sonra kaç.",
    "Klavyene her saat başı 'Merhaba dünya, ben buradayım ama aslında değilim' yaz.",
    "Gökyüzüne bakıp 'Bulutlar aslında şifreli mesajlar' diye fısılda. Kimse duymasa da olur."
]

def tavsiye_ver():
    print("\n" + "="*50)
    print("ABSÜRT TAVSİYE MAKİNESİ ÇALIŞIYOR...")
    print("="*50)
    time.sleep(1.5)
    print("Evrenle bağlantı kuruluyor...")
    time.sleep(1)
    print("Saçmalık seviyesi hesaplanıyor: %99.9")
    time.sleep(0.8)
    secilen = random.choice(tavsiyeler)
    print("\n>>> BUGÜNÜN CİDDİ TAVSİYESİ:")
    print(f"   {secilen}")
    print("\nBu tavsiyeyi uygulamadan önce lütfen 3 kez düşün. Sonra yine de uygula.")
    print("="*50 + "\n")

if __name__ == "__main__":
    print("Hoş geldiniz. Bu program sizi kurtarmaz ama güldürür.")
    tavsiye_ver()
    print("İşte bu kadar. Daha fazlası için tekrar çalıştır. Sonsuza kadar.")

# Gizli not: Özgürlük, kaşığı ters tutmakta gizlidir. Kimse fark etmez.
