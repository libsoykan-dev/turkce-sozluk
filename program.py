    # Türk Dil Kurumu Sözlüğü'nün veritabanında çevrimdışı sorgu yapma olanağı sağlayan program.
    # Copyright (C) 2022 libsoykan-dev

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json # JSON veritabanını işlemek için json kütüphanesi eklenir

import veritabani # veritabani.py dosyası içe aktarılır. (veritabani.py dosyasını edindiğinizden emin olun!)

sozluk = json.loads(veritabani.jsondata) # Sözlük Veritabanı içe aktarılır

kelime = input("Kelime: ") # Kelime girişi istenir

for arama in sozluk: # Sözlükte kelime arama döngüsü

    if kelime.lower() == arama['kelime'].lower(): # Eşleşme bulunursa

        sanlam = int(arama['sanlam']) + 1 # Kelimenin kaç anlamı olduğu okunur

        for gug in range(1, sanlam): # Anlamları yazdırma döngüsü

            anlam = arama['anlam' + str(gug)] # Anlamları "anlam" değerine kaydeder

            print("\n", anlam) # Anlamı yazdırır

        else: # !!! Aynı değerlerin art arda yazdırılmasını önlemek için "else" kullanılmıştır

            exit() # Çıkış
