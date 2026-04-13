# 🛡️ Cynx Manager - Premium Edition

![Banner](https://img.shields.io/badge/Status-Premium-gold?style=for-the-badge&logo=roblox)
![Version](https://img.shields.io/badge/Version-2.5.0-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Android_Root-green?style=for-the-badge&logo=android)
![Python](https://img.shields.io/badge/Python-3.8_→_3.15+-yellow?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Security-Hardened_v2-red?style=for-the-badge&logo=shield)

**Cynx Manager Premium** là công cụ quản lý và tối ưu hóa treo game (Auto Rejoin) chuyên nghiệp nhất dành cho Roblox trên Android (Termux). Được tối ưu đặc biệt cho **Cloud Phone ARM** với hiệu năng vượt trội.

> [!IMPORTANT]
> **Mua Key Bản Quyền**: Bạn cần có Key Premium để sử dụng Tool. Truy cập ngay: **[https://client.sieuthicloud247.com/](https://client.sieuthicloud247.com/)** để mua hoặc gia hạn Key.

---

## 🆕 Changelog v2.5.0

### ⚡ Tối ưu hiệu năng (ARM Cloud Phone)
- **Batch subprocess**: Gộp 50+ lệnh tối ưu hệ thống thành 1 script duy nhất
- **Async HTTP monitoring**: Kiểm tra trạng thái tất cả users trong 1 API call (giảm ~90% thời gian)
- **Cache thông minh**: Cache process list (3s), /proc reads (5s), giảm I/O disk
- **Smart screen refresh**: Chỉ cập nhật khi có thay đổi (giảm ~70% terminal I/O)
- **Tối ưu system chỉ chạy 1 lần** khi khởi động (kernel params không tự reset)
- **Monitoring loop: từ ~40s → ~3s** mỗi vòng

### 🔒 Bảo mật Hardened v2
- **HTTPS API**: License key được truyền qua HTTPS (không còn plaintext)
- **POST authentication**: Key không bị lộ trong URL/server logs
- **HWID đa nguồn**: Kết hợp 4 hardware identifiers + SHA256 hash (chống giả mạo)
- **Encrypted license**: File key được mã hoá HMAC — vô dụng trên thiết bị khác
- **Anti-tamper nâng cao**: Phát hiện exec() hook, frame inspection, runtime code hash
- **Integrity verification**: SHA256 checksum cho tất cả file khi cài đặt

### 🔔 Webhook Fix & Cải tiến
- **Auto-start**: Webhook tự khởi động khi restart tool (nếu đã cấu hình)
- **Screenshot fallback**: Gửi text-only nếu không chụp được màn hình
- **Multi-method screenshot**: Thử 3 phương pháp chụp (binary, shell, su)
- **Test trước khi chạy**: Gửi tin nhắn thử ngay khi setup
- **Discord rate limit**: Tự xử lý HTTP 429 với retry thông minh

### 🐛 Bug Fixes
- Fix accounts/server_links lệch gây crash
- Fix `asyncio.run()` crash trên Python 3.8-3.9
- Fix executor check block 230s trong monitoring loop (giảm còn 15s)
- Fix `kill_all_roblox()` scan lại packages mỗi lần (dùng cache)

---

## ✨ Tính năng chính

### 🚀 Hệ thống ép xung (Overclock Boost)
- **CPU Performance**: Ép tất cả nhân xử lý chạy tối đa, chống throttle
- **GPU High-Performance**: Boost Adreno/Mali lên performance mode
- **Storage Optimizer**: fstrim + I/O Scheduler tối ưu cho game
- **RAM Latency Tweak**: Giảm độ trễ RAM, ưu tiên tài nguyên cho Roblox
- ⚡ Tất cả chạy **1 lần duy nhất** bằng 1 script gộp — không gây lag

### 🤖 Smart Auto Rejoin 2.0
- **Crash Detection**: Phát hiện app crash/văng → tự khởi động lại
- **Stale Detection**: Phát hiện treo máy, mất kết nối → auto rejoin
- **Executor Check**: Đảm bảo Lua script luôn active sau rejoin
- **Batch Monitoring**: Kiểm tra tất cả accounts cùng lúc (1 API call)
- **Force Rejoin**: Ép rejoin toàn bộ định kỳ (safety net)

### 🛡️ Bảo mật
- **License API**: HTTPS + POST body + HWID đa nguồn
- **Encrypted storage**: Key mã hoá bằng HWID thiết bị
- **Code protection**: 5 lớp mã hoá + 7 lớp anti-tamper
- **Integrity check**: SHA256 verify file khi cài đặt

### 🔔 Discord Webhook
- Gửi thông báo rejoin alert + ảnh chụp màn hình định kỳ
- Auto-start khi restart tool
- Fallback text-only nếu screenshot fail
- Rate limit handling

### 📊 Lua Script In-Game (Cynx-Script)
- **Extreme FPS Boost**: Tắt shadow, particles, post effects
- **Graphics Optimizer**: Batch optimize tất cả objects
- **FPS Counter**: Hiển thị FPS realtime
- **Executor Status**: Báo cáo trạng thái cho Python tool

---

## 📥 Cài đặt

### Cài đặt nhanh (Khuyên dùng)
```bash
pkg update -y && pkg install libnghttp2 curl -y && curl -Ls "https://raw.githubusercontent.com/hoangcuong19962303-wq/CynxmanagerPre/refs/heads/main/cynxsetup.sh" | bash
```

### Chạy Tool
```bash
cynx
```

> [!NOTE]
> Cần cấp quyền **Root** cho Termux để kích hoạt tính năng ép xung và monitoring đầy đủ.

---

## ⚙️ Cấu hình

| Cài đặt | Mặc định | Mô tả |
|---------|----------|-------|
| `force_rejoin_interval` | 60 phút | Chu kỳ ép rejoin toàn bộ |
| `monitoring_delay` | 25 giây | Thời gian chờ giữa các lần check |
| `stale_timeout` | 5 phút | Thời gian offline trước khi auto rejoin |
| `executor_timeout` | 230 giây | Timeout chờ executor active |
| `loop_sleep` | 90 giây | Sleep giữa các monitoring cycle |
| `auto_clear_cache` | true | Tự xoá cache Roblox khi khởi động |

---

## 📂 Cấu trúc file

```
📁 CynxmanagerPre/
├── Cynx-Manager.py     # Tool chính (obfuscated)
├── Cynx-Script          # Lua script in-game
├── cynxsetup.sh         # Script cài đặt
├── checksums.sha256     # SHA256 integrity hash
├── Authencator          # Remote auth flag
└── README.md            # File này
```

---

## 📞 Hỗ trợ

- **Mua Key**: [https://client.sieuthicloud247.com/](https://client.sieuthicloud247.com/)
- **Website**: [sieuthicloud247.com](https://sieuthicloud247.com)
- **Developer**: Cynx2502
- **Telegram**: [@Cynx2502](https://t.me/Cynx2502)

---

## 📋 Yêu cầu hệ thống

| Yêu cầu | Chi tiết |
|----------|----------|
| OS | Android 8.1+ (ARM) |
| Root | ✅ Bắt buộc |
| Terminal | Termux |
| Python | 3.8 → 3.15+ |
| RAM | 1GB+ khuyên dùng |
| Mạng | Ổn định cho API calls |

---
*© 2024-2026 Cynx Manager Premium. Developed by Cynx2502. All rights reserved.*
