/**
  ******************************************************************************
  * @file    USB_Example/hw_config.h
  * @author  MCD Application Team
  * @version V1.1.0
  * @date    20-September-2012
  * @brief   Hardware Configuration & Setup.
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; COPYRIGHT 2012 STMicroelectronics</center></h2>
  *
  * Licensed under MCD-ST Liberty SW License Agreement V2, (the "License");
  * You may not use this file except in compliance with the License.
  * You may obtain a copy of the License at:
  *
  *        http://www.st.com/software_license_agreement_liberty_v2
  *
  * Unless required by applicable law or agreed to in writing, software 
  * distributed under the License is distributed on an "AS IS" BASIS, 
  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  * See the License for the specific language governing permissions and
  * limitations under the License.
  *
  ******************************************************************************
  */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __USB_HW_CONFIG_H
#define __USB_HW_CONFIG_H

//#define RTC_SUMMER_CORRECTION //define this to use the rtc semmer correction routine

/* Includes ------------------------------------------------------------------*/
 #include "stm32f30x.h"
#include <stdbool.h>
#include "integer.h"
#include "DataTypes.h"  //here we difined all the global data types used
#include <string.h>	
#include <stdint.h>
#include "math.h"
#include "main.h"
//#include "EEPROM_24Cxx.h"
///#include "ff.h"
//#include "SPI_SD_Storage.h"
//#include "UART_OneWire.h"
#include "BuildDefs.h"
#include "integer.h"
#include <string.h>	
#include <stdlib.h>
//#include "SIM800L.h"
#include <stdio.h>

#include "usb_lib.h"
#include "flash_if.h"
#include "usb_pwr.h"
#include "usb_bot.h"   //for bot state detection
#include "math.h"
#include "usb_istr.h"
#include "stm32f30x_it.h"
#include "usb_desc.h"
#include <stdarg.h>
//#include "RFM69.h"
//#include "ESP8266.h"
//#include "RF_OOK.h"
//////////#include "TICC2500.h"
//////////#include "TICC1101.h"
//#include "Si7021.h"
//#include "SSD1306.h"
//#include "IRArrayHW.h"



/* Exported types ------------------------------------------------------------*/
/* Exported constants --------------------------------------------------------*/
/* Exported macro ------------------------------------------------------------*/
/* Exported define -----------------------------------------------------------*/


#define USB_INT_DEFAULT// For Default Interrupt Mode see usb_hw_config.c

#define USB_USE_EXTERNAL_PULLUP


#define USB_DISCONNECT_PORT                     GPIOB  
#define USB_DISCONNECT_PIN                  GPIO_Pin_0
#define RCC_AHBPeriph_GPIO_DISCONNECT       RCC_AHBPeriph_GPIOB



/* Exported functions ------------------------------------------------------- */
//extern volatile bool LOAD_MSD;
void  USB_Config (void);
void Set_System(void);
void Set_USBClock(void);
void Enter_LowPowerMode(void);
void Leave_LowPowerMode(void);
void USB_Interrupts_Config(void);
void USB_Cable_Config (FunctionalState NewState);
void Get_SerialNum(void);


//kjjkhgjkhgjhgdfgdgsdf
#endif  /*__USB_HW_CONFIG_H*/

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/ 
