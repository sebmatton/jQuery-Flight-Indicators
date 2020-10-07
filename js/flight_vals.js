export function GetFlightVals(){

    // Check to see if the counter has been initialized
    if ( typeof increment == 'undefined' ) {
        // It has not... perform the initialization
        increment = 0;
    }

	var flight_vals = {
	heading_deg: 180+180*Math.sin(increment/25), 
    speed_knots: 80+80*Math.sin(increment/600), 
    pressure_Pa: 1000+3*Math.sin(increment/50), 
    altitude_ft: 1250+1250*Math.sin(increment/250), 
    roll_deg: 180*Math.sin(increment/50), 
    pitch_deg: 180*Math.sin(increment/50)
    };

    ++increment
  
  return flight_vals
}




