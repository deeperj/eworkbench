#ifndef H_IRArrayHW_H
#define H_IRArrayHW_H

#include <stdint.h>
#include "stm32f30x.h"
#include <stdbool.h>
#include <string.h>
#include <math.h>
#include "STM32F303_HAL.h"  //already included in hardware config
#include "stm32f30x_exti.h"

#define MAX_CLUSTERS 50 //this is the total number of clusters that the master can handle

#define TOTAL_IR_TEST_COLUMNS 5
#define TOTAL_IR_TEST_ROWS 5
#define TOTAL_IRES (TOTAL_IR_TEST_ROWS * TOTAL_IR_TEST_COLUMNS)
#define POWER_RESOLUTION 100


//#define ATTENUATION 0.5 //atenuation percentage

//#define MINIMUM_TRIGGER 2 //the minimum triac firing period in us

//#define HOLD_OFF ((TOTAL_PERIOD * ATTENUATION)/100)
//#define FIRING_PERIOD (TOTAL_PERIOD -  HOLD_OFF)
//#define SLOT_PERIOD  (FIRING_PERIOD /	POWER_RESOLUTION)

//set whether to enable tx and rx using 433 mhz modules
//#define RF433_TX_ENABLE
//#define RF433_RX_ENABLE
#define IRE_ZERO_CROSS_PORT                     		GPIOA 
#define IRE_ZERO_CROSS_PIN                  				GPIO_Pin_15
#define IRE_ZERO_CROSS_RCC_AHBPeriph      					RCC_AHBPeriph_GPIOA
#define IRE_ZERO_CROSS_IRQ_EXTI_LINE              	EXTI_Line15
#define IRE_ZERO_CROSS_IRQ_EXTI_PIN_SOURCE        	EXTI_PinSource15
#define IRE_ZERO_CROSS_IRQ_EXTI_PORT_SOURCE       	EXTI_PortSourceGPIOA
#define IRE_ZERO_CROSS_IRQ_EXTI_IRQn               	EXTI15_10_IRQn 
#define IRE_ZERO_CROSS_TriggerType               	EXTI_Trigger_Rising_Falling //EXTI_Trigger_Rising//EXTI_Trigger_Falling //EXTI_Trigger_Rising_Falling 
#define IRE_ZERO_CROSS_EXTI_Piority               	0x00
#define IRE_ZERO_CROSS_EXTI_SubPiority               	0x00

////Cuolum driver pin definitions
#define IRE_C0_PORT                     		GPIOA 
#define IRE_C0_PORT_PIN                  				GPIO_Pin_1
#define IRE_C0_PORT_RCC_AHBPeriph      					RCC_AHBPeriph_GPIOA

#define IRE_C1_PORT                     		GPIOA 
#define IRE_C1_PORT_PIN                  				GPIO_Pin_4
#define IRE_C1_PORT_RCC_AHBPeriph      					RCC_AHBPeriph_GPIOA

#define IRE_C2_PORT                     		GPIOA 
#define IRE_C2_PORT_PIN                  				GPIO_Pin_8
#define IRE_C2_PORT_RCC_AHBPeriph      					RCC_AHBPeriph_GPIOA

#define IRE_C3_PORT                     		GPIOA 
#define IRE_C3_PORT_PIN                  				GPIO_Pin_9
#define IRE_C3_PORT_RCC_AHBPeriph      					RCC_AHBPeriph_GPIOA

#define IRE_C4_PORT                     		GPIOA 
#define IRE_C4_PORT_PIN                  				GPIO_Pin_10
#define IRE_C4_PORT_RCC_AHBPeriph      					RCC_AHBPeriph_GPIOA


///Row Drivers Pin definitions
#define IRE_R0_PORT                     		GPIOB 
#define IRE_R0_PORT_PIN                  				GPIO_Pin_1
#define IRE_R0_PORT_RCC_AHBPeriph      					RCC_AHBPeriph_GPIOB

#define IRE_R1_PORT                     		GPIOB 
#define IRE_R1_PORT_PIN                  				GPIO_Pin_2
#define IRE_R1_PORT_RCC_AHBPeriph      					RCC_AHBPeriph_GPIOB

#define IRE_R2_PORT                     		GPIOB 
#define IRE_R2_PORT_PIN                  				GPIO_Pin_4
#define IRE_R2_PORT_RCC_AHBPeriph      					RCC_AHBPeriph_GPIOB

#define IRE_R3_PORT                     		GPIOB 
#define IRE_R3_PORT_PIN                  				GPIO_Pin_5
#define IRE_R3_PORT_RCC_AHBPeriph      					RCC_AHBPeriph_GPIOB

#define IRE_R4_PORT                     		GPIOB 
#define IRE_R4_PORT_PIN                  				GPIO_Pin_8
#define IRE_R4_PORT_RCC_AHBPeriph      					RCC_AHBPeriph_GPIOB

typedef struct {
	uint8_t PowerLevel;
	uint32_t TriggerCount;
	uint32_t LastUpdateCycleID; //this is the cycle id when this was last updated
	bool Active; //this flag tells whether the element is present or not maybe a dead cel this is updated during startup post
	}IR_Element_Type;

	typedef struct {
	uint8_t PowerLevel;
//	uint32_t TriggerCount;
//	uint32_t LastUpdateCycleID; //this is the cycle id when this was last updated
//	bool Active; //this flag tells whether the element is present or not maybe a dead cel this is updated during startup post
	}IR_Element_Shadow_Type;
	
	typedef struct{
		uint32_t SlotLatency;
		uint8_t ElementCount;
	}FireSlotType;
	
	typedef struct{
		float Vload;
		float Power; //apparent power taken at the current firing angle
		float FireAngle;
	}PowerTableType;
	
	typedef struct
{
uint8_t ID; //this is the identifier for the cluster.
uint8_t	ElementsRows; //the number of rows of elements on this cluster
uint8_t	ElementsColumns; //the number of columns of elements of this cluster
uint8_t	LocationRow; //the row location for this cluster on the heating array
uint8_t	LocationColumn; //the column location of this cluster on the full heating array
IR_Element_Type Elements[TOTAL_IRES]; //this holds the  array of elements in the cluster
IR_Element_Shadow_Type ElementsShadow[TOTAL_IRES]; //this holds the shadow of array of elements in the cluster	
float	TotalPower; //this keeps track of the total power taken by the switched on elements of the cluster
}ClusterType;


extern GPIOParamStruct IRE_Rows[];
extern GPIOParamStruct IRE_Columns[];

extern GPIOParamStruct IRE_ZERO_CROSS;

void InitTestCluster(void);

extern volatile ClusterType * IRE_CLUSTER_ARRAY[];

extern volatile uint32_t  ZeroCrossCycleId; //thisw keeps track on the zero crossing cycles
volatile extern float AttenuationFactor ;
volatile extern uint32_t SlotPeriod;
volatile extern uint32_t FireInterval;
volatile extern uint32_t CURRENT_SLOT ;
volatile extern uint32_t LastZeroCross;

volatile extern uint8_t TotalDetectedClusters; 
volatile extern	uint32_t HoldOffPeriod;
volatile extern	uint32_t ZeroCrossPeriod;
void FireSegment(uint8_t segment);
void SetPower(uint8_t cluster,uint8_t element,uint8_t level);
void FireElement(uint8_t row,uint8_t column);
void ZeroCrossInterrupt(void);
void IRArray_Config(void);
void RefactorPowerTable(void);
//void RF433_Send(uint8_t * code , bool InvertedRf) ;
#endif // H_IRArrayHW_H
