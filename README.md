# Khanh Đan AI

Ứng dụng AI dạng website có thể cài lên màn hình chính Android/iPhone (PWA).

## Chạy thử trên máy tính

1. Cài Python 3.10 trở lên.
2. Mở terminal tại thư mục dự án:
   ```bash
   python -m venv .venv
   ```
3. Kích hoạt môi trường:
   - Windows: `.venv\\Scripts\\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Cài thư viện:
   ```bash
   pip install -r requirements.txt
   ```
5. Tạo API key trên trang OpenAI Platform, sau đó đặt biến môi trường:
   - Windows PowerShell: `$env:OPENAI_API_KEY="YOUR_API_KEY"`
   - macOS/Linux: `export OPENAI_API_KEY="YOUR_API_KEY"`
6. Chạy:
   ```bash
   uvicorn main:app --reload
   ```
7. Mở http://127.0.0.1:8000

## Đưa lên Internet bằng Render

1. Giải nén dự án và đưa toàn bộ thư mục lên một repository GitHub.
2. Đăng nhập Render, chọn **New + → Web Service**, kết nối repository.
3. Render có thể đọc cấu hình từ `render.yaml`. Nếu cần nhập thủ công:
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Trong Environment của dịch vụ, thêm `OPENAI_API_KEY` với API key của bạn. Không đặt key trong mã HTML/JavaScript, không gửi key cho người khác.
5. Deploy. Mở URL `https://...onrender.com` do Render cấp.

## Cài như ứng dụng trên Android

1. Mở URL HTTPS của website bằng Chrome.
2. Chọn menu ⋮ → **Cài đặt ứng dụng** hoặc **Thêm vào màn hình chính**.
3. Chọn Install/Add. Biểu tượng Khanh Đan AI sẽ xuất hiện trên màn hình.

## Lưu ý

- Ứng dụng cần Internet để gọi AI.
- API sử dụng tính phí theo mức sử dụng của tài khoản API; ChatGPT Plus/Free không bao gồm chi phí API.
- Đặt giới hạn ngân sách và theo dõi Usage trong trang quản lý API.
- Bản mẫu chưa có tài khoản người dùng, lưu lịch sử trên máy chủ, giới hạn tốc độ hay kiểm duyệt nâng cao. Không nhập thông tin bí mật/cá nhân.
- Service worker chỉ cache giao diện tĩnh; tính năng chat cần mạng.
