# 🛡️ Cynx Manager - Premium Edition (Pre-Release)

![Banner](https://img.shields.io/badge/Status-Premium-gold?style=for-the-badge&logo=roblox)
![Version](https://img.shields.io/badge/Version-2.2.0-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Android_Root-green?style=for-the-badge&logo=android)

**Cynx Manager Premium** là công cụ quản lý và tối ưu hóa treo game (Auto Rejoin) chuyên nghiệp nhất dành cho Roblox trên Android (Termux). Phiên bản Premium được thiết kế đặc biệt để tối đa hóa hiệu năng thông qua hệ thống ép xung (Overclock) dành riêng cho máy **Root**.

> [!IMPORTANT]
> **Mua Key Bản Quyền**: Bạn cần có Key Premium để sử dụng Tool. Truy cập ngay: **[https://client.sieuthicloud247.com/](https://client.sieuthicloud247.com/)** để mua hoặc gia hạn Key.

---

## ✨ Tính năng nổi bật (Premium Only)

### 🚀 Hệ thống ép xung (Overclock Boost)
- **CPU Performance**: Ép tất cả các nhân xử lý chạy ở công suất tối đa, ngăn tình trạng tụt xung nhịp khi máy nóng.
- **GPU High-Performance**: Boost chip đồ họa (Adreno/Mali) lên mức cao nhất, tăng FPS đáng kể.
- **Storage Optimizer**: Thực hiện `fstrim` và tối ưu I/O Scheduler giúp load dữ liệu game thần tốc.
- **RAM Latency Tweak**: Giảm độ trễ RAM và ép hệ thống ưu tiên tài nguyên cho Roblox.

### 🤖 Smart Auto Rejoin 2.0
- **Per-Package Crash Detection**: Tự động phát hiện và khởi động lại từng app clone riêng biệt nếu bị crash/văng.
- **Stale Detection**: Nhận diện trường hợp treo máy, mất kết nối mạng để tự động Join lại game.
- **Executor Check**: Đảm bảo Script (Luau) luôn được thực thi đúng cách sau mỗi lần Rejoin.

### 🛡️ Bảo mật & Tiện ích
- **Discord Webhook**: Gửi thông báo Rejoin và ảnh chụp màn hình định kỳ về máy điện thoại.
- **Smart Optimizer**: Tự động dọn dẹp Cache và giải phóng ứng dụng chạy ngầm mỗi 10 phút.
- **Cross-Version Support**: Tương thích hoàn toàn với Python 3.8 đến 3.15+ trên mọi phiên bản Termux.

---

## 📥 Hướng dẫn cài đặt và sử dụng

### 1. Cài đặt nhanh (Khuyên dùng)
Mở ứng dụng Termux và dán lệnh sau (tự động sửa lỗi `curl` nếu có):

```bash
pkg update -y && pkg install libnghttp2 curl -y && curl -Ls "https://raw.githubusercontent.com/hoangcuong19962303-wq/CynxmanagerPre/refs/heads/main/cynxsetup.sh" | bash
```

### 2. Cách chạy Tool
Sau khi cài đặt xong, bạn có thể dùng lệnh ngắn:
```bash
cynx
```
*Lưu ý: Để kích hoạt các tính năng ép xung (Overclock), vui lòng cấp quyền Root cho Termux khi Tool yêu cầu.*

---

## ⚙️ Cấu hình cơ bản

- **Force Rejoin Interval**: Chu kỳ ép Rejoin toàn bộ (mặc định 60 phút).
- **Monitoring Delay**: Thời gian chờ giữa các lần kiểm tra trang thái (mặc định 25 giây).
- **Stale Timeout**: Thời gian tối đa cho phép offline trước khi tự động Rejoin (mặc định 5 phút).

---

## 📞 Hỗ trợ và Liên hệ

- **Mua Key Bản Quyền**: [https://client.sieuthicloud247.com/](https://client.sieuthicloud247.com/)
- **Website Chính Thức**: [sieuthicloud247.com](https://sieuthicloud247.com)
- **Developer**: Cynx2502
- **Telegram Support**: [@Cynx2502](https://t.me/Cynx2502)

---
*© 2024-2026 Cynx Manager. All rights reserved.*
