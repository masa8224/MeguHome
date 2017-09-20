#light() = [front] | [back];
@results 
	0 {'front'}
	1 {'back'}
@
#home() = (home | going);
#hours() = (one | two | three | four | five | six | seven | eight | nine | ten | eleven | twelve);
#ampm() = (am | pm);
#days() = (today | tomorrow);
#onOff() = [on] | [off];
@results
	0 {'on'}
	1 {'off'}
@
#me() = (i);
#turn() = (turn);

[megumi] #turn (the)? #light (light)? (to)? #onOff;
@results
	#light, #onOff {#onOff'("'#light'")'}
@
[megumi] #turn #onOff (the)? #light (light)?;
@results
	#light, #onOff {#onOff'("'#light'")'}
@
[megumi] (set alarm)* (at)? #hours #ampm #days;
@results
	#hours, #ampm, #days {'print "'#hours','#ampm','#days'"'}
@
[megumi] #me (am)? #home;
@results
	0 {'Iam("'#home'")'}
@
[megumi] [quit | stop | exit];
@results
	0 {'quit()'}
@
[megumi] [search | custom];
@results
	0 {'print "search"'}
@
[deactivate voice recongintion];
@results
	0 {'ignore(True)'}
@
[activate voice recongintion];
@results
	0 {'ignore(False)'}
@
[megumi];
@results
	0 {'print "Hai!"'}
@