#ifndef __PLATFORM_CONFIG__
#define __PLATFORM_CONFIG__

#include "ota.h"

#define PORT_PROVIDE_RANDOM FALSE
#define UID_BYTES   6

/*====== DRIVER MAPPING ================================================== */


#define EXT_SLOTS EXT_INTERRUPTS_NEEDED


/*====== PORT HOOKS ================================================ */

#define PORT_BLINK_FN() \
void _port_blink(int vpin,int n,int ms){            \
    int i;                                          \
    for (i=0;i<n;i++){                              \
        vosThSleep(TIME_U(ms/2,MILLIS));            \
        vosThSleep(TIME_U(ms/2,MILLIS));            \
    }                                               \
}

#define PORT_PRE_UPLOAD_HOOK() 
#define PORT_AFTER_UPLOAD_HOOK() vosThSleep(TIME_U(500,MILLIS))

#define PORT_LED_CONFIG()
#define PORT_LED_ON() 
#define PORT_LED_OFF() 
#define PORT_BLINK_ONE()                _port_blink(LED0,1,10);
#define PORT_BLINK_PRE_UPLOAD()         _port_blink(LED0,1,100);
#define PORT_BLINK_PRE_UPLOAD_OK()      _port_blink(LED0,2,500);
#define PORT_BLINK_AFTER_UPLOAD_OK()    _port_blink(LED0,2,500);
#define PORT_BLINK_AFTER_UPLOAD_KO()    _port_blink(LED0,2,500);

void port_main_hook(void);

#endif