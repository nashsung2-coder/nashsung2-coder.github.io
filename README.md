# Field Notes Archive — GitHub Pages 個人網站

這是一個**不需要額外部署指令**的靜態個人網站。GitHub Pages 已設定為從 `main` 分支根目錄發佈；你在 GitHub 網頁上提交任何 HTML、CSS、JavaScript 或圖片檔案的變更後，網站會自動更新。

## 最常用的更新方式

| 你想做什麼 | 在 GitHub 網頁上的做法 | 要改的檔案或位置 |
|---|---|---|
| 修改首頁文字 | 開啟檔案後按鉛筆圖示編輯，再按 **Commit changes** | `index.html` |
| 換主視覺或新增照片 | 進入資料夾後按 **Add file → Upload files** | `assets/images/` |
| 新增一個頁面 | 複製 `new-page.html`、改成新檔名，再新增首頁連結 | 例如 `projects.html` |
| 修改顏色或版面 | 編輯樣式表 | `assets/css/site.css` |
| 修改互動行為 | 編輯 JavaScript | `assets/js/site.js` |

## 放入自己的照片

請將圖片上傳到 `assets/images/`。接著在 `index.html` 裡尋找例如：

```html
<img src="assets/images/hero.jpg" alt="桌上的筆記本、攝影作品與文具" />
```

把 `hero.jpg` 改成你實際上傳的檔名即可。建議使用 `.jpg`、`.png` 或 `.webp`，檔名使用英文、小寫與連字號，例如 `kyoto-sunrise.jpg`。

## 新增 HTML 頁面

`new-page.html` 是可以複製的起始範本。將它複製後改名，例如 `about.html`，然後在首頁加入：

```html
<a href="about.html">關於我</a>
```

## 注意事項

GitHub Pages 會將這個網站公開在網路上。請不要上傳 Token、密碼、私密照片、個資檔案或任何不希望公開的內容。完成更新後，GitHub Pages 的發佈通常需要短暫時間；可到 GitHub 儲存庫的 **Actions** 或 **Settings → Pages** 查看狀態。

## 檔案結構

```text
.
├── index.html                 # 首頁
├── new-page.html              # 新頁面範本
├── 404.html                   # 找不到頁面時顯示的內容
└── assets/
    ├── css/site.css           # 全站樣式
    ├── js/site.js             # 輕量互動
    └── images/                # 你的照片與圖像
```
