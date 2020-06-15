## Why balenaSense?
We wanted to simplify the method of building a DIY environmental monitoring application. With balenaSense, users can set up the application, assemble their hardware, and have their own remote-accessible dashboard to view their private environmental data.

## Is balenaSense free?
Yes! balenaSense requires you to sign up for a free [balenaCloud](https://dashboard.balena-cloud.com/signup) account. Your first 10 devices are always free and full-featured.

## Privacy: is balenaSense secure? 
balenaSense does not not depend on any type of cloud service to process or store environmental data. Your device will be running balenaOS which does communicate with balenaCloud to get application updates. This can be disabled however and won't affect your experience. Both [balenaSense](https://github.com/balenalabs/balena-sense/) and [balenaOS](https://github.com/balena-os) are open source projects, so feel free to check the source code if you want to know more about how they work!

## Does balenaSense need internet access?
You need an interent connection to access balenaCloud, set the project up on your device, and to update containers and code. However, the project should work "offline" on your local network. So long as proper credentials are set, and the device and its sensors are properly powered, they'll collect data and you can access the device's local URL.