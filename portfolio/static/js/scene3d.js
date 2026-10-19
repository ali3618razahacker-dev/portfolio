(()=>{
const c=document.getElementById('scene'),root=document.documentElement;
const fail=()=>root.classList.add('no-webgl');
if(!c||typeof THREE==='undefined')return fail();
let r;try{r=new THREE.WebGLRenderer({canvas:c,antialias:true,alpha:true})}catch(e){return fail()}
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const sc=new THREE.Scene(),cam=new THREE.PerspectiveCamera(50,1,.1,100);cam.position.z=7;
r.setPixelRatio(Math.min(devicePixelRatio,2));
sc.add(new THREE.AmbientLight(0x6688aa,.6));
const l1=new THREE.PointLight(0x22d3ee,2,30);l1.position.set(4,4,5);sc.add(l1);
const l2=new THREE.PointLight(0x8b5cf6,2,30);l2.position.set(-4,-3,4);sc.add(l2);
const g=new THREE.Group();sc.add(g);
const chip=new THREE.Mesh(new THREE.BoxGeometry(2.2,2.2,.35),new THREE.MeshStandardMaterial({color:0x0a1124,metalness:.8,roughness:.3,emissive:0x0b3a4a}));g.add(chip);
chip.add(new THREE.LineSegments(new THREE.EdgesGeometry(chip.geometry),new THREE.LineBasicMaterial({color:0x22d3ee})));
const pm=new THREE.MeshStandardMaterial({color:0x34d399,emissive:0x0f5c42});
for(let i=-3;i<=3;i++)for(const s of[-1,1]){const p=new THREE.Mesh(new THREE.BoxGeometry(.12,.35,.06),pm);p.position.set(i*.28,s*1.4,0);chip.add(p);const q=new THREE.Mesh(new THREE.BoxGeometry(.35,.12,.06),pm);q.position.set(s*1.4,i*.28,0);chip.add(q)}
const ico=new THREE.Mesh(new THREE.IcosahedronGeometry(3.1,1),new THREE.MeshBasicMaterial({color:0x8b5cf6,wireframe:true,transparent:true,opacity:.35}));g.add(ico);
const cubes=[];for(let i=0;i<8;i++){const m=new THREE.Mesh(new THREE.BoxGeometry(.3,.3,.3),new THREE.MeshStandardMaterial({color:i%2?0x22d3ee:0x34d399,emissive:0x112233}));m.userData={a:i/8*Math.PI*2,s:.3+Math.random()*.4};g.add(m);cubes.push(m)}
const N=150,pos=new Float32Array(N*3);for(let i=0;i<N*3;i++)pos[i]=(Math.random()-.5)*14;
const pg=new THREE.BufferGeometry();pg.setAttribute('position',new THREE.BufferAttribute(pos,3));
sc.add(new THREE.Points(pg,new THREE.PointsMaterial({color:0x22d3ee,size:.04})));
const mouse={x:0,y:0};addEventListener('pointermove',e=>{mouse.x=e.clientX/innerWidth-.5;mouse.y=e.clientY/innerHeight-.5});
function size(){const w=c.clientWidth,h=c.clientHeight;if(!w||!h)return;r.setSize(w,h,false);cam.aspect=w/h;cam.updateProjectionMatrix()}
addEventListener('resize',size);size();
let t=0,raf=0,vis=true;
new IntersectionObserver(e=>{vis=e[0].isIntersecting;go()}).observe(c);
document.addEventListener('visibilitychange',go);
function frame(){raf=0;t+=.01;
 g.rotation.y+=(mouse.x*1.2+t*.3-g.rotation.y)*.04;g.rotation.x+=(mouse.y*.8-g.rotation.x)*.05;
 ico.rotation.y=t*.2;cubes.forEach(m=>{const a=m.userData.a+t*m.userData.s;m.position.set(Math.cos(a)*3.1,Math.sin(a*1.3)*1.6,Math.sin(a)*1.5);m.rotation.x=m.rotation.y=a});
 r.render(sc,cam);go()}
function go(){if(!raf&&vis&&!document.hidden&&!reduce)raf=requestAnimationFrame(frame)}
r.render(sc,cam);go();
})();
