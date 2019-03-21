#ifndef _1WIRE_
#define _1WIRE_

#include "stm32f30x.h"
 #include <stdint.h>
#include "main.h"
//#define BOOL uint8_t

//#ifndef FALSE

//#define FALSE 0
//#define TRUE  1

//#endif


/* Private variables ---------------------------------------------------------*/


#define SKIPROM 1    //set this to 1 if only one device is on the onewire bus else make it 0

#define CommandReadMemory					0xF0
#define CommandCopyScratchpad			0x55
#define CommandReadScratchpad			0xAA
#define CommandWriteScratchpad		0x0F
#define CommandSkipRom 						0xCC
#define CommandReadRom 						0x33
#define CommandMatchRom 					0x55
#define CommandSearchRom 					0xF0
#define CommandResume 						0xA5
#define CommandOverdriveSkipRom 	0x3C
#define CommandOverdriveMatchRom 	0x69


typedef enum {ReadWrite = 1 , ResetDetect = 2} OwMode ; 

extern unsigned char OneWireState;

ErrorStatus OneWireScratchpadVerify(uint8_t *address,uint8_t *addressverify,uint8_t * data);
ErrorStatus OneWireScratchpadWrite(uint8_t *address,uint8_t * data, uint16_t * CRCval);
ErrorStatus OneWireScratchpadCopy(uint8_t *address);

extern bool OneWire_Initialized;

void OneWireIdleHigh(void);

ErrorStatus  OneWireCheckPattern(void);

ErrorStatus  OneWireReadMemory(uint8_t *address,uint8_t * data, uint32_t count); //reads an specified number of bytes from the device starting at specified address // returns ERROR or SUCCESS

uint16_t OneWireCRC16(unsigned char *ptr,  unsigned int count);
uint8_t OneWireCRC8( uint8_t *addr, uint8_t len);

ErrorStatus OneWireResetDetect(void);
void OneWire_Send(unsigned char * Data);
void OneWire_Init(OwMode mode);
void OneWire_Write_Char(unsigned char Data);
unsigned char OneWire_Read_Char(void) ;
//uint8_t  oneWireSearchRom (OneWireDriver* drv, bool_t conditional, OneWireRomAddress *addrs, uint8_t len);
ErrorStatus  OneWireWritePage(uint8_t *address,uint8_t * Data) ; //writes an 8-byte page to the device starting at specified address //returns ERROR or SUCCESS

ErrorStatus  OneWireReadROM(uint8_t * romcode);




//ONLY UNCOMMENT ONE OF THE UARTS BELOW TO SPECIFY WHICH WILL BE USED BY THE ONEWIRE LIBRARY/////
/////////////////////////////////////////////////////////////////////////////////////////////////

//#define Use_USART1
#define Use_USART2
//define Use_USART3
//#define Use_USART4
//#define Use_USART5

/////////////////////////////////////////////////////////////////////////////////////////////////

#define Uart_1wire_Baudrate_ResetDetect 	9600
#define Uart_1wire_Baudrate_ReadWrite    	115200


#ifdef Use_USART1
#define Onewire_Port_Peripheral_RCC  			RCC_AHBPeriph_GPIOA
#define Onewire_Usart_Peripheral_RCC 			RCC_APB1Periph_USART1
#define Onewire_txPort  									GPIOA
#define Onewire_USARTx										USART1
#define Onewire_txPin											GPIO_Pin_9
#define Onewire_PinSource									GPIO_PinSource9
#define Onewire_PinAF	 										GPIO_AF_7    
#endif	//Use_USART1

#ifdef Use_USART2
#define Onewire_Port_Peripheral_RCC  			RCC_AHBPeriph_GPIOA
#define Onewire_Usart_Peripheral_RCC 			RCC_APB1Periph_USART2 
#define Onewire_txPort  									GPIOA
#define Onewire_USARTx										USART2
#define Onewire_txPin											GPIO_Pin_2
#define Onewire_PinSource									GPIO_PinSource2
#define Onewire_PinAF	 										GPIO_AF_7    
#endif  //Use_USART2

#ifdef Use_USART3
#define Onewire_Port_Peripheral_RCC  			RCC_AHBPeriph_GPIOB
#define Onewire_Usart_Peripheral_RCC 			RCC_APB1Periph_USART3
#define Onewire_txPort  									GPIOB
#define Onewire_USARTx										USART3
#define Onewire_txPin											GPIO_Pin_10
#define Onewire_PinSource									GPIO_PinSource10
#define Onewire_PinAF	 										GPIO_AF_7    
#endif  //Use_USART3

#ifdef Use_USART4
#define Onewire_Port_Peripheral_RCC  			RCC_AHBPeriph_GPIOC
#define Onewire_Usart_Peripheral_RCC 			RCC_APB1Periph_USART4
#define Onewire_txPort  									GPIOC
#define Onewire_USARTx										USART4
#define Onewire_txPin											GPIO_Pin_10
#define Onewire_PinSource									GPIO_PinSource10
#define Onewire_PinAF	 										GPIO_AF_5    
#endif //Use_USART4

#ifdef Use_USART5
#define Onewire_Port_Peripheral_RCC  			RCC_AHBPeriph_GPIOC
#define Onewire_Usart_Peripheral_RCC 			RCC_APB1Periph_USART5
#define Onewire_txPort  									GPIOC
#define Onewire_USARTx										USART5
#define Onewire_txPin											GPIO_Pin_12
#define Onewire_PinSource									GPIO_PinSource12
#define Onewire_PinAF	 										GPIO_AF_5   
#endif //Use_USART5
/* Private macro -------------------------------------------------------------*/



#endif


