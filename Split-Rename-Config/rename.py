import os
import glob

# Resimlerin bulunduğu klasörün yolu
klasor_yolu = "dataset/"

# Klasördeki tüm resim dosyalarını bul
resimler_txt = glob.glob(os.path.join(klasor_yolu, "*.txt"))  # Örneğin, .jpg uzantılı resimleri seçtik

# Yeniden adlandırma işlemi
for i, eski_ad in enumerate(resimler_txt, start=1):
    yeni_ad = os.path.join(klasor_yolu, f"{i}.txt")  
    os.rename(eski_ad, yeni_ad)
    print(f"{eski_ad} dosyası {yeni_ad} olarak yeniden adlandırıldı.")