#ifndef __BOARD_MCU__
#define __BOARD_MCU__



#define EXT_INTERRUPTS_NEEDED   16



//VHAL Drivers
#define VHAL_GPIO 1
#define VHAL_EXT 1
#define VHAL_SER 1
#define VHAL_NFO 1
#define VHAL_FLASH 1
#define VHAL_RNG 1
#define BOARD_HAS_RNG   1


#define SERIAL0_RX_PIN  3
#define SERIAL0_TX_PIN  1
#define SERIAL0_RT_PIN  -1
#define SERIAL0_CT_PIN  -1

#define SERIAL1_RX_PIN  0
#define SERIAL1_TX_PIN  25
#define SERIAL1_RT_PIN  -1
#define SERIAL1_CT_PIN  -1

#define SERIAL2_RX_PIN  16
#define SERIAL2_TX_PIN  17
#define SERIAL2_RT_PIN  -1
#define SERIAL2_CT_PIN  -1


#endif