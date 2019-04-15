/**
  ******************************************************************************
  * @file    EEPROM_24Cxx.h
  * @author  Edison Owhonda
  * @version V1.0.0
  * @date    14-March-2014
  * @brief    
  *          
  *  
  ******************************************************************************
  * @attention
  * this is the driver for external I2C eeprom
  * 
  *
  ******************************************************************************
  */
		/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __EEPROM_24Cxx_H
#define __EEPROM_24Cxx_H
	
	 #include "main.h"
#include <stdint.h>
 #include "utils.h"
 #include "stm32f30x_conf.h"   //includes all the Peripheral Library configuration header files


#define EEPROM_USE_I2C1		//ONLY one should be uncommented
//#define EEPROM_USE_I2C2		//ONLY one should be uncommented

#define Own_I2C_Address 0xEE;


/* Uncomment the following line to use the default LSM303DLHC_TIMEOUT_UserCallback() 
   function implemented in stm32f3_discovery_lgd20.c file.
   LSM303DLHC_TIMEOUT_UserCallback() function is called whenever a timeout condition 
   occure during communication (waiting transmit data register empty flag(TXE)
   or waiting receive data register is not empty flag (RXNE)). */   
/* #define USE_DEFAULT_TIMEOUT_CALLBACK */

/* Maximum Timeout values for flags waiting loops. These timeouts are not based
   on accurate values, they just guarantee that the application will not remain
   stuck if the I2C communication is corrupted.
   You may modify these timeout values depending on CPU frequency and application
   conditions (interrupts routines ...). */   
#define I2C_TIMEOUT_FLAG ((uint32_t)0x1000)
#define I2C_TIMEOUT_LONG ((uint32_t)(10 * I2C_TIMEOUT_FLAG)) 


#define MEM_DEVICE_ADDR 0xA0


//Memory type  //maximum address
#define M2400 	0x000F
#define M2401 	0x007F
#define M2402 	0x00FF
#define M2404 	0x01FF
#define M2408 	0x03FF
#define M2416 	0x07FF
#define M2432 	0x0FFF
#define M2464 	0x1FFF
#define M24128 	0x3FFF
#define M24256 	0x7FFF
#define M24512 	0xFFFF


//#if BOARD_PCB_REV  == 2
//#define MEM_TYPE  M2408 //M24512
//#endif

//rev 3 and above boards have a larger 64k bit eeprom
//#if BOARD_PCB_REV  >= 3
#define MEM_TYPE  M24256 //M24512
//#endif

//this is not yet implemented as it will require receving adress over 16 bits right now the funtion gets just 16 bit address. so LATERRRRRRR!! mate
#if MEM_TYPE > M2416   //if we are using memory with 16 bit addressing
#define MEM_BANKS 1  //specify the number of banks used //1 is default
#endif

#ifdef EEPROM_USE_I2C1

#define EEP_I2Cx  I2C1

#define I2Cx_RCC_AHBPeriph 				RCC_APB1Periph_I2C1
#define I2Cx_Port_RCC_AHBPeriph  RCC_AHBPeriph_GPIOB

#define I2Cx_SCL_Pin  GPIO_Pin_6
#define I2Cx_SDA_Pin  GPIO_Pin_7

#define I2Cx_SCL_Port  GPIOB
#define I2Cx_SDA_Port  GPIOB

#define I2Cx_SCL_PinSource  GPIO_PinSource6
#define I2Cx_SDA_PinSource  GPIO_PinSource7

#define I2Cx_GPIO_AF 	GPIO_AF_4

#endif



#ifdef EEPROM_USE_I2C2

#define EEP_I2Cx  I2C2

#define I2Cx_RCC_AHBPeriph 				RCC_APB1Periph_I2C2


#define I2Cx_Port_RCC_AHBPeriph  RCC_AHBPeriph_GPIOA


#define I2Cx_SCL_Pin  GPIO_Pin_9
#define I2Cx_SDA_Pin  GPIO_Pin_10

#define I2Cx_SCL_Port  GPIOA
#define I2Cx_SDA_Port  GPIOA

#define I2Cx_SCL_PinSource  GPIO_PinSource9
#define I2Cx_SDA_PinSource  GPIO_PinSource10

#define I2Cx_GPIO_AF 	GPIO_AF_4


#endif

uint32_t EEP_I2Cx_TIMEOUT_UserCallback(void);
void Wipe_24Cxx(void);
void I2C_Eeprom_Init( void);
//This function initializes the I2C hardware, all the I2C configuration are done in this function. Try to understand this function carefully (explained later in this post).
ErrorStatus  Write_24Cxx(uint16_t MemAddr, uint8_t Data); 
ErrorStatus  Write_24Cxx2(uint16_t MemAddr,  uint8_t * pBuffer, uint16_t NumByteToWrite);

//16 bits variable is used for address because 24C512 accept address up to  0xffff, Others accept up to 0xff, this addressing scheme is taken care of in this function according to Mem_Type supplied by user. Mem_Type can be 24C01, 24C02, 24C04, 24C08, 24C16, 24C32, 24C64, 24C128, 24C256 & 24C512.
ErrorStatus Read_24Cxx(uint16_t MemAddr, uint8_t * ptrData,  uint16_t ReadCount );
ErrorStatus  MultiWrite_24Cxx(uint16_t MemAddr, uint8_t *Data, uint8_t NumBytes);
ErrorStatus  EEP_I2Cx_Reset(void);
//This is Memory read function, this function returns the 8 bit data read from Address ‘Addr’ of Memory ‘Mem_Type’.


#endif //__EEPROM_24Cxx_H
