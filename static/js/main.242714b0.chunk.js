(this["webpackJsonpadvice-app"]=this["webpackJsonpadvice-app"]||[]).push([[0],{47:function(t,e,n){t.exports=n(57)},52:function(t,e,n){},57:function(t,e,n){"use strict";n.r(e);var r=n(0),a=n.n(r),o=n(10),i=n.n(o),s=n(30),l=n(96),c=n(95),g=(n(52),n(35)),u=n.n(g);var p=Object.values(function(){var t;return u.a.ajax({url:"https://murat-db-20-default-rtdb.firebaseio.com/.json",dataType:"json",type:"GET",async:!1,success:function(e){t=e},error:function(e){throw console.log("Errorlog: Response: ",e),t=e,new Error("Error during loading of all songs")}}),t}());p.sort((function(t,e){return function(t,e,n){var r=t[n].toUpperCase(),a=e[n].toUpperCase();return r<a?-1:r>a?1:0}(t,e,"song_title")}));var f=function(){var t=Object(r.useState)({song_title:""}),e=Object(s.a)(t,2),n=e[0],o=e[1],i=Object(r.useState)([{song_title:""},{song_title:""},{song_title:""}]),g=Object(s.a)(i,2),u=g[0],f=g[1];console.log(p);var h=function(){var t=function(t){var e=[];p.forEach((function(n){var r=0;n.song_title!=t.song_title&&function(t,e){for(var n=0;n<t.length;n++)for(var r=0;r<e.length;r++)if(t[n]===e[r])return!0;return!1}(n.song_genre,t.song_genre)?(r+=Math.abs(n.happy-t.happy),r+=Math.abs(n.angry-t.angry),r+=Math.abs(n.surprise-t.surprise),r+=Math.abs(n.sad-t.sad),r+=Math.abs(n.fear-t.fear)):r=1e11,e.push(r)}));for(var n=[],r=0,a=p.slice(0,-1),o=0;o<3;o++)r=e.indexOf(Math.min.apply(Math,e)),n.push(a.splice(r,1)[0]);return n}(function(t,e){for(var n=0;n<e.length;n++)if(e[n].song_title===t.song_title)return e[n]}(n,p));f(t)};return a.a.createElement("div",{className:"App",style:{textAlign:"center"}},a.a.createElement("h1",{style:{textAlign:"center"}},"Songtiteleingabe:"),a.a.createElement(l.a,{id:"combo-box-demo",options:p,getOptionLabel:function(t){return t.song_title},renderInput:function(t){return a.a.createElement(c.a,Object.assign({},t,{label:"Song",variant:"outlined"}))},style:{width:300,marginLeft:"auto",marginRight:"auto"},onChange:function(t){o({song_title:t.target.innerHTML})}}),a.a.createElement("button",{onClick:function(){h()},style:{marginTop:50,width:300,marginLeft:"auto",marginRight:"auto",marginBottom:50}},"Vorschlag generieren"),a.a.createElement("p",{style:{textAlign:"center",fontWeight:"bold"}},"Songvorschlag:"),a.a.createElement("p",{style:{textAlign:"center"}},u[0].song_title),a.a.createElement("p",{style:{textAlign:"center"}},u[1].song_title),a.a.createElement("p",{style:{textAlign:"center"}},u[2].song_title))};i.a.render(a.a.createElement(f,null),document.getElementById("root"))}},[[47,1,2]]]);
//# sourceMappingURL=main.242714b0.chunk.js.map