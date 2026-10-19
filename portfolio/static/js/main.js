(()=>{
const d=document;d.documentElement.classList.remove('no-js');
d.getElementById('yr').textContent=new Date().getFullYear();
const m=d.querySelector('.menu'),n=d.querySelector('.nav nav');
if(m&&n){m.addEventListener('click',()=>{n.classList.toggle('open');m.setAttribute('aria-expanded',n.classList.contains('open'))});
n.addEventListener('click',e=>{if(e.target.tagName==='A')n.classList.remove('open')})}
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.1});
d.querySelectorAll('.reveal').forEach(el=>io.observe(el));
const h=d.querySelector('h1[data-type]');
if(h&&!matchMedia('(prefers-reduced-motion: reduce)').matches){const t=h.dataset.type;h.textContent='';let i=0;const s=setInterval(()=>{h.textContent=t.slice(0,++i);if(i>=t.length)clearInterval(s)},140)}
})();
