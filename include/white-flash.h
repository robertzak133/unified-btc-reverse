// 
// white-flash-large-date.h
// 
// Prototypes for functions defined in white-flash-large-date.c


// Internally Defined Functions

void wf_setDigitalEffect(enum_digital_effect digital_effect,
			 unsigned int brightness_hue, unsigned int brightness,
			 unsigned int param_4);


extern void setDigitalEffect(enum_digital_effect digital_effect, ...);

extern void cp_setSensorDigitalEffectPhoto(char night_p);

extern void cp_setSensorDigitalEffectVideo(char night_p);

