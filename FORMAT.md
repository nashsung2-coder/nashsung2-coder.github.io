# HTML 頁面格式

這個網站的導覽列由每個 HTML 頁面開頭的三個中繼資料欄位決定。你只要新增一個 HTML 檔案、填好它們並提交，網站就會更新導覽順序；不需要修改導覽列，也不需要手動編輯 `pages.json`。

| 欄位 | 用途 | 範例 |
|---|---|---|
| `site-nav-title` | 導覽列顯示名稱 | `關於我` |
| `site-nav-order` | 排序數字；越小越靠左 | `20` |
| `site-nav-visible` | 是否顯示於導覽列 | `true` 或 `false` |

## 新增一頁

先在 GitHub 中把 `templates/page-template.html` 複製到 `pages/` 資料夾，例如建立 `pages/about.html`。接著只修改頁面最上方的格式設定與 `<main>` 內文。

```html
<meta name="site-nav-title" content="關於我" />
<meta name="site-nav-order" content="20" />
<meta name="site-nav-visible" content="true" />
```

排序建議使用 `10`、`20`、`30`。以後想在兩頁中間新增內容時，可直接使用 `15`，不必重排所有頁面。提交後，網站會自動更新 `pages.json`，導覽列隨即依新設定排列。

> **請保留**每個頁面的 `<header ... data-site-navigation>`、`<nav ... data-navigation-list>` 和最下方的 `nav.js`。它們是共用導覽列的必要部分。

## 檔案位置

| 目的 | 路徑 |
|---|---|
| 首頁 | `index.html` |
| 新增的公開頁面 | `pages/你的檔名.html` |
| 可以複製的格式檔 | `templates/page-template.html` |
| 導覽列樣式 | `assets/css/site.css` |
| 導覽列程式 | `assets/js/nav.js` |
| 自動產生的頁面清單 | `pages.json`，請不要手動編輯 |
