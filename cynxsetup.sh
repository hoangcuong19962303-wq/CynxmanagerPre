#!/bin/bash
echo ""
echo "══════════════════════════════════════"
echo "  Cynx Manager - Premium Setup"
echo "══════════════════════════════════════"
echo ""

echo "[1/5] Setting up storage..."
termux-setup-storage
sleep 2

echo "[2/5] Fixing & Updating Termux packages..."
# Fix potentially broken packages and update all to prevent library link errors
pkg update -y && pkg upgrade -y
pkg install libnghttp2 -y
pkg reinstall curl -y

echo "[3/5] Installing Python & tools..."
pkg install python python-pip tsu libexpat openssl -y

echo "[4/5] Installing Python packages..."
pip install requests colorama aiohttp prettytable

echo "[5/5] Downloading Cynx Manager..."
curl -Ls "https://raw.githubusercontent.com/hoangcuong19962303-wq/CynxmanagerPre/refs/heads/main/Cynx-Manager.py" -o /sdcard/Download/Cynx-Manager.py

# Create shortcut command
echo '#!/bin/bash' > /data/data/com.termux/files/usr/bin/cynx
echo 'su -c "/data/data/com.termux/files/usr/bin/python /sdcard/Download/Cynx-Manager.py"' >> /data/data/com.termux/files/usr/bin/cynx
chmod +x /data/data/com.termux/files/usr/bin/cynx

echo ""
echo "══════════════════════════════════════"
echo "  ✅ Setup completed!"
echo ""
echo "  Cach chay (chon 1 trong 2):"
echo ""
echo "  1. Lenh ngan:  cynx"
echo "  2. Lenh day du: su -c '/data/data/com.termux/files/usr/bin/python /sdcard/Download/Cynx-Manager.py'"
echo ""
echo "══════════════════════════════════════"
