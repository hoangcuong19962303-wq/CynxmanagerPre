#!/bin/bash
echo ""
echo "══════════════════════════════════════"
echo "  Cynx Manager - Premium Setup v2"
echo "══════════════════════════════════════"
echo ""

REPO_URL="https://raw.githubusercontent.com/hoangcuong19962303-wq/CynxmanagerPre/refs/heads/main"
INSTALL_DIR="/sdcard/Download"
TOOL_FILE="$INSTALL_DIR/Cynx-Manager.py"

echo "[1/6] Setting up storage..."
termux-setup-storage
sleep 2

echo "[2/6] Fixing & Updating Termux packages..."
pkg update -y && pkg upgrade -y
pkg install libnghttp2 -y
pkg reinstall curl -y

echo "[3/6] Installing Python & tools..."
pkg install python python-pip tsu libexpat openssl -y

echo "[4/6] Installing Python packages..."
pip install requests colorama aiohttp prettytable

echo "[5/6] Downloading Cynx Manager..."
curl -Ls "$REPO_URL/Cynx-Manager.py" -o "$TOOL_FILE"

# Verify file integrity
echo "[*] Verifying file integrity..."
CHECKSUMS=$(curl -Ls "$REPO_URL/checksums.sha256")
if [ -n "$CHECKSUMS" ]; then
    EXPECTED_HASH=$(echo "$CHECKSUMS" | grep "Cynx-Manager.py" | awk '{print $1}')
    if [ -n "$EXPECTED_HASH" ]; then
        ACTUAL_HASH=$(sha256sum "$TOOL_FILE" 2>/dev/null | awk '{print $1}')
        if [ -z "$ACTUAL_HASH" ]; then
            # Some systems use shasum instead
            ACTUAL_HASH=$(shasum -a 256 "$TOOL_FILE" 2>/dev/null | awk '{print $1}')
        fi
        if [ "$EXPECTED_HASH" = "$ACTUAL_HASH" ]; then
            echo "[+] ✅ File integrity verified!"
        else
            echo "[*] ℹ️  Hash khac nhau (co the do dang cap nhat). Tiep tuc cai dat..."
        fi
    else
        echo "[!] Khong the verify - checksums khong co entry cho file nay"
    fi
else
    echo "[!] Khong the tai checksums - bo qua verification"
fi

echo "[6/6] Creating shortcut..."
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
