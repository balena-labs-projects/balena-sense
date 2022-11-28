# Customization

## Adding support for various sensors

We encourage contributors to add code to extend our supported sensors. Please review [existing issues](https://github.com/balena-labs-projects/balena-sense/issues) to see which sensors and types are currently being worked on. We'll eventually build a list of compatible sensors.

## Multiple sensors

![](https://assets.balena.io/blog-common/2021/07/sensev2-data.png)

Using I2C, you can "daisy chain" multiple sets of I2C sensors together, or use multiple devices with balenaSense to aggregate data. See our official project guide's section on [data aggregation](https://www.balena.io/blog/balenasense-v2-updated-temperature-pressure-and-humidity-monitoring-for-raspberry-pi/#data) to learn more about this and the [sensor block](https://github.com/balena-labs-projects/sensor).

## Customizing your Grafana dashboard

![](https://assets.balena.io/blog-common/2021/07/sensev2-grafana-4.png)

While the stock/default dashboard is a helpful way to start, you'll probably want to customize your own visualizations at some point. Please follow [this subsection](https://www.balena.io/blog/balenasense-v2-updated-temperature-pressure-and-humidity-monitoring-for-raspberry-pi/#dashboard) of our project guide for dashboard customization.

If you have a favorite way to customize your balenaSense dashboard, feel free to [contribute](https://github.com/balena-labs-projects/balena-sense) to this documentation.
