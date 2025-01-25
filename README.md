# Enerji Tüketim Takip Sistemi

Bu proje, endüstriyel makinelerin enerji tüketim verilerini takip etmek, maliyet analizleri yapmak ve karbon emisyonu azaltımına yönelik önerilerde bulunmak için geliştirilmiştir. Aynı zamanda yenilenebilir enerji entegrasyonu ve IoT verileri ile gerçek zamanlı izleme yapılarak sistem optimizasyonu sağlanmaktadır. Bu sistemde ayrıca kullanıcı arayüzü (GUI) ile günlük raporlar, grafikler ve gelecek tüketim tahminleri sunulmaktadır.

## Özellikler

- **Enerji Tüketimi Hesaplaması:** Cihazların günlük ve saatlik enerji tüketimleri hesaplanır.
- **Maliyet Analizi:** Günlük ve aylık maliyetler hesaplanarak, enerji tüketimine dayalı tasarruf önerileri sunulur.
- **Karbon Emisyonu Analizi:** Günlük enerji tüketimine göre karbon emisyonu hesaplanır ve bu emisyonun telafi edilmesi için gereken ağaç sayısı belirlenir.
- **Yenilenebilir Enerji Entegrasyonu:** Güneş ve rüzgar enerjisinden elde edilen enerji ile toplam enerji tüketimi azaltılır.
- **Gerçek Zamanlı İzleme:** IoT cihazlarından gelen veri akışı izlenir ve cihazların durumuna göre uyarılar oluşturulur.
- **Tahminleme:** Geçmiş verilere dayalı olarak gelecekteki enerji tüketimi tahmin edilir.
- **Veri Kaydetme:** Tüm analizler ve hesaplamalar bir CSV dosyasına kaydedilir.
- **Kullanıcı Arayüzü (GUI):** Tkinter ile geliştirilmiş bir arayüz üzerinden raporlar, grafikler ve tahminler görüntülenebilir.

## Kullanım

### Adımlar:
1. Projeyi çalıştırmak için Python yüklü olmalıdır.
2. Gerekli kütüphanelerin kurulu olduğundan emin olun:
   ```bash
   pip install pandas matplotlib scikit-learn numpy
   ```
3. Kodun tamamını bir Python dosyasına yapıştırın ve çalıştırın.

### Fonksiyonlar:
- **Raporu Göster:** Cihazlar, günlük tüketim, maliyet, karbon emisyonu, ağaç sayısı ve optimizasyon önerileri ile ilgili verileri gösterir.
- **Grafikleri Göster:** Günlük enerji tüketimi, yenilenebilir enerji entegrasyonu, IoT veri akışı ve aylık karbon emisyonu azaltımını görselleştirir.
- **Zamanlama Yap:** Günlük analizlerin sabah 8:00'de yapılacağı bilgisi gösterilir.
- **Gelecek Tüketim Tahminlerini Göster:** Gelecek 5 gün için tahmin edilen enerji tüketim değerlerini gösterir.

### Veri Kaydetme:
Proje çalıştırıldığında, tüm veriler ve hesaplamalar `enerji_tuketim_raporu.csv` dosyasına kaydedilecektir.

## Teknolojiler

- **Python:** Proje Python dilinde yazılmıştır.
- **Pandas:** Veri işleme ve analiz için kullanılır.
- **Matplotlib:** Grafiklerin oluşturulmasında kullanılır.
- **Scikit-learn:** Basit lineer regresyon modeli için kullanılır.
- **Tkinter:** Kullanıcı arayüzü oluşturmak için kullanılır.

## Ekran Görüntüleri

- **Günlük Enerji Tüketimi (Cihaz Bazında)**
- **Yenilenebilir Enerji ve Net Tüketim**
- **IoT Durum Verisi**
- **Aylık Karbon Emisyonu Azaltımı**
- **Yenilenebilir Enerji Kullanım Oranı**

## Örnek Çıktılar

- Günlük enerji tüketimi, maliyetler, karbon emisyonu ve tasarruf miktarları.
- Gelecek günler için tahmin edilen enerji tüketimi.
- Yenilenebilir enerji entegrasyonunun toplam enerji tüketimine etkisi.

## Katkıda Bulunanlar
- **Furkan** – Proje sahibi ve geliştirici

Bu proje, endüstriyel enerji yönetimini daha verimli hale getirmek ve çevresel etkileri azaltmak için önemli bir araçtır.
