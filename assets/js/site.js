/* Field Notes Archive — mobile navigation is the only enhancement; the page remains usable without JavaScript. */
const menuToggle = document.getElementById('menu-toggle');
const mobileNav = document.getElementById('mobile-nav');
if (menuToggle && mobileNav) {
  menuToggle.addEventListener('click', () => {
    const open = mobileNav.classList.toggle('open');
    menuToggle.textContent = open ? '×' : '☰';
    menuToggle.setAttribute('aria-label', open ? '關閉選單' : '開啟選單');
  });
  mobileNav.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
    mobileNav.classList.remove('open');
    menuToggle.textContent = '☰';
    menuToggle.setAttribute('aria-label', '開啟選單');
  }));
}
