# Maintainer: [Adınız] <email@example.com>

pkgname=qrgen
pkgver=1.0.0
pkgrel=1
pkgdesc="Basit bir QR kod oluşturucu uygulaması."
arch=('any')
url="https://github.com/kamilturan/qrgen.git"
license=('CC0')
depends=('python' 'python-virtualenv')
source=("qrgen.py" "license.dat" "icons8-qr-50.png")
sha256sums=('SKIP' 'SKIP' 'SKIP')

package() {
    cd "$srcdir"

    # Sanal ortam oluşturma
    mkdir -p "$pkgdir/usr/share/$pkgname"
    python -m venv "$pkgdir/usr/share/$pkgname/venv"

    # Sanal ortama bağımlılıkları yükleme
    source "$pkgdir/usr/share/$pkgname/venv/bin/activate"
    pip install --no-cache-dir PyQt6 segno
    deactivate

    # Uygulama dosyasını yükleme
    install -Dm644 "qrgen.py" "$pkgdir/usr/share/$pkgname/qrgen.py"
    install -Dm644 "license.dat" "$pkgdir/usr/share/licenses/$pkgname/license.dat"
    install -Dm644 "icons8-qr-50.png" "$pkgdir/usr/share/icons/hicolor/64x64/apps/qrgen.png"

    # Çalıştırılabilir başlatıcı script oluşturma
    mkdir -p "$pkgdir/usr/bin"
    echo '#!/bin/bash
source /usr/share/qrgen/venv/bin/activate
python /usr/share/qrgen/qrgen.py "$@"
deactivate' > "$pkgdir/usr/bin/qrgen"
    chmod +x "$pkgdir/usr/bin/qrgen"

   # Menü girişi oluşturma
    mkdir -p "$pkgdir/usr/share/applications"
    echo "[Desktop Entry]
Name=QrGen
Comment=Basit bir QR kod oluşturucu uygulaması
Exec=qrgen
Icon=qrgen
Terminal=false
Type=Application
Categories=Utility;" > "$pkgdir/usr/share/applications/qrgen.desktop"
}
