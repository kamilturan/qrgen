# QR Code Generator

QR Code Generator, PyQt6 tabanlı basit ve etkili bir QR kod oluşturma uygulamasıdır. Bu uygulama, kullanıcıların metin verilerini QR kodu formatında oluşturmasına, ön izlemesine ve kaydetmesine olanak tanır.

## Özellikler

- **QR Kod Oluşturma:** Girdiğiniz metne göre QR kodu oluşturur.
- **Özelleştirme:** QR kod ölçeğini (boyutunu) ayarlayabilirsiniz.
- **Ön İzleme:** QR kodunu uygulama üzerinden görüntüleyebilirsiniz.
- **Kaydetme:** Oluşturulan QR kodunu PNG formatında kaydedebilirsiniz.
- **Hakkında Bölümü:** Lisans bilgilerini görüntüleyin.

## Gereksinimler

- Python 3.8 veya üzeri
- PyQt6
- segno

## Kurulum

1. **Gereklilikleri yükleyin**:
   ```bash
   pip install PyQt6 segno

## Kullanım

    "Label" kutucuğuna QR kodunda saklamak istediğiniz metni girin.
    "Scale" kutucuğuna QR kod ölçeğini belirlemek için bir değer girin (varsayılan: 10).
    Generate butonuna basarak QR kodunuzu oluşturun.
    Ön izleme penceresinde QR kodunuzu görüntüleyin.
    "Save" butonuna basarak QR kodunu kaydedin.

## Lisans

