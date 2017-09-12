#light() = [front] | [back];
@results 
	0 {'front'}
	1 {'back'}
@
#home() = (home | out);

#onOff() = [on] | [off];
@results
	0 {'on'}
	1 {'off'}
@
#me() = (i);
#turn() = (turn);

#turn (the)? #light (light)? (to)? #onOff;
@results
	#light, #onOff {#onOff ' ' #light}
@

#me (am)? #home;
@results
	#home {'I am ' #home}
@

