/* Field Notes Archive — only lightweight progressive enhancements; every page remains functional without JavaScript. */
document.querySelectorAll('img').forEach((image) => {
  image.addEventListener('error', () => {
    image.closest('figure, .image-link')?.classList.add('image-missing');
  });
});
