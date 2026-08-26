# Nash Pages 格式引導文件

這是一套給 GitHub Pages 使用的純 HTML 網站框架。首頁刻意只保留導覽列；你不需要修改 JavaScript，也不需要手動重寫選單。每次新增或修改一個 HTML 頁面後，系統會依頁面最上方的設定，自動更新導覽列的名稱、順序與可見性。

> **最短工作流程：** 複製 `templates/page-template.html` → 存到 `pages/` → 填寫三個 `<meta>` → 寫 HTML → 按 **Commit changes** → 檢查網站。

這份文件本身也可以作為其他靜態網站的操作說明範本：保留「檔案位置、必填設定、可複製範例、錯誤排查與檢查清單」五個段落，即可改寫成不同網站的引導文件。

## 檔案結構與用途

| 路徑 | 功能 | 你平常是否需要修改 |
|---|---|---|
| `index.html` | 空白首頁與共用導覽列 | 通常不需要 |
| `pages/` | 放你新增的公開或隱藏 HTML 頁面 | **需要** |
| `templates/page-template.html` | 可複製的頁面格式檔 | 複製，不直接改動 |
| `assets/css/site.css` | 全站基本樣式 | 想調整顏色或排版時才修改 |
| `assets/js/nav.js` | 讀取自動導覽列 | 不需要修改 |
| `pages.json` | 導覽列資料清單 | **不要手動修改** |
| `FORMAT.md` | 簡短格式說明 | 可閱讀 |
| `GUIDE.zh-Hant.md` | 本份完整引導文件 | 可閱讀 |

## 新增第一個頁面

假設你要建立「關於我」。先在 GitHub 儲存庫開啟 `templates/page-template.html`，使用 **Copy raw file** 或複製整份內容；再進入 `pages/` 資料夾，按 **Add file → Create new file**，將檔案命名為 `about.html`，貼上內容。最後，填寫頁面上方的三個設定欄位，並在 `<main class="page-content">` 中寫下你的內容。

| 步驟 | 要做的事 | 範例 |
|---|---|---|
| 1 | 複製格式檔 | `templates/page-template.html` |
| 2 | 建立新檔案 | `pages/about.html` |
| 3 | 填寫導覽設定 | `關於我`、`10`、`true` |
| 4 | 寫入 HTML 內容 | `<h1>...</h1>`、`<p>...</p>` |
| 5 | 提交變更 | **Commit changes** |

## 三個導覽設定：請全部填寫

每個頁面的 `<head>` 裡都有三個 `site-nav-` 設定。**請將三個都視為必填欄位**，即使其中一個技術上有預設值，也不要省略。完整填寫可避免頁面被意外隱藏、排序跑到最後或無法被導覽系統辨識。

| 設定欄位 | 用途 | 正確格式 | 實際預設行為 | 建議 |
|---|---|---|---|---|
| `site-nav-title` | 導覽列顯示名稱 | 短文字 | 無名稱時，頁面不會加入導覽列 | **務必填寫** |
| `site-nav-order` | 導覽排序數字 | 純整數，例如 `10` | 省略或非數字時會排到後面 | **務必填寫** |
| `site-nav-visible` | 是否顯示在導覽列 | `true` 或 `false` | 省略時會視為 `true` | **仍務必填寫** |

```html
<!-- 放在 <head> 內；新增頁面時只需要先改這三行。 -->
<meta name="site-nav-title" content="關於我" />
<meta name="site-nav-order" content="10" />
<meta name="site-nav-visible" content="true" />
```

排序建議使用 `10`、`20`、`30` 這種有間隔的數字。日後想在「關於我」與「作品」之間插入「凌極世界」時，可使用 `15`，不必重新調整所有頁面的排序。

## 可直接複製的完整 HTML 頁面

以下內容可直接存為 `pages/about.html`。請把「關於我」、`10`、標題和段落替換為你的實際內容。

```html
<!doctype html>
<html lang="zh-Hant">
  <head>
    <!-- 導覽列設定：三個都請填寫。 -->
    <meta name="site-nav-title" content="關於我" />
    <meta name="site-nav-order" content="10" />
    <meta name="site-nav-visible" content="true" />

    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <!-- title 建議固定採用「頁面名稱 — 網站名稱」。 -->
    <title>關於我 — 宋嵐緒</title>
    <link rel="icon" type="image/png" href="../assets/images/avatar-circle.png" />
    <link rel="stylesheet" href="../assets/css/site.css" />
  </head>
  <body>
    <!-- 請保留 header 與 nav.js；它們提供全站一致的自動導覽列。 -->
    <header class="site-header" data-site-navigation>
      <a class="site-brand" href="/" aria-label="宋嵐緒首頁">
        <img class="site-brand-avatar" src="../assets/images/avatar-circle.png" alt="宋嵐緒的角色插圖" />
        <span>宋嵐緒</span>
      </a>
      <nav class="site-nav" aria-label="網站導覽" data-navigation-list></nav>
      <span class="site-status">STATIC INDEX</span>
    </header>

    <!-- 從這裡開始寫你的內容。 -->
    <main class="page-content">
      <p class="page-kicker">ABOUT / 10</p>
      <h1>在這裡寫你的大標題</h1>
      <p>這裡是第一段內容。你可以像平常寫 HTML 一樣加入文字、連結、圖片、清單或其他標籤。</p>
      <p>這裡是第二段內容。</p>
    </main>

    <script src="../assets/js/nav.js"></script>
  </body>
</html>
```

## 預留 class 的用途

格式檔中的 class 已經有基本樣式。建議先保留它們，等熟悉後再自行調整 CSS。

| Class | 用途 | 建議做法 |
|---|---|---|
| `site-header` | 頂端固定導覽列外框 | 請保留 |
| `site-brand` | 左側的角色圖示與「宋嵐緒」首頁連結 | 可改名稱文字，不要移除圖片與連結 |
| `site-brand-avatar` | 圓形角色圖示 | 請保留圖片路徑與 `alt` 文字 |
| `site-nav` | 自動插入導覽連結的位置 | 請保留 `data-navigation-list` |
| `page-content` | 內容區域的最大寬度、間距與閱讀排版 | 放所有主要內容 |
| `page-kicker` | 標題上方的小字分類或編號 | 例如 `ABOUT / 10`、`NOTE / 20` |

## 編輯、刪除與隱藏既有頁面

### 編輯頁面

要修改既有內容時，直接開啟 `pages/` 中對應的 HTML 檔案，編輯 `<main>` 內的文字、圖片或連結後提交即可。如果你同時修改了 `site-nav-title`、`site-nav-order` 或 `site-nav-visible`，導覽列也會跟著重新整理。

### 刪除頁面

如果某一頁不再需要，直接在 GitHub 開啟 `pages/` 下的對應 HTML，使用 **Delete file** 並提交。系統會重新建立導覽清單，因此不需要手動刪除選單項目，也不需要編輯 `pages.json`。

### 建立不顯示在導覽列的頁面

某些頁面可能只想透過特定網址分享，例如草稿、閱讀筆記或活動頁。將 `site-nav-visible` 設為 `false`，它仍然可以用網址開啟，但不會出現在導覽列。

```html
<meta name="site-nav-title" content="閱讀筆記" />
<meta name="site-nav-order" content="90" />
<meta name="site-nav-visible" content="false" />
```

如果檔案名稱是 `pages/private-note.html`，網址會是：

```text
https://nashsung.crestylon.org/pages/private-note.html
```

> `false` 只代表「不顯示於導覽列」，不是保密功能。網站內容仍公開可讀；知道網址的人仍能開啟頁面。

## `<title>` 的一致性

每個頁面的 `<title>` 建議固定使用：**頁面名稱 — 網站名稱**。例如：

```html
<title>凌極世界 — Nash Pages</title>
```

這樣瀏覽器分頁更容易辨認，搜尋結果也較能顯示清楚的頁面名稱。`site-nav-title` 是導覽列短名稱，`<title>` 則是瀏覽器與搜尋引擎辨識用的完整名稱；兩者最好對應，但不必完全相同。

## 圖片、檔案命名與連結

圖片請先上傳到 `assets/images/`。由於內容頁面放在 `pages/` 資料夾，圖片路徑要寫成 `../assets/images/檔名`。

```html
<img src="../assets/images/my-photo.jpg" alt="用一句話描述圖片內容" />
<a href="https://example.com" target="_blank" rel="noreferrer">開啟外部連結</a>
```

請使用**英文小寫、連字號與副檔名**命名，例如 `my-photo.jpg`、`cestylon-notes-2026.pdf`。避免檔名包含空格、中文、特殊符號或容易混淆的大小寫。GitHub Pages 的檔案路徑區分大小寫，因此上傳 `My-Photo.jpg` 後，HTML 也必須完全寫成 `My-Photo.jpg`；寫成 `my-photo.jpg` 會找不到圖片。

| 想放的內容 | 可用 HTML |
|---|---|
| 大標題 | `<h1>標題</h1>` |
| 小標題 | `<h2>小標題</h2>` |
| 一段文字 | `<p>文字</p>` |
| 外部連結 | `<a href="https://...">連結文字</a>` |
| 圖片 | `<img src="../assets/images/檔名.jpg" alt="描述" />` |
| 無序清單 | `<ul><li>第一點</li><li>第二點</li></ul>` |
| 有序清單 | `<ol><li>第一步</li><li>第二步</li></ol>` |

## 發布、快取與檢查

提交後，GitHub 會先執行導覽清單更新，再發布網站。通常只需稍候片刻；若看見舊內容，可依序確認 GitHub 的 **Actions** 是否完成、重新整理頁面，或使用網址參數開啟，例如 `https://nashsung.crestylon.org/?v=2`。

若仍顯示舊版，可執行強制重新整理：Windows 使用 `Ctrl + F5`，macOS 使用 `Cmd + Shift + R`。這會跳過瀏覽器已儲存的舊快取，重新向網站要求最新版本。

| 狀況 | 優先檢查 |
|---|---|
| 新頁面沒有出現在導覽列 | 三個 `<meta>` 是否全在 `<head>` 內；`site-nav-title` 是否有內容；`site-nav-visible` 是否為 `true` |
| 排序不對 | `site-nav-order` 是否為純數字，例如 `20`，不是 `第二頁` |
| 頁面有開啟但沒有導覽列 | 是否保留 `data-navigation-list` 與最下方的 `../assets/js/nav.js` |
| 圖片無法顯示 | 檔名大小寫是否一致；路徑是否從 `../assets/images/` 開始 |
| 網站還是舊內容 | 等待工作流程完成；重新整理、強制重新整理或加上 `?v=2` |

## 公開網站的安全提醒

GitHub Pages 上的所有檔案都可能被公開讀取。請不要上傳 API Key、Token、密碼、私密文件、電話、住址、身分證件照片、個人帳號資料、未公開的真實姓名，或其他不希望被搜尋、下載與轉傳的資料。即使頁面設定為 `site-nav-visible="false"`，它也不是私人頁面。

## 提交前快速檢查清單

提交前，請確認以下項目：

- [ ] 我是從 `templates/page-template.html` 複製建立頁面。
- [ ] 三個 `<meta>` 都已填寫，而且位於 `<head>` 內。
- [ ] `site-nav-title` 短而清楚，`site-nav-order` 是數字，`site-nav-visible` 是 `true` 或 `false`。
- [ ] `<title>` 使用「頁面名稱 — 網站名稱」格式。
- [ ] 圖片檔名為英文小寫與連字號，HTML 路徑及大小寫完全一致。
- [ ] 我保留了 `site-header`、`data-navigation-list` 與 `nav.js`。
- [ ] 我沒有放入 API Key、Token、密碼或私人資料。
- [ ] 提交後已開啟網站，確認導覽順序、頁面連結與圖片正常。

> **再提醒一次：** 不要手動編輯 `pages.json`。它是依照 HTML 中的導覽設定自動產生的結果。
