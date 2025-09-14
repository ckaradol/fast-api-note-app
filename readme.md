# Connectinno - Not Alma Uygulaması Backend (FastAPI)

## 🎯 Proje Hakkında
Bu proje, FastAPI kullanılarak geliştirilmiş bir not alma backend servisidir.  
Uygulama, kullanıcı kimlik doğrulama, not CRUD işlemleri, arama & filtreleme, sabitleme ve geri alma gibi tüm temel özellikleri destekler.  
Firebase veya Supabase ile entegre edilmiştir ve sadece not sahibi kullanıcıların verilere erişmesine izin verir.

---

## 📝 Özellikler

### Kullanıcı Yönetimi
- Kayıt, giriş ve çıkış işlemleri.
- Firebase Authentication ile güvenli kullanıcı yönetimi.

### Not Yönetimi (CRUD)
- `GET /notes` → Kullanıcının tüm notlarını listeler.
- `POST /notes` → Yeni not oluşturur.
- `PUT /notes/{id}` → Not günceller.
- `DELETE /notes/{id}` → Not siler, silinen notlar için Undo özelliği desteklenir.

### Notları Sabitleme / Favorilere Ekleme
- Notlar sabitlenebilir ve listede en üstte gösterilir.

### Arama & Filtreleme
- Başlığa veya içeriğe göre filtreleme yapılabilir.
- Veriler hem çevrimdışı önbellekten hem de backend’den hızlı şekilde sorgulanabilir.

### Hata Yönetimi & Güvenlik
- Geçersiz isteklerde anlamlı hata mesajları döner.
- Sadece not sahibi kullanıcıya veri erişim izni verilir.

### Çevrimdışı Senkronizasyon
- Mobil istemciler için çevrimdışı önbellekleme ile uyumlu.
- Ağ bağlantısı olduğunda backend ile otomatik senkronizasyon sağlanır.

---

## 📦 Endpointler

| Method | Endpoint        | Açıklama                  |
|--------|----------------|---------------------------|
| GET    | /notes          | Kullanıcının notlarını listeler |
| POST   | /notes          | Yeni not oluşturur        |
| PUT    | /notes/{id}     | Mevcut notu günceller     |
| DELETE | /notes/{id}     | Notu siler|

---

## ⚡ Kurulum ve Çalıştırma

```bash
# Repo klonla
git clone https://github.com/kullanici/connectinno_backend.git
cd connectinno_backend

# Sanal ortam oluştur ve etkinleştir
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# API'yi başlat
uvicorn main:app --reload
