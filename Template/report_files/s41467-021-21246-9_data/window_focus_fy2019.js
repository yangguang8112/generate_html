(function(){/* 
 
 Copyright The Closure Library Authors. 
 SPDX-License-Identifier: Apache-2.0 
*/ 
'use strict';const f=Symbol("IS_REPEATED_FIELD");var g=Object,h=g.freeze,k=[];Array.isArray(k)&&!Object.isFrozen(k)&&(k[f]=!0);h.call(g,k);/* 
 
 SPDX-License-Identifier: Apache-2.0 
*/ 
function l(a,b,e){a.addEventListener&&a.addEventListener(b,e,!1)};function m(a,b,e){if(Array.isArray(b))for(var c=0;c<b.length;c++)m(a,String(b[c]),e);else null!=b&&e.push(a+(""===b?"":"="+encodeURIComponent(String(b))))};function n(a,b,e=null){p(a,b,e)}function p(a,b,e){a.google_image_requests||(a.google_image_requests=[]);const c=a.document.createElement("img");if(e){const d=A=>{e&&e(A);c.removeEventListener&&c.removeEventListener("load",d,!1);c.removeEventListener&&c.removeEventListener("error",d,!1)};l(c,"load",d);l(c,"error",d)}c.src=b;a.google_image_requests.push(c)};function q(a=null){return a&&"22"===a.getAttribute("data-jc")?a:document.querySelector('[data-jc="22"]')};var r=document,t=window;function u(a){return"undefined"!==typeof a}function v(a){l(r,a.h,()=>{if(r[a.g])a.i&&(a.i=!1,a.j=Date.now(),w(a,0));else{if(-1!==a.j){const b=Date.now()-a.j;0<b&&(a.j=-1,w(a,1,b))}w(a,3)}})}function x(a){l(t,"click",b=>{a.handleClick(b)})} 
function w(a,b,e=0){var c={gqid:a.m,qqid:a.o};0===b&&(c["return"]=0);1===b&&(c["return"]=1,c.timeDelta=e);2===b&&(c.bgload=1);3===b&&(c.fg=1);b=[];for(var d in c)m(d,c[d],b);n(t,a.l+"&label=window_focus&"+b.join("&"),void 0);if(!(.01<Math.random())){a=q(document.currentScript);a=`https://${"pagead2.googlesyndication.com"}/pagead/gen_204?id=jca&jc=${22}&version=${a&&a.getAttribute("data-jc-version")||"unknown"}&sample=${.01}`;c=window;if(d=c.navigator)d=c.navigator.userAgent,d=/Chrome/.test(d)&&!/Edge/.test(d)? 
!0:!1;d&&c.navigator.sendBeacon?c.navigator.sendBeacon(a):n(c,a)}} 
var z=class{constructor(){var a=y["gws-id"],b=y["qem-id"];this.l=y.url;this.m=a;this.o=b;this.i=!1;a=u(r.hidden)?{g:"hidden",h:"visibilitychange"}:u(r.mozHidden)?{g:"mozHidden",h:"mozvisibilitychange"}:u(r.msHidden)?{g:"msHidden",h:"msvisibilitychange"}:u(r.webkitHidden)?{g:"webkitHidden",h:"webkitvisibilitychange"}:{g:"hidden",h:"visibilitychange"};this.g=a.g;this.h=a.h;this.j=-1;r[this.g]&&w(this,2);v(this);x(this)}handleClick(){this.i=!0;t.setTimeout(()=>{this.i=!1},5E3)}};const B=q(document.currentScript);if(null==B)throw Error("JSC not found 22");var y;const C={},D=B.attributes;for(let a=D.length-1;0<=a;a--){const b=D[a].name;0===b.indexOf("data-jcp-")&&(C[b.substring(9)]=D[a].value)}y=C;window.window_focus_for_click=new z;}).call(this);
