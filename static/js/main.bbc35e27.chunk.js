(this["webpackJsonpadvice-app"]=this["webpackJsonpadvice-app"]||[]).push([[0],{49:function(e,n,t){e.exports=t(59)},54:function(e,n,t){},59:function(e,n,t){"use strict";t.r(n);var o=t(0),a=t.n(o),r=t(9),l=t.n(r),c=t(31),s=t(98),i=t(97),u=(t(54),t(36)),p=t.n(u);var g=function(){var e=Object(o.useState)(""),n=Object(c.a)(e,2),t=n[0],r=n[1],l=Object(o.useState)({title:""}),u=Object(c.a)(l,2),g=u[0],f=u[1],d=Object.values(function(){var e;return p.a.ajax({url:"https://murat-db-default-rtdb.europe-west1.firebasedatabase.app/songs.json",dataType:"json",type:"GET",async:!1,success:function(n){console.log(n),e=n},error:function(n){throw console.log("Errorlog: Response: ",n),e=n,new Error("Error during loading of all songs")}}),e}());console.log(d),Array.min=function(e){return Math.min.apply(Math,e)};var b=function(){var e=function(e){console.log("im getSuggestions:"),console.log(e);var n=[];console.log("start error calculation"),d.forEach((function(t){console.log("forEach");var o=0;o+=t.happy-e.happy,o+=t.angry-e.angry,o+=t.surprise-e.surprise,o+=t.sad-e.sad,o+=t.fear-e.fear,n.push(o)}));var t=Math.min.apply(Math,n),o=n.indexOf(t);return d[o]}(function(e,n){for(var t=0;t<n.length;t++)if(n[t].title===e)return n[t]}(t,d));f(e),r(""),console.log("generateSuffestion fetr")};return console.log(g),console.log(t),a.a.createElement("div",{className:"App"},a.a.createElement("h1",null,"Songtiteleingabe:"),a.a.createElement(s.a,{id:"combo-box-demo",options:d,getOptionLabel:function(e){return e.title},style:{width:300},renderInput:function(e){return a.a.createElement(i.a,Object.assign({},e,{label:"Combo box",variant:"outlined"}))},onChange:function(e){r(e.target.innerHTML)}}),a.a.createElement("button",{onClick:function(){b()}},"Vorschlag generieren"),a.a.createElement("p",null,"Songvorschlag:"),a.a.createElement("p",null,g.title))};l.a.render(a.a.createElement(g,null),document.getElementById("root"))}},[[49,1,2]]]);
//# sourceMappingURL=main.bbc35e27.chunk.js.map