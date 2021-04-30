document.querySelectorAll('.tabs-header__label').forEach((el) => {
  el.addEventListener('click', () => {
    console.log(el);
    let oldStep = document.querySelector('.tabs-header__input:checked').value;
    let newStep = el.dataset.step;
    if (oldStep != newStep) {
      document
        .querySelector(`#work-step-${oldStep}`)
        .classList.remove('work-step-item_active');
      document
        .querySelector(`#work-step-${newStep}`)
        .classList.add('work-step-item_active');
    }
  });
});

document.querySelector('.nav-toggler').addEventListener('click', () => {
  document.querySelector('.nav-list').classList.toggle('nav-list_expanded');
});

function simpleParallax (elem, modifier) {
  let paras = document.querySelectorAll(elem);
  // for (let i = 0; i < paras.length; i++) {
  // }
  const sp = () => {
      for (let i = 0; i < paras.length; i++) {
          let x = paras[i].getBoundingClientRect().top / modifier;
          let y = Math.round(x * 100) / 100;
          paras[i].style.backgroundPosition = 'center ' + y + 'px';
      }
      requestAnimationFrame(sp);
  }
  requestAnimationFrame(sp);
}

simpleParallax('#heroBg', 15)
