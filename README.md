# Nash Pages：HTML 靜態導覽框架

這是一個可放在 GitHub Pages 的純 HTML 網站框架。首頁只保留導覽列；新增內容時，只要從 `templates/page-template.html` 複製一份 HTML 到 `pages/` 資料夾，並在檔案開頭設定名稱與排序。每次提交後，GitHub Actions 都會更新導覽列所需的 `pages.json`。

請先閱讀 [FORMAT.md](FORMAT.md)，再建立第一個頁面。這個專案不需要 Node.js、資料庫或 API Key。

## 基本結構

```text
.
├── index.html                       # 空白首頁與導覽列
├── pages/                            # 你新增的 HTML 頁面
├── templates/page-template.html      # 可複製的頁面格式檔
├── assets/css/site.css               # 全站樣式
├── assets/js/nav.js                  # 自動導覽列程式
├── scripts/build_navigation.py       # 由 GitHub Actions 執行
├── pages.json                        # 自動產生，請不要手動編輯
└── FORMAT.md                         # 中文寫作與排序說明
```

GitHub Pages 會公開這個網站。請不要上傳 Token、密碼、私密照片、個資檔案或任何不希望公開的內容。
