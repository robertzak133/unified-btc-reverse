// 
// white-flash-large-date.h
// 
// Prototypes for functions defined in white-flash-large-date.c


// Internally Defined Functions

void wfl_setSensorDigitalEffectPhoto(byte night_p);
void wfl_setSensorDigitalEffectVideo(byte night_p);
void wfl_spawnIRCutFSM_per_mode(void);



#if  (defined BTC_7A_OLD) 
void cp_setSensorDigitalEffectPhoto(byte night_p,uint param_2,uint param_3,uint param_4);
void cp_setSensorDigitalEffectVideo(byte night_p,uint param_2,uint param_3,uint param_4);
#elif (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4) || (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
extern void cp_setSensorDigitalEffectPhoto(char night_p);
extern void cp_setSensorDigitalEffectVideo(char night_p);

#endif
