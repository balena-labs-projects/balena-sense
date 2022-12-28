"use strict";(self.webpackChunkbalena_labs=self.webpackChunkbalena_labs||[]).push([[805],{3905:(e,t,r)=>{r.d(t,{Zo:()=>c,kt:()=>f});var a=r(7294);function n(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,a)}return r}function s(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){n(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t){if(null==e)return{};var r,a,n=function(e,t){if(null==e)return{};var r,a,n={},o=Object.keys(e);for(a=0;a<o.length;a++)r=o[a],t.indexOf(r)>=0||(n[r]=e[r]);return n}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)r=o[a],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(n[r]=e[r])}return n}var i=a.createContext({}),u=function(e){var t=a.useContext(i),r=t;return e&&(r="function"==typeof e?e(t):s(s({},t),e)),r},c=function(e){var t=u(e.components);return a.createElement(i.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},d=a.forwardRef((function(e,t){var r=e.components,n=e.mdxType,o=e.originalType,i=e.parentName,c=l(e,["components","mdxType","originalType","parentName"]),d=u(r),f=n,h=d["".concat(i,".").concat(f)]||d[f]||p[f]||o;return r?a.createElement(h,s(s({ref:t},c),{},{components:r})):a.createElement(h,s({ref:t},c))}));function f(e,t){var r=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var o=r.length,s=new Array(o);s[0]=d;var l={};for(var i in t)hasOwnProperty.call(t,i)&&(l[i]=t[i]);l.originalType=e,l.mdxType="string"==typeof e?e:n,s[1]=l;for(var u=2;u<o;u++)s[u]=r[u];return a.createElement.apply(null,s)}return a.createElement.apply(null,r)}d.displayName="MDXCreateElement"},8140:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>i,contentTitle:()=>s,default:()=>p,frontMatter:()=>o,metadata:()=>l,toc:()=>u});var a=r(7462),n=(r(7294),r(3905));const o={},s="Usage",l={unversionedId:"usage",id:"usage",title:"Usage",description:"Verify that all services are working",source:"@site/docs/02-usage.md",sourceDirName:".",slug:"/usage",permalink:"/balena-sense/usage",draft:!1,editUrl:"https://github.com/balena-labs-projects/balena-sense/edit/master/docs/02-usage.md",tags:[],version:"current",sidebarPosition:2,frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Getting Started",permalink:"/balena-sense/"},next:{title:"Customization",permalink:"/balena-sense/customization"}},i={},u=[{value:"Verify that all services are working",id:"verify-that-all-services-are-working",level:2},{value:"Accessing your dashboard",id:"accessing-your-dashboard",level:2},{value:"As part of an Open Fleet",id:"as-part-of-an-open-fleet",level:3},{value:"As your own fleet or forked setup on balenaCloud",id:"as-your-own-fleet-or-forked-setup-on-balenacloud",level:3},{value:"Dashboard",id:"dashboard",level:2}],c={toc:u};function p(e){let{components:t,...r}=e;return(0,n.kt)("wrapper",(0,a.Z)({},c,r,{components:t,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"usage"},"Usage"),(0,n.kt)("h2",{id:"verify-that-all-services-are-working"},"Verify that all services are working"),(0,n.kt)("p",null,(0,n.kt)("img",{parentName:"p",src:"https://assets.balena.io/blog-common/2021/07/sensev2-services.png",alt:null})),(0,n.kt)("p",null,"After following all of the instructions on ",(0,n.kt)("a",{parentName:"p",href:"/balena-sense/"},"Getting Started"),", ensure all the services are running on your device."),(0,n.kt)("p",null,"If everything worked out correctly, after a few minutes your device information screen in the dashboard should look something like this, showing the services running, one for each of the software components. (If not, check out our ",(0,n.kt)("a",{parentName:"p",href:"https://www.balena.io/docs/faq/troubleshooting/troubleshooting/"},"troubleshooting guide")," or head over to ",(0,n.kt)("a",{parentName:"p",href:"https://forums.balena.io/"},"the forums")," where we can help you out.)"),(0,n.kt)("h2",{id:"accessing-your-dashboard"},"Accessing your dashboard"),(0,n.kt)("h3",{id:"as-part-of-an-open-fleet"},"As part of an Open Fleet"),(0,n.kt)("p",null,"If you added your device to the balenaSense Open Fleet, you can access your dashboard locally by visiting ",(0,n.kt)("inlineCode",{parentName:"p"},"http://balena.local")," in your browser."),(0,n.kt)("h3",{id:"as-your-own-fleet-or-forked-setup-on-balenacloud"},"As your own fleet or forked setup on balenaCloud"),(0,n.kt)("p",null,(0,n.kt)("img",{parentName:"p",src:"https://assets.balena.io/blog-common/2021/07/sensev2-addresses.png",alt:null})),(0,n.kt)("p",null,"If you're using balenaSense on a device on balenaCloud, you can use the built-in VPN and remote URL to access your device's dashboard remotely. You can access this URL from anywhere where you have internet access."),(0,n.kt)("p",null,"If you don\u2019t want to enable the public device access, you can still view the dashboard from within your own local network by using the IP address value from the image above (green encircled area.) Yours will be different, but if you enter http://your-ip-address into a browser, you\u2019ll still be able to access the dashboard as long as you\u2019re on the same network as the device. For example, to access my device I would use ",(0,n.kt)("a",{parentName:"p",href:"http://192.168.1.251"},"http://192.168.1.251"),"."),(0,n.kt)("p",null,"Remember that if you have multiple devices running balenaSense, you'll want to keep track of which IP is for which setup."),(0,n.kt)("h2",{id:"dashboard"},"Dashboard"),(0,n.kt)("p",null,"Assuming your sensor is set up properly, and data is being collected and presented by various blocks, you should be able to access the default dashboard using one of the methods above. You'll see something like this:"),(0,n.kt)("p",null,(0,n.kt)("img",{parentName:"p",src:"https://assets.balena.io/blog-common/2021/07/sensev2-grafana-1.png",alt:null})),(0,n.kt)("p",null,"If you want to customize your dashboard, you'll want to sign into Grafana. The default username and password for your device is ",(0,n.kt)("inlineCode",{parentName:"p"},"admin"),"."),(0,n.kt)("p",null,"Follow our ",(0,n.kt)("a",{parentName:"p",href:"https://www.balena.io/blog/balenasense-v2-updated-temperature-pressure-and-humidity-monitoring-for-raspberry-pi/"},"official project guide")," for detailed instructions on how to do this."))}p.isMDXComponent=!0}}]);