"use strict";(self.webpackChunkbalena_labs_docs=self.webpackChunkbalena_labs_docs||[]).push([[368],{3905:(e,t,r)=>{r.d(t,{Zo:()=>p,kt:()=>m});var a=r(7294);function n(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,a)}return r}function s(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){n(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function i(e,t){if(null==e)return{};var r,a,n=function(e,t){if(null==e)return{};var r,a,n={},o=Object.keys(e);for(a=0;a<o.length;a++)r=o[a],t.indexOf(r)>=0||(n[r]=e[r]);return n}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)r=o[a],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(n[r]=e[r])}return n}var l=a.createContext({}),u=function(e){var t=a.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):s(s({},t),e)),r},p=function(e){var t=u(e.components);return a.createElement(l.Provider,{value:t},e.children)},c={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},d=a.forwardRef((function(e,t){var r=e.components,n=e.mdxType,o=e.originalType,l=e.parentName,p=i(e,["components","mdxType","originalType","parentName"]),d=u(r),m=n,b=d["".concat(l,".").concat(m)]||d[m]||c[m]||o;return r?a.createElement(b,s(s({ref:t},p),{},{components:r})):a.createElement(b,s({ref:t},p))}));function m(e,t){var r=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var o=r.length,s=new Array(o);s[0]=d;var i={};for(var l in t)hasOwnProperty.call(t,l)&&(i[l]=t[l]);i.originalType=e,i.mdxType="string"==typeof e?e:n,s[1]=i;for(var u=2;u<o;u++)s[u]=r[u];return a.createElement.apply(null,s)}return a.createElement.apply(null,r)}d.displayName="MDXCreateElement"},331:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>l,contentTitle:()=>s,default:()=>c,frontMatter:()=>o,metadata:()=>i,toc:()=>u});var a=r(7462),n=(r(7294),r(3905));const o={},s="Customization",i={unversionedId:"customization",id:"customization",title:"Customization",description:"Adding support for various sensors",source:"@site/../docs/03-customization.md",sourceDirName:".",slug:"/customization",permalink:"/balena-sense/customization",draft:!1,editUrl:"https://github.com/balena-labs-projects/balena-sense/edit/master/../docs/03-customization.md",tags:[],version:"current",sidebarPosition:3,frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Usage",permalink:"/balena-sense/usage"},next:{title:"Supported devices",permalink:"/balena-sense/device-support"}},l={},u=[{value:"Adding support for various sensors",id:"adding-support-for-various-sensors",level:2},{value:"Multiple sensors",id:"multiple-sensors",level:2},{value:"Customizing your Grafana dashboard",id:"customizing-your-grafana-dashboard",level:2}],p={toc:u};function c(e){let{components:t,...r}=e;return(0,n.kt)("wrapper",(0,a.Z)({},p,r,{components:t,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"customization"},"Customization"),(0,n.kt)("h2",{id:"adding-support-for-various-sensors"},"Adding support for various sensors"),(0,n.kt)("p",null,"We encourage contributors to add code to extend our supported sensors. Please review ",(0,n.kt)("a",{parentName:"p",href:"https://github.com/balena-labs-projects/balena-sense/issues"},"existing issues")," to see which sensors and types are currently being worked on. We'll eventually build a list of compatible sensors."),(0,n.kt)("h2",{id:"multiple-sensors"},"Multiple sensors"),(0,n.kt)("p",null,(0,n.kt)("img",{parentName:"p",src:"https://assets.balena.io/blog-common/2021/07/sensev2-data.png",alt:null})),(0,n.kt)("p",null,'Using I2C, you can "daisy chain" multiple sets of I2C sensors together, or use multiple devices with balenaSense to aggregate data. See our official project guide\'s section on ',(0,n.kt)("a",{parentName:"p",href:"https://www.balena.io/blog/balenasense-v2-updated-temperature-pressure-and-humidity-monitoring-for-raspberry-pi/#data"},"data aggregation")," to learn more about this and the ",(0,n.kt)("a",{parentName:"p",href:"https://github.com/balena-labs-projects/sensor"},"sensor block"),"."),(0,n.kt)("h2",{id:"customizing-your-grafana-dashboard"},"Customizing your Grafana dashboard"),(0,n.kt)("p",null,(0,n.kt)("img",{parentName:"p",src:"https://assets.balena.io/blog-common/2021/07/sensev2-grafana-4.png",alt:null})),(0,n.kt)("p",null,"While the stock/default dashboard is a helpful way to start, you'll probably want to customize your own visualizations at some point. Please follow ",(0,n.kt)("a",{parentName:"p",href:"https://www.balena.io/blog/balenasense-v2-updated-temperature-pressure-and-humidity-monitoring-for-raspberry-pi/#dashboard"},"this subsection")," of our project guide for dashboard customization."),(0,n.kt)("p",null,"If you have a favorite way to customize your balenaSense dashboard, feel free to ",(0,n.kt)("a",{parentName:"p",href:"https://github.com/balena-labs-projects/balena-sense"},"contribute")," to this documentation."))}c.isMDXComponent=!0}}]);