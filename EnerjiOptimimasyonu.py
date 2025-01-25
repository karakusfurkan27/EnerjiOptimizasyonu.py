import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Enerji tüketim verileri
data = {
    'Cihaz': ['Tufting Makinesi', 'Büküm Makinesi', 'Kesme Makinesi', 'Yıkama Makinesi'],
    'Günlük Tüketim (kWh)': [120, 80, 60, 150],
    'Çalışma Süresi (Saat)': [10, 8, 6, 12],
    'Tarih': [datetime.date(2025, 1, i) for i in range(1, 5)]
}

# Veri çerçevesi oluşturma
df = pd.DataFrame(data)

# Saatlik tüketim hesaplama
df['Saatlik Tüketim (kWh)'] = df['Günlük Tüketim (kWh)'] / df['Çalışma Süresi (Saat)']

# Elektrik birim fiyatı (TL/kWh)
unit_price = 2.0  # Örnek birim fiyat

# Günlük maliyet hesaplama
df['Günlük Maliyet (TL)'] = df['Günlük Tüketim (kWh)'] * unit_price

# %10 verimlilik artırımı ile tasarruf hesaplama
df['Tasarruflu Tüketim (kWh)'] = df['Günlük Tüketim (kWh)'] * 0.9
df['Tasarruf (kWh)'] = df['Günlük Tüketim (kWh)'] - df['Tasarruflu Tüketim (kWh)']
df['Tasarruflu Maliyet (TL)'] = df['Tasarruflu Tüketim (kWh)'] * unit_price
savings = df['Günlük Maliyet (TL)'].sum() - df['Tasarruflu Maliyet (TL)'].sum()

# Günlük karbon emisyonu hesaplama (kg CO₂/kWh)
carbon_emission_factor = 0.5  # Örnek emisyon faktörü (kg CO₂/kWh)
df['Karbon Emisyonu (kg CO₂)'] = df['Günlük Tüketim (kWh)'] * carbon_emission_factor

# Karbon telafi hesaplama (örneğin, ağaç dikimi)
tree_absorption = 22  # Bir ağacın yıllık absorbe ettiği CO₂ miktarı (kg)
df['Telafi İçin Ağaç Sayısı'] = (df['Karbon Emisyonu (kg CO₂)'] / tree_absorption).apply(np.ceil)

# Aylık tahmini tüketim ve maliyet hesaplama
df['Aylık Tahmini Tüketim (kWh)'] = df['Günlük Tüketim (kWh)'] * 30
df['Aylık Tahmini Maliyet (TL)'] = df['Aylık Tahmini Tüketim (kWh)'] * unit_price

# Aylık karbon emisyonu azaltımı ve ağaç sayısı
df['Aylık Karbon Emisyonu Azaltımı (kg CO₂)'] = (df['Günlük Tüketim (kWh)'] - df['Tasarruflu Tüketim (kWh)']) * carbon_emission_factor * 30
df['Aylık Azaltım İçin Ağaç Sayısı'] = (df['Aylık Karbon Emisyonu Azaltımı (kg CO₂)'] / tree_absorption).apply(np.ceil)

# Toplam enerji tüketimi içinde cihaz oranları
df['Tüketim Oranı (%)'] = (df['Günlük Tüketim (kWh)'] / df['Günlük Tüketim (kWh)'].sum()) * 100

# Eşik değeri belirleme ve uyarı sistemi
threshold = 100  # kWh
df['Uyarı'] = df['Günlük Tüketim (kWh)'].apply(lambda x: 'Yüksek Tüketim!' if x > threshold else 'Normal')

# Günlük toplam enerji tüketimini tarih bazında analiz etme
df['Tarih'] = pd.to_datetime(df['Tarih'])
daily_usage = df.groupby('Tarih')['Günlük Tüketim (kWh)'].sum()

# Gerçek zamanlı izleme (Simülasyon)
real_time_data = np.random.randint(50, 150, size=len(df))
df['Gerçek Zamanlı Tüketim (kWh)'] = real_time_data

# Geçmiş verilerden tahmin (Basit lineer regresyon)
dates = np.arange(len(daily_usage)).reshape(-1, 1)
consumptions = daily_usage.values.reshape(-1, 1)
model = LinearRegression().fit(dates, consumptions)
future_dates = np.arange(len(daily_usage), len(daily_usage) + 5).reshape(-1, 1)
future_predictions = model.predict(future_dates)

# Optimizasyon önerileri
df['Optimizasyon Önerisi'] = df['Günlük Tüketim (kWh)'].apply(
    lambda x: 'Çalışma süresi azaltılabilir.' if x > threshold else 'Düşük tüketim, uygun!'
)

# Yenilenebilir Enerji Entegrasyonu
df['Güneş Enerjisi Üretimi (kWh)'] = np.random.randint(20, 50, size=len(df))
df['Rüzgar Enerjisi Üretimi (kWh)'] = np.random.randint(10, 30, size=len(df))
df['Toplam Yenilenebilir Enerji (kWh)'] = df['Güneş Enerjisi Üretimi (kWh)'] + df['Rüzgar Enerjisi Üretimi (kWh)']
df['Net Enerji Tüketimi (kWh)'] = df['Günlük Tüketim (kWh)'] - df['Toplam Yenilenebilir Enerji (kWh)']

# Emisyon Takibi ve Karbon Ayak İzi Azaltımı
df['Azaltılmış Karbon Emisyonu (kg CO₂)'] = df['Net Enerji Tüketimi (kWh)'] * carbon_emission_factor
df['Azaltılmış Emisyon İçin Ağaç Sayısı'] = (df['Azaltılmış Karbon Emisyonu (kg CO₂)'] / tree_absorption).apply(np.ceil)

# Endüstriyel IoT Entegrasyonu
df['IoT Veri Akışı (kWh)'] = np.random.randint(50, 150, size=len(df))
df['IoT Durum'] = df['IoT Veri Akışı (kWh)'].apply(lambda x: 'Veri Alınıyor' if x >= 100 else 'Düşük Veri Akışı')

# GUI güncellemesi: Veri güncelleme butonu ekleme
def update_data(cihaz, günlük_tüketim, çalışma_süresi, tarih):
    new_data = pd.DataFrame({
        'Cihaz': [cihaz],
        'Günlük Tüketim (kWh)': [günlük_tüketim],
        'Çalışma Süresi (Saat)': [çalışma_süresi],
        'Tarih': [tarih]
    })
    global df
    df = pd.concat([df, new_data], ignore_index=True)
    df['Saatlik Tüketim (kWh)'] = df['Günlük Tüketim (kWh)'] / df['Çalışma Süresi (Saat)']
    df['Günlük Maliyet (TL)'] = df['Günlük Tüketim (kWh)'] * unit_price
    df['Tasarruflu Tüketim (kWh)'] = df['Günlük Tüketim (kWh)'] * 0.9
    df['Tasarruf (kWh)'] = df['Günlük Tüketim (kWh)'] - df['Tasarruflu Tüketim (kWh)']
    df['Tasarruflu Maliyet (TL)'] = df['Tasarruflu Tüketim (kWh)'] * unit_price
    df['Karbon Emisyonu (kg CO₂)'] = df['Günlük Tüketim (kWh)'] * carbon_emission_factor
    df['Telafi İçin Ağaç Sayısı'] = (df['Karbon Emisyonu (kg CO₂)'] / tree_absorption).apply(np.ceil)
    df['Aylık Tahmini Tüketim (kWh)'] = df['Günlük Tüketim (kWh)'] * 30
    df['Aylık Tahmini Maliyet (TL)'] = df['Aylık Tahmini Tüketim (kWh)'] * unit_price
    df['Aylık Karbon Emisyonu Azaltımı (kg CO₂)'] = (df['Günlük Tüketim (kWh)'] - df['Tasarruflu Tüketim (kWh)']) * carbon_emission_factor * 30
    df['Aylık Azaltım İçin Ağaç Sayısı'] = (df['Aylık Karbon Emisyonu Azaltımı (kg CO₂)'] / tree_absorption).apply(np.ceil)
    df['Tüketim Oranı (%)'] = (df['Günlük Tüketim (kWh)'] / df['Günlük Tüketim (kWh)'].sum()) * 100
    messagebox.showinfo("Başarılı", "Veri başarıyla güncellendi!")

# GUI Tasarımı
def gui_main():
    window = tk.Tk()
    window.title("Enerji Tüketim Takip Sistemi")
    
    # Cihaz adı
    cihaz_label = tk.Label(window, text="Cihaz Adı:")
    cihaz_label.grid(row=0, column=0)
    cihaz_entry = tk.Entry(window)
    cihaz_entry.grid(row=0, column=1)

    # Günlük tüketim
    günlük_tüketim_label = tk.Label(window, text="Günlük Tüketim (kWh):")
    günlük_tüketim_label.grid(row=1, column=0)
    günlük_tüketim_entry = tk.Entry(window)
    günlük_tüketim_entry.grid(row=1, column=1)

    # Çalışma süresi
    çalışma_süresi_label = tk.Label(window, text="Çalışma Süresi (Saat):")
    çalışma_süresi_label.grid(row=2, column=0)
    çalışma_süresi_entry = tk.Entry(window)
    çalışma_süresi_entry.grid(row=2, column=1)

    # Tarih
    tarih_label = tk.Label(window, text="Tarih (YYYY-MM-DD):")
    tarih_label.grid(row=3, column=0)
    tarih_entry = tk.Entry(window)
    tarih_entry.grid(row=3, column=1)

    # Veri güncelleme butonu
    update_button = tk.Button(window, text="Veri Güncelle", command=lambda: update_data(cihaz_entry.get(), 
                                             float(günlük_tüketim_entry.get()), float(çalışma_süresi_entry.get()), 
                                             pd.to_datetime(tarih_entry.get()).date()))
    update_button.grid(row=4, column=0, columnspan=2)

    window.mainloop()

# Ana GUI uygulaması
gui_main()
