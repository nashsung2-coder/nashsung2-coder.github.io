# Nash Pages 格式引導文件

這份文件教你如何維護目前的靜態網站。網站首頁刻意只保留導覽列；你不需要碰 JavaScript，也不需要手動修改導覽列。只要新增一個 HTML 檔案、填好三個設定欄位、寫下你的 HTML 內容並提交，導覽列就會依你指定的順序自動更新。

> **核心規則：** 新頁面放進 `pages/`，並從 `templates/page-template.html` 複製格式。不要手動編輯 `pages.json`，因為它會自動產生。

## 一次看懂：新增第一個頁面

假設你要建立「關於我」頁面。請在 GitHub 儲存庫開啟 `templates/page-template.html`，按右上角的 **Copy raw file** 或複製內容；接著在 `pages/` 資料夾中新增檔案 `about.html`，把內容貼上。請在頁面最上方填寫名稱、排序與顯示設定，再填寫你的 HTML 內容，最後按 **Commit changes**。

| 步驟 | 你要做的事 | 位置 |
|---|---|---|
| 1 | 複製格式檔 | `templates/page-template.html` |
| 2 | 建立頁面檔 | `pages/about.html` |
| 3 | 填寫名稱、排序、顯示設定 | HTML 最上方的三個 `<meta>` |
| 4 | 寫下頁面內容 | `<main class="page-content">` 內 |
| 5 | 提交變更 | GitHub 的 **Commit changes** |

## 三個必填的導覽設定

每個頁面的 `<head>` 裡都有三行設定。它們決定導覽列顯示的名稱、位置與可見性。

| 設定欄位 | 功能 | 可填內容 | 範例 |
|---|---|---|---|
| `site-nav-title` | 導覽列顯示的名稱 | 任何短文字 | `關於我` |
| `site-nav-order` | 導覽列排列順序 | 整數；數字越小越靠左 | `10` |
| `site-nav-visible` | 是否顯示於導覽列 | `true` 或 `false` | `true` |

請優先使用 `10`、`20`、`30` 這種有間隔的排序。日後想在「關於我」和「作品」之間加一頁時，可以直接用 `15`，不必重新調整所有頁面。

```html
<!-- 放在 <head> 內；只需要改這三行。 -->
<meta name="site-nav-title" content="關於我" />
<meta name="site-nav-order" content="10" />
<meta name="site-nav-visible" content="true" />
```

## 可直接複製的完整頁面範例

以下範例可以直接存成 `pages/about.html`。你只要替換標題和段落內容即可。

```html
<!doctype html>
<html lang="zh-Hant">
  <head>
    <!-- 導覽列設定 -->
    <meta name="site-nav-title" content="關於我" />
    <meta name="site-nav-order" content="10" />
    <meta name="site-nav-visible" content="true" />

    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="../assets/css/site.css" />
    <title>關於我 — Nash Pages</title>
  </head>
  <body>
    <!-- 請保留以下導覽列，不需要自行新增選單連結。 -->
    <header class="site-header" data-site-navigation>
      <a class="site-brand" href="/">NASH / PAGES</a>
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

    <!-- 請保留這行，它會讀取自動排序的導覽列。 -->
    <script src="../assets/js/nav.js"></script>
  </body>
</html>
```

## 排序範例

下表展示導覽列的最終順序。首頁固定是 `0`；其他頁面依 `site-nav-order` 的數字由小到大排列。

| 檔案 | `site-nav-title` | `site-nav-order` | 導覽列位置 |
|---|---|---:|---|
| `index.html` | 首頁 | 0 | 第一個 |
| `pages/about.html` | 關於我 | 10 | 第二個 |
| `pages/projects.html` | 作品 | 20 | 第三個 |
| `pages/contact.html` | 聯絡 | 30 | 第四個 |

如果你後來要建立「凌極世界」頁面，而且希望它在「關於我」與「作品」之間，就設定成：

```html
<meta name="site-nav-title" content="凌極世界" />
<meta name="site-nav-order" content="15" />
<meta name="site-nav-visible" content="true" />
```

## 建立不顯示在導覽列的頁面

有些頁面可能只想透過特定網址分享，例如閱讀筆記、活動頁或尚未完成的草稿。將 `site-nav-visible` 設為 `false`，頁面仍然可以用網址開啟，但不會出現在導覽列。

```html
<meta name="site-nav-title" content="閱讀筆記" />
<meta name="site-nav-order" content="90" />
<meta name="site-nav-visible" content="false" />
```

若檔案名稱是 `pages/private-note.html`，網址會是：

```text
https://nashsung.crestylon.org/pages/private-note.html
```

> **提醒：** `false` 只是「不顯示在導覽列」，不是保密功能。GitHub Pages 是公開網站；知道網址的人仍然能看到頁面。

## 加入圖片、連結與基本 HTML

請先把圖片上傳到 `assets/images/`。因為你的頁面在 `pages/` 資料夾內，圖片路徑需要往上一層寫成 `../assets/images/檔名`。

```html
<img src="../assets/images/my-photo.jpg" alt="用一句話描述圖片內容" />

<a href="https://example.com" target="_blank" rel="noreferrer">
  開啟外部連結
</a>
```

| 你想放的內容 | 可用 HTML |
|---|---|
| 大標題 | `<h1>標題</h1>` |
| 小標題 | `<h2>小標題</h2>` |
| 一段文字 | `<p>文字</p>` |
| 外部連結 | `<a href="https://...">連結文字</a>` |
| 圖片 | `<img src="../assets/images/檔名.jpg" alt="描述" />` |
| 無序清單 | `<ul><li>第一點</li><li>第二點</li></ul>` |
| 有序清單 | `<ol><li>第一步</li><li>第二步</li></ol>` |

## 發布與檢查

你在 GitHub 按下 **Commit changes** 後，網站會開始更新。導覽列的頁面清單由工作流程自動整理，因此不用自己新增選單連結或調整 `pages.json`。完成後，請打開 <https://nashsung.crestylon.org/>，確認新頁面出現在正確位置，並點擊一次連結確認網址正常。

| 狀況 | 先檢查什麼 |
|---|---|
| 新頁面沒有出現在導覽列 | 三個 `<meta>` 是否都在 `<head>` 內；`site-nav-visible` 是否為 `true` |
| 排序不對 | `site-nav-order` 是否填入純數字，例如 `20` 而不是 `第二頁` |
| 頁面有開啟但沒有導覽列 | 是否保留 `data-navigation-list` 與 `../assets/js/nav.js` |
| 圖片無法顯示 | 檔名大小寫是否一致；頁面中的圖片路徑是否以 `../assets/images/` 開頭 |
| 網站還是舊內容 | 等待更新完成後重新整理，或加入網址參數，例如 `?v=2` |

## 不要做的事

請不要在任何 HTML、JavaScript、Markdown 或圖片檔名中放入 API Key、Token、密碼或私人資料。GitHub Pages 的內容是公開的。也不要手動修改 `pages.json`，因為系統會根據 HTML 頁面的設定重新產生它。

## 你的最短工作流程

> 複製 `templates/page-template.html` → 存成 `pages/你的檔名.html` → 改三個 `<meta>` → 寫 HTML → Commit changes → 在網站確認導覽列。
