/**
  ******************************************************************************
  * @file    usb_desc.c
  * @author  MCD Application Team
  * @version V4.0.0
  * @date    21-January-2013
  * @brief   Descriptors for Custom HID Demo
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; COPYRIGHT 2013 STMicroelectronics</center></h2>
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


/* Includes ------------------------------------------------------------------*/
#include "usb_lib.h"
#include "usb_desc.h"

/* Private typedef -----------------------------------------------------------*/
/* Private define ------------------------------------------------------------*/
/* Private macro -------------------------------------------------------------*/
/* Private variables ---------------------------------------------------------*/
/* Extern variables ----------------------------------------------------------*/
/* Private function prototypes -----------------------------------------------*/
/* Private functions ---------------------------------------------------------*/

/* USB Standard Device Descriptor */
const uint8_t CustomHID_DeviceDescriptor[CUSTOMHID_SIZ_DEVICE_DESC] =
  {
    0x12,                       /*bLength */
    USB_DEVICE_DESCRIPTOR_TYPE, /*bDescriptorType*/
    0x00,                       /*bcdUSB */
    0x02,
    0x00,                       /*bDeviceClass*/
    0x00,                       /*bDeviceSubClass*/
    0x00,                       /*bDeviceProtocol*/
    0x40,                       /*bMaxPacketSize40*/
    0x88,                       /*idVendor (0x0488)*/
    0x04,
    0x55,                       /*idProduct = 0x5655*/
    0x56,
    0x00,                       /*bcdDevice rel. 2.00*/
    0x05,
    1,                          /*Index of string descriptor describing
                                              manufacturer */
    2,                          /*Index of string descriptor describing
                                             product*/
    3,                          /*Index of string descriptor describing the
                                             device serial number */
    0x01                        /*bNumConfigurations*/
  }
  ; /* CustomHID_DeviceDescriptor */


/* USB Configuration Descriptor */
/*   All Descriptors (Configuration, Interface, Endpoint, Class, Vendor */
const uint8_t CustomHID_ConfigDescriptor[CUSTOMHID_SIZ_CONFIG_DESC] =
  {
    0x09, /* bLength: Configuration Descriptor size */
    USB_CONFIGURATION_DESCRIPTOR_TYPE, /* bDescriptorType: Configuration */
    CUSTOMHID_SIZ_CONFIG_DESC,
    /* wTotalLength: Bytes returned */
    0x00,
    0x01,         /* bNumInterfaces: 1 interface */    //this determines the number of interface descriptors to follow
    0x01,         /* bConfigurationValue: Configuration value */
    0x00,         /* iConfiguration: Index of string descriptor describing
                                 the configuration*/
    0xC0,         /* bmAttributes: Self powered */
    0x32,         /* MaxPower 100 mA: this current is used for detecting Vbus */

    /**************INTERFACE DESCRIPTOR FOR Custom HID interface ****************/
    /* 09 */
    0x09,         /* bLength: Interface Descriptor size */
    USB_INTERFACE_DESCRIPTOR_TYPE,/* bDescriptorType: Interface descriptor type */
    0x00,         /* bInterfaceNumber: Number of Interface */
    0x00,         /* bAlternateSetting: Alternate setting */
    0x02,         /* bNumEndpoints */
    0x03,         /* bInterfaceClass: HID */
    0x00,         /* bInterfaceSubClass : 1=BOOT, 0=no boot */
    0x00,         /* nInterfaceProtocol : 0=none, 1=keyboard, 2=mouse */
    0,            /* iInterface: Index of string descriptor */
    /******************** Descriptor of Custom HID HID ********************/
    /* 18 */
    CUSTOMHID_SIZ_HID_DESC,         /* bLength: HID Descriptor size */
    HID_DESCRIPTOR_TYPE, /* bDescriptorType: HID */
    0x10,         /* bcdHID: HID Class Spec release number */
    0x01,
    0x00,         /* bCountryCode: Hardware target country */
    0x01,         /* bNumDescriptors: Number of HID class descriptors to follow */
    0x22,         /* bDescriptorType */
    CUSTOMHID_SIZ_REPORT_DESC,/* wItemLength: Total length of Report descriptor */
    0x00,
    /******************** Descriptor of Custom HID endpoints ******************/
    /* 27 */
    0x07,          /* bLength: Endpoint Descriptor size */
    USB_ENDPOINT_DESCRIPTOR_TYPE, /* bDescriptorType: */

    0x81,          /* bEndpointAddress: Endpoint Address (IN) */
    0x03,          /* bmAttributes: Interrupt endpoint */
    USB_EP1_MAX_BUFFER_SIZE,          /* wMaxPacketSize: specified in the descriptor header file */
    0x00,
    0x20,          /* bInterval: Polling Interval (32 ms) */
    /* 34 */
    	
    0x07,	/* bLength: Endpoint Descriptor size */
    USB_ENDPOINT_DESCRIPTOR_TYPE,	/* bDescriptorType: */
			/*	Endpoint descriptor type */
    0x01,	/* bEndpointAddress: Endpoint Address (OUT) */
    0x03,	/* bmAttributes: Interrupt endpoint */
    USB_EP1_MAX_BUFFER_SIZE,	/* wMaxPacketSize:   */
    0x00,
    0x20,	/* bInterval: Polling Interval (20 ms) */
    /* 41 */
  }
  ; /* CustomHID_ConfigDescriptor */
	
	
	
const uint8_t CustomHID_ReportDescriptor[CUSTOMHID_SIZ_REPORT_DESC] =
  {                    
    0x06, 0xFF, 0x00,      /* USAGE_PAGE (Vendor Page: 0xFF00) */                       
    0x09, 0x01,            /* USAGE (Demo Kit)               */    
    0xa1, 0x01,            /* COLLECTION (Application)       */            
    /* 7 */
    
     /* BUS STATUS REPORT IN */  ///INPUT///
		0x85, IN_ClusterPowerStatus,            /*     REPORT_ID (2)              */         
    0x09, 0x02,            /*     USAGE (ADC IN)             */          
    0x15, 0x00,            /*     LOGICAL_MINIMUM (0)        */               
    0x26, 0xff, 0x00,      /*     LOGICAL_MAXIMUM (255)      */                 
    0x75, 0x08,            /*     REPORT_SIZE (8)            */    
    0x95, PROFILE_REPORT_SIZE,            /*     REPORT_COUNT (1)           */   		
    0x81, 0x82,            /*     INPUT (Data,Var,Abs,Vol)   */                    

////////////////////////////////////////////////////////////////////////////////
    /* CHANGE OUTPUT SETTINGS REPORT */    ///OUTPUT///
    0x85, OUT_RequestConfiguration,            /*     REPORT_ID (6)              */
    0x09, 0x06,            /*     USAGE (Tamper Push Button) */      
    0x15, 0x00,            /*     LOGICAL_MINIMUM (0)        */      
    0x25, 0xff,            /*     LOGICAL_MAXIMUM (1)        */      
    0x75, 0x08,            /*     REPORT_SIZE (1) this must match the maximum specified above 0xff for 8 bits size           */  
		0x95, PROFILE_REPORT_SIZE,            /*     REPORT_COUNT (1)           */ 
    0x91, 0x82,            /*     OUTPUT (Data,Var,Abs,Vol)  */
	/*  20  */
	
////////////////////////////////////////////////////////////////////////       
    /* Request Board Status Report */  ///OUTPUT///
    0x85, OUT_SetOperationState,            /*     REPORT_ID 4)		     */
    0x09, 0x04,            /*     USAGE (LED 4)	             */
    0x15, 0x00,            /*     LOGICAL_MINIMUM (0)        */          
    0x25, 0xff,            /*     LOGICAL_MAXIMUM (255)        */           
    0x75, 0x08,            /*     REPORT_SIZE (1)            */        
    0x95, PROFILE_REPORT_SIZE,            /*     REPORT_COUNT (1)           */    
    0x91, 0x82,            /*     OUTPUT (Data,Var,Abs,Vol)  */
    /* 20 */

  /* Send INPUT Status to pc */  ///INPUT///
    0x85, IN_12,            /*     REPORT_ID (12)              */         
    0x09, 0x0C,            /*     USAGE (ADC IN)             */          
    0x15, 0x00,            /*     LOGICAL_MINIMUM (0)        */               
    0x26, 0xff, 0x00,      /*     LOGICAL_MAXIMUM (255)      */                 
    0x75, 0x08,            /*     REPORT_SIZE (8)            */    
    0x95, PROFILE_REPORT_SIZE,            /*     REPORT_COUNT (1)           */   		
    0x81, 0x82,            /*     INPUT (Data,Var,Abs,Vol)   */                    

    /* OUTPUT STATUS REPORT IN */  ///INPUT///
    0x85, IN_StatusMessage,            /*     REPORT_ID (7)              */         
    0x09, 0x07,            /*     USAGE (ADC IN)             */          
    0x15, 0x00,            /*     LOGICAL_MINIMUM (0)        */               
    0x26, 0xff, 0x00,      /*     LOGICAL_MAXIMUM (255)      */                 
    0x75, 0x08,            /*     REPORT_SIZE (8)            */    
    0x95, PROFILE_REPORT_SIZE,            /*     REPORT_COUNT (1)           */   		
    0x81, 0x82,            /*     INPUT (Data,Var,Abs,Vol)   */                    
    
		 /* excitation status feedback to pc*/  ///INPUT/// IN_ExcitationStatus
    0x85, IN_HardwareConfiguration,           //    REPORT_ID (11)                      
    0x09, 0x0B,            ///     USAGE (ADC IN)                      
    0x15, 0x00,            //     LOGICAL_MINIMUM (0)                       
    0x26, 0xff, 0x00,      //     LOGICAL_MAXIMUM (255)      //                
    0x75, 0x08,            //     REPORT_SIZE (8)           //    
    0x95, PROFILE_REPORT_SIZE,          //    REPORT_COUNT (1)             		
    0x81, 0x82,            //    INPUT (Data,Var,Abs,Vol)   //                    
    		
		  /*  */   /* CHANGE EXCITATION SETTINGS REPORT */      ///OUTPUT///  
    0x85, OUT_ControlOperation,            /*     REPORT_ID (08)		     */
    0x09, 0x08,            /*     USAGE (LED 1)	             */
    0x15, 0x00,            /*     LOGICAL_MINIMUM (0)        */          
    0x25, 0xff,            /*     LOGICAL_MAXIMUM (255)        */           
    0x75, 0x08,            /*     REPORT_SIZE (8)            */        
    0x95, PROFILE_REPORT_SIZE,            /*     REPORT_COUNT (2)           */       
    0x91, 0x82,            /*     OUTPUT (Data,Var,Abs,Vol)  */                                  
    /* total bytes = 20*/



/*  */   /* Profile settings Report from PC */      ///OUTPUT///  
    0x85, OUT_SetClusterPowerLevel,            /*     REPORT_ID (05)		     */
    0x09, 0x05,            /*     USAGE (LED 1)	             */
    0x15, 0x00,            /*     LOGICAL_MINIMUM (0)        */          
    0x26, 0xff,0x00,            /*     LOGICAL_MAXIMUM (255)        */           
    0x75, 0x08,            /*     REPORT_SIZE (8)            */        
    0x95, PROFILE_REPORT_SIZE,            /*     REPORT_COUNT (2)           */       
    0x91, 0x82,           /*     OUTPUT (Data,Var,Abs,Vol)  */                                  
    /* total bytes = 20*/

/*  */   /* Profile settings Report to PC */      ///INPUT///  
    0x85, IN_OperationStatus,            /*     REPORT_ID (03)		     */
    0x09, 0x03,            /*     USAGE (LED 1)	             */
    0x15, 0x00,            /*     LOGICAL_MINIMUM (0)        */          
    0x26, 0xff,0x00,            /*     LOGICAL_MAXIMUM (255)        */           
    0x75, 0x08,            /*     REPORT_SIZE (8)            */        
    0x95, PROFILE_REPORT_SIZE,            /*     REPORT_COUNT (2)           */       
   
    0x81, 0x82,           /*     INPUT (Data,Var,Abs,Vol)  */                                  
    /* total bytes = 20*/

/*  */   /* control status report from PC */      ///OUTPUT///  
    0x85, OUT_13,            /*     REPORT_ID (13)		     */
    0x09, 0x0D,            /*     USAGE (LED 1)	             */
    0x15, 0x00,            /*     LOGICAL_MINIMUM (0)        */          
    0x26, 0xff,0x00,            /*     LOGICAL_MAXIMUM (255)        */           
    0x75, 0x08,            /*     REPORT_SIZE (8)            */        
    0x95, PROFILE_REPORT_SIZE,            /*     REPORT_COUNT (2)           */       

    0x91, 0x82,           /*     OUTPUT (Data,Var,Abs,Vol)  */                                  
    /* total bytes = 20*/

/*  */   /* Linearization Command */      ///OUTPUT///  
    0x85, OUT_14,            /*     REPORT_ID (14)		     */
    0x09, 0x0E,            /*     USAGE (LED 1)	             */
    0x15, 0x00,            /*     LOGICAL_MINIMUM (0)        */          
    0x26, 0xff,0x00,            /*     LOGICAL_MAXIMUM (255)        */           
    0x75, 0x08,            /*     REPORT_SIZE (8)            */        
    0x95, PROFILE_REPORT_SIZE,            /*     REPORT_COUNT (2)           */       
    0x91, 0x82,           /*     OUTPUT (Data,Var,Abs,Vol)  */                                  
    /* total bytes = 21*/
		
		 /* Linearization status report*/  ///INPUT/// 
    0x85, IN_15,            /*     REPORT_ID (15)              */         
    0x09, IN_15,            /*     USAGE (ADC IN)             */          
    0x15, 0x00,            /*     LOGICAL_MINIMUM (0)        */               
    0x26, 0xff, 0x00,      /*     LOGICAL_MAXIMUM (255)      */                 
    0x75, 0x08,            /*     REPORT_SIZE (8)            */    
    0x95, PROFILE_REPORT_SIZE,            /*     REPORT_COUNT (1)           */   		
    0x81, 0x82,            /*     INPUT (Data,Var,Abs,Vol)   */                    
    
			 /* Linearization status report*/  ///INPUT/// 
    0x85, IN_17,            /*     REPORT_ID (17)              */         
    0x09, IN_17,            /*     USAGE (ADC IN)             */          
    0x15, 0x00,            /*     LOGICAL_MINIMUM (0)        */               
    0x26, 0xff, 0x00,      /*     LOGICAL_MAXIMUM (255)      */                 
    0x75, 0x08,            /*     REPORT_SIZE (8)            */    
    0x95, PROFILE_REPORT_SIZE,            /*     REPORT_COUNT (1)           */   		
    0x81, 0x82,            /*     INPUT (Data,Var,Abs,Vol)   */                    
		
 /* Linearization status report*/  ///INPUT/// 
    0x85, IN_16,            /*     REPORT_ID (7)              */         
    0x09, IN_16,            /*     USAGE (ADC IN)             */          
    0x15, 0x00,            /*     LOGICAL_MINIMUM (0)        */               
    0x26, 0xff, 0x00,      /*     LOGICAL_MAXIMUM (255)      */                 
    0x75, 0x08,            /*     REPORT_SIZE (8)            */    
    0x95, PROFILE_REPORT_SIZE,            /*     REPORT_COUNT (1)           */   		
    0x81, 0x82,            /*     INPUT (Data,Var,Abs,Vol)   */                    
    
    0xc0 	          /*     END_COLLECTION	             */
  }; /* CustomHID_ReportDescriptor */  

/* USB String Descriptors (optional) */
const uint8_t CustomHID_StringLangID[CUSTOMHID_SIZ_STRING_LANGID] =
  {
    CUSTOMHID_SIZ_STRING_LANGID,
    USB_STRING_DESCRIPTOR_TYPE,
    0x09,
    0x04
  }
  ; /* LangID = 0x0409: U.S. English */

const uint8_t CustomHID_StringVendor[CUSTOMHID_SIZ_STRING_VENDOR] =
  {
    CUSTOMHID_SIZ_STRING_VENDOR, /* Size of Vendor string */
    USB_STRING_DESCRIPTOR_TYPE,  /* bDescriptorType*/
    /* Manufacturer: "Phoenix Calibration" */
    'P', 0, 'H', 0, 'O', 0, 'E', 0, 'N', 0, 'I', 0, 'X', 0, ' ', 0,
    'C', 0, 'A', 0, 'L', 0, 'I', 0, 'B', 0, 'R', 0, 'A', 0, 'T', 0,
    'I', 0, 'O', 0, 'N', 0
  };

const uint8_t CustomHID_StringProduct[CUSTOMHID_SIZ_STRING_PRODUCT] =
  {
		
    CUSTOMHID_SIZ_STRING_PRODUCT,          /* bLength */
    USB_STRING_DESCRIPTOR_TYPE,        /* bDescriptorType */
    'I', 0, 'R', 0, '_', 0, 'E', 0, 'M', 0, 'I', 0, 'T', 0,
    'T', 0, 'E', 0, 'R', 0, '_', 0, 'C', 0, 'O', 0, 'N', 0
  };
uint8_t CustomHID_StringSerial[CUSTOMHID_SIZ_STRING_SERIAL] =
  {
    CUSTOMHID_SIZ_STRING_SERIAL,           /* bLength */
    USB_STRING_DESCRIPTOR_TYPE,        /* bDescriptorType */
    '3', 0, '5', 0, '4', 0,'5', 0,'3', 0
  };

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
