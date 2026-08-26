/* Static Navigation Framework — renders the ordered page list generated from each HTML page's metadata. */
(async () => {
  const list = document.querySelector('[data-navigation-list]');
  if (!list) return;

  const normalizedPath = window.location.pathname === '/index.html' ? '/' : window.location.pathname;
  try {
    const response = await fetch('/pages.json', { cache: 'no-store' });
    if (!response.ok) throw new Error('pages.json could not be loaded');
    const { pages } = await response.json();
    pages.filter((page) => page.visible).forEach((page) => {
      const link = document.createElement('a');
      link.href = page.path;
      link.innerHTML = `<span>${String(page.order).padStart(2, '0')}</span>${page.title}`;
      if (page.path === normalizedPath) link.setAttribute('aria-current', 'page');
      list.appendChild(link);
    });
  } catch (error) {
    console.warn('Navigation list is not ready yet.', error);
  }
})();
