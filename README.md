jQuery Flight Indicators
===================

"Flight Indicators" gives the ability to display web based flight indicator using html, css3, jQuery and SVG. Currently supported indicators are :
* Attitude (artificial horizon)
* Heading 
* Vertical speed
* Air speed
* Altimeter

Example & Demo
-------------------
![demo](https://raw.githubusercontent.com/sebmatton/jQuery-Flight-Indicators/master/example.png "demo")

Demo can be found here : [http://sebmatton.github.io/flightindicators/](http://sebmatton.github.io/flightindicators/)

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
	size : 200,
	roll : 0,
	pitch : 0,
	heading: 0,
	vario: 0,
	airspeed: 0,
	altitude: 0,
	pressure: 1000,
	showBox : true,
	img_directory : 'img/'
}
```

##### Size
The `size` option sets the size in pixels of the indicator.

##### Roll
The `roll` option sets the roll angle in degrees for an attitude indicator.

##### Pitch
The `pitch` option sets the pitch angle in degrees for an attitude indicator.

##### Heading
The `heading` option sets the heading angle in degrees for an heading indicator.

##### Vario
The `vario` option sets the variometer value in 1000 feets per minute for the variometer indicator !

##### Airspeed
The `airspeed` option sets the air speed angle knots for an air speed indicator.

##### Altitude
The `altitude` option sets the altitude in feets for an altimeter indicator.

##### Pressure
The `pressure` option sets the pressure in hpa for an altimeter indicator.

##### ShowBox
The `showBox` option sets if the outer squared box is visible or not. It may only take the value `true` of `false`.

##### img_directory
the `img_directory` option sets the directory where the images are saved. The default value is `img/` directory.

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
Hi ! I'm Sebastien Matton and I'm from Belgium. This project was initialy developped for an engineering project during my Master's Thesis. Feel free to use it.

Thanks
---------
Thanks to igneosaur for work on which this project was initialy based ([Project on Bitbucket](https://bitbucket.org/igneosaur/attitude-indicator))