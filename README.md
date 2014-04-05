Flight Indicators jQuery plugin [![GitHub version](https://badge.fury.io/gh/sebmatton%2FjQuery-Flight-Indicators.svg)](http://badge.fury.io/gh/sebmatton%2FjQuery-Flight-Indicators) 
===================

The Flight Indicators Plugin allows you to display high quality flight indicators using html, css3, jQuery and SVG images. The methods make customization and real time implementation really easy. Further, since all the images are vector svg you can resize the indicators to your application without any quality loss ! 

Currently supported indicators are :

* Attitude (artificial horizon)
* Heading 
* Vertical speed
* Air speed
* Altimeter

Example & Demo
-------------------
Demo can be found here : [http://sebmatton.github.io/flightindicators/](http://sebmatton.github.io/flightindicators/)

Here are a few examples of currently implemented indicators :

![demo_example](https://raw.githubusercontent.com/sebmatton/jQuery-Flight-Indicators/master/_examples_data/example.png "Indicator examples")

The image below shows a part of an 800px indicator. Vector images allows you to keep high quality render with large indicators.

![demo_highres](https://raw.githubusercontent.com/sebmatton/jQuery-Flight-Indicators/master/_examples_data/example_highres.png "High resolution indicator")

Usage
-------------------
### Initialization
To use this plugin you need to import the css file in the head of your html file :

```html
<link rel="stylesheet" type="text/css" href="css/flightindicators.css" />
```

Before the `</body>` tag, include jQuery and this plugin :

```html
<script src="js/jquery.js"></script>
<script src="js/jquery.flightindicator.js"></script>
```

### Using the plugin
Create a `<span>` section to put an indicator in :

```html
<span id="attitude"></span>
```

Then, when the span is ready in the DOM (maybe you need to wait for document ready), you can run the indicator function :

```js
var indicator = $.flightIndicator('#attitude', type, options);
```
Where the first argument is the selector, the type value specify the indicator type and the options overwrite the default settings.

To display the most simple indicator, as for example the attitude indicator, we use :

```js
var indicator = $.flightIndicator('#attitude', 'attitude');
```

The type may be `attitude`, `heading`, `variometer`, `airspeed` or `altimeter`. If the type is not correct, the default type will be attitude.

Initial settings can be modified using the `options` parameter. Here are the valid options and the default settings :

```js
var options = {
	size : 200,				// Sets the size in pixels of the indicator (square)
	roll : 0,				// Roll angle in degrees for an attitude indicator
	pitch : 0,				// Pitch angle in degrees for an attitude indicator
	heading: 0,				// Heading angle in degrees for an heading indicator
	vario: 0,				// Variometer in 1000 feets/min for the variometer indicator
	airspeed: 0,			// Air speed in knots for an air speed indicator
	altitude: 0,			// Altitude in feets for an altimeter indicator
	pressure: 1000,			// Pressure in hPa for an altimeter indicator
	showBox : true,			// Sets if the outer squared box is visible or not (true or false)
	img_directory : 'img/'	// The directory where the images are saved to
}
```

The options parameters are optionnals.

### Updating the indicator informations
Some methods are used to update the indicators, giving the opportunity to create realtime GUI !

The way to use it is really simple.

```js
var attitude = $.flightIndicator('#attitude', 'attitude');
attitude.setRoll(30); // Sets the roll to 30 degrees
```

Here are the valid methods :

```js
indicator.setRoll(roll);			// Sets the roll of an attitude indicator
indicator.setPitch(pitch);			// Sets the pitch of an attitude indicator
indicator.setHeading(heading);		// Sets the heading of an heading indicator
indicator.setVario(vario);			// Sets the climb speed of an variometer indicator
indicator.setAirSpeed(speed);		// Sets the speed of an airspeed indicator
indicator.setAltitude(altitude);	// Sets the altitude of an altimeter indicator
indicator.setPressure(pressure);	// Sets the pressure of an altimeter indicator
indicator.resize(size);				// Sets the size of any indicators
indicator.showBox();				// Make the outer squared box of any instrument visible
indicator.hideBox();				// Make the outer squared box of any instrument invisible
```

Author and License
-----------
Author : Sébastien Matton (seb_matton@hotmail.com)

jQuery Flight Indicators plugin was developped as part of my Master's Thesis since I needed a realtime interface showing the flight datas about for a quadcopter.

The project is published under GPLv3 License. See LICENSE file for more informations

Feel free to take part in this project or/and contact me for any reason :-)


Thanks
---------
Thanks to igneosaur for work on which this project was initialy based ([Project on Bitbucket](https://bitbucket.org/igneosaur/attitude-indicator))