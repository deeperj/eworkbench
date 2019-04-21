#include "IRArrayHW.h"

volatile uint32_t ZeroCrossPeriod = 0 ;
volatile uint32_t LastZeroCross = 0 ;
volatile uint32_t FireInterval = 0;
volatile uint32_t CURRENT_SLOT = 0;
volatile 	uint32_t FiringTime;
volatile  uint32_t SlotPeriod;
volatile 	uint32_t HoldOffPeriod;
volatile uint8_t TotalDetectedClusters = 0; // this holds the total number of clusters that have been found and stored on the cluster array
volatile ClusterType * IRE_CLUSTER_ARRAY[MAX_CLUSTERS];
volatile uint32_t SoftStartCyclesDelay = 10 ;  //minimum cycles between power increase update from shadow to main cluster data //50 yields 500ms update rate
volatile uint32_t SoftStartSteps = 5 ; //minimum power increase before using soft start routine

//volatile ClusterShadowType * IRE_CLUSTER_ARRAY_SHADOW[MAX_CLUSTERS];
volatile uint32_t ZeroCrossCycleId = 0;
volatile float AttenuationFactor = 0.01;
volatile uint32_t MINIMUM_TRIGGER = 12;

volatile uint32_t MAXIMUM_LEVEL = 90; //the minimum power level that can be set
volatile uint32_t MINIMUM_LEVEL = 10; //the minimum power level that can be set

volatile float MAX_POWER = 3120; //this is the totall power that can be drwn by this cluster

volatile int32_t PowerDiff = 0 ;
volatile FireSlotType FiringSlotData[POWER_RESOLUTION + 1];

volatile PowerTableType PowerTable[POWER_RESOLUTION + 1];

GPIOParamStruct IRE_Rows[TOTAL_IR_TEST_ROWS]=
{
{IRE_R0_PORT,IRE_R0_PORT_PIN,IRE_R0_PORT_RCC_AHBPeriph,GPIO_PuPd_UP,OUTPUT}	,
	{IRE_R1_PORT,IRE_R1_PORT_PIN,IRE_R1_PORT_RCC_AHBPeriph,GPIO_PuPd_UP,OUTPUT},
	{IRE_R2_PORT,IRE_R2_PORT_PIN,IRE_R2_PORT_RCC_AHBPeriph,GPIO_PuPd_UP,OUTPUT},
	{IRE_R3_PORT,IRE_R3_PORT_PIN,IRE_R3_PORT_RCC_AHBPeriph,GPIO_PuPd_UP,OUTPUT},
{IRE_R4_PORT,IRE_R4_PORT_PIN,IRE_R4_PORT_RCC_AHBPeriph,GPIO_PuPd_UP,OUTPUT}	,
};

GPIOParamStruct IRE_Columns[TOTAL_IR_TEST_COLUMNS]=
{
{IRE_C0_PORT,IRE_C0_PORT_PIN,IRE_C0_PORT_RCC_AHBPeriph,GPIO_PuPd_UP,OUTPUT}	,
	{IRE_C1_PORT,IRE_C1_PORT_PIN,IRE_C1_PORT_RCC_AHBPeriph,GPIO_PuPd_UP,OUTPUT},
	{IRE_C2_PORT,IRE_C2_PORT_PIN,IRE_C2_PORT_RCC_AHBPeriph,GPIO_PuPd_UP,OUTPUT},
	{IRE_C3_PORT,IRE_C3_PORT_PIN,IRE_C3_PORT_RCC_AHBPeriph,GPIO_PuPd_UP,OUTPUT},
{IRE_C4_PORT,IRE_C4_PORT_PIN,IRE_C4_PORT_RCC_AHBPeriph,GPIO_PuPd_UP,OUTPUT}	,
};

GPIOParamStruct IRE_ZERO_CROSS = 
{
	IRE_ZERO_CROSS_PORT,IRE_ZERO_CROSS_PIN,IRE_ZERO_CROSS_RCC_AHBPeriph,GPIO_PuPd_UP,INPUT,IRE_ZERO_CROSS_IRQ_EXTI_LINE,\
	IRE_ZERO_CROSS_IRQ_EXTI_PIN_SOURCE,IRE_ZERO_CROSS_IRQ_EXTI_PORT_SOURCE,IRE_ZERO_CROSS_IRQ_EXTI_IRQn,IRE_ZERO_CROSS_TriggerType,\
	IRE_ZERO_CROSS_EXTI_Piority,IRE_ZERO_CROSS_EXTI_SubPiority,
	
};

void InitTestCluster(void)
{
	//uint32_t * p;
	//allocate a memory block for the new cluster and put the address in the cluster arry
	IRE_CLUSTER_ARRAY[TotalDetectedClusters] = calloc( 1 , sizeof(ClusterType));
	//populate the cluster properties
	IRE_CLUSTER_ARRAY[TotalDetectedClusters]->ElementsRows = TOTAL_IR_TEST_ROWS;
		IRE_CLUSTER_ARRAY[TotalDetectedClusters]->ElementsColumns =TOTAL_IR_TEST_COLUMNS ;
		IRE_CLUSTER_ARRAY[TotalDetectedClusters]->LocationRow = 0;
		IRE_CLUSTER_ARRAY[TotalDetectedClusters]->LocationColumn = 0;
	//allocate memory for an aray of the total numbr of elements in the cluster of the type ir_elements
//	IRE_CLUSTER_ARRAY[TotalDetectedClusters]->Elements = malloc(sizeof(IR_Element_Type ) * 25);
	//assign address referencing to the first array member
	//incrase cluster count
	TotalDetectedClusters++;
}

void SetPower(uint8_t cluster,uint8_t element,uint8_t level)
{
	IRE_CLUSTER_ARRAY[cluster]->ElementsShadow[element].PowerLevel = level;
}
void FireSegment(uint8_t segment)
{
	//bool ColumnFound = FALSE;
	uint32_t FireCache;
	uint8_t r,c,x,RowStart = 0;
		//save the serocross id upon entry to see if it occured during our execution --only useful fir direct trigger system that leave trigger for the remaining cycle
// //sounds useless though as it still needs to be removed for the next half cycle .. .. . anyway, i will revisit this later
	uint32_t ZeroCrossEntryId = ZeroCrossCycleId;
	
	uint32_t LastColumnFire = 0;
		uint32_t EntryTime = SystickCount_us;
FiringSlotData[segment].ElementCount = 0;


	for(r = 0; r < TOTAL_IR_TEST_ROWS;r++)
	{
		RowStart = r*TOTAL_IR_TEST_COLUMNS;
		FireCache =0; //clear this for fresh start
//		ColumnFound = FALSE; //clear this for a new colums test
		//test the elements columns on this row if any needs firing
		for(x = 0 ;x < TOTAL_IR_TEST_COLUMNS; x++)
		{
			//if this column should be fired . . .
			if (((IRE_CLUSTER_ARRAY[0]->Elements[(RowStart)+ x].PowerLevel)) == segment )
			{
				//increase the firing count
				IRE_CLUSTER_ARRAY[0]->Elements[(RowStart)+x].TriggerCount ++;
				//save this info on the firing cache
				FireCache  |= 1 << x;
				//increment the fired elements counter
				FiringSlotData[segment].ElementCount++;
			}
			
		}
		//check if column found otherwise skip loop altogether
		if(FireCache == 0)
		{
			continue;
		}
		
	//assert the row
	IRE_Rows[r].IO_Port->BRR = IRE_Rows[r].IO_Pin;
	//RowStart = ;
		for(c = 0; c < TOTAL_IR_TEST_COLUMNS;c++)
		{
			//ActualPower = POWER_RESOLUTION - (uint8_t)((IRE_CLUSTER_ARRAY[0]->Elements[RowStart + c].PowerLevel));
			if(FireCache & (1 << c))
			{
					//if the cycle id has changed as a result of zero cros occuring whilst we are here then dont fire
				if(ZeroCrossEntryId != ZeroCrossCycleId	)	
				{
					break;
				}
			//set the column
			IRE_Columns[c].IO_Port->BSRR = IRE_Columns[c].IO_Pin;
				
				//record the time the column was set
				LastColumnFire = SystickCount_us ;
				
				//FiringSlotData[segment].ElementCount ++;
				//reset the column
		//	IRE_Columns[c].IO_Port->BRR = IRE_Columns[c].IO_Pin;	

			}
			
		}
		
//make sure last column fire time is adequate for the triac to fire
		while ((SystickCount_us - LastColumnFire) < MINIMUM_TRIGGER); //wait till mimimum time
		
		for(c = 0; c < TOTAL_IR_TEST_COLUMNS;c++)
		{
			//reset the column
			IRE_Columns[c].IO_Port->BRR = IRE_Columns[c].IO_Pin;	
		}
			
			//de assert the row after  columns have ben removed to give more trigger time
	IRE_Rows[r].IO_Port->BSRR = IRE_Rows[r].IO_Pin;	
	
	}
		FiringSlotData[segment].SlotLatency = SystickCount_us - EntryTime ;
	//return FiringSlotData[segment].ElementCount
	//FiringTime = ;
//	if(ZeroCrossEntryCount != ZeroCrossCycleId)
//	{
//		//remove the trigger that was just activated for direct drive systems not using matrix drive
//	}
}

void IRArray_Config(void)
{
	int i;
	for(i=0;i < TOTAL_IR_TEST_ROWS ;i++)
	{
	ConfigureIOPin(&IRE_Rows[i],FALSE);
	//set pin default high
IRE_Rows[i].IO_Port->BSRR = IRE_Rows[i].IO_Pin;		
	}
	
	for(i=0;i < TOTAL_IR_TEST_COLUMNS ;i++)
	{
	ConfigureIOPin(&IRE_Columns[i],FALSE);
	//	set pin default as low
		IRE_Columns[i].IO_Port->BRR = IRE_Columns[i].IO_Pin;
	}

	//setup the zero cross interupt pin
ConfigureIOPin(&IRE_ZERO_CROSS,TRUE);
	
}
void RefactorPowerTable(void)
{
	uint32_t x;
	float MaxVAngle = (AttenuationFactor * 180);
	float SlotAngle = (180 - MaxVAngle)/ POWER_RESOLUTION ;
	float VoltageIn = 240 ;
		float VPeak = VoltageIn / sqrt(0.5) ;
	float Vload ;
	float Rad;
	#define pi 3.141592654
	#define ILoad (450.0/117.0)//this is computed from the IR emmiters parameters
	for(x = 0; x < POWER_RESOLUTION;x++)
	{
		//get the firing angle
		PowerTable[POWER_RESOLUTION - x].FireAngle = MaxVAngle + (x * SlotAngle);
		//compute the radians angle
		Rad = 	PowerTable[POWER_RESOLUTION - x].FireAngle  * (pi / 180) ;
		//compute the Vload for this angle
		Vload = (VPeak * sqrt(((2 * pi) - (2 * Rad) + (sin(2 * Rad)))/(4 * pi)));
		
		//save the Vload 
		PowerTable[POWER_RESOLUTION - x].Vload = Vload  ;
		
		//compute the power starting from the highest on the table//percentage of voltage increase multiplied by the current to give apparent current then multiplied by the voltage to get power
		PowerTable[POWER_RESOLUTION - x].Power = ((Vload /PowerTable[POWER_RESOLUTION].Vload)* ILoad) * Vload;
	}
//compute total power
	IRE_CLUSTER_ARRAY[0]->TotalPower = 0;
		for(x = 0; x < TOTAL_IRES;x++)
		{
			IRE_CLUSTER_ARRAY[0]->TotalPower += PowerTable[ IRE_CLUSTER_ARRAY[0]->Elements[x].PowerLevel].Power  ;
		}
	
	
}
//this interrupt routine is supposed to be local to a cluster hence it should not see the cluster arry rather access the elements within its cluster 
//however for the testing we are hosting a single cluster, 0 in this case, within the master code 
void ZeroCrossInterrupt(void)
{
	uint32_t x;
uint32_t	NewPowerLevel;
	float NewTotalPower;
static float LastAttenuationFactor;
static float LastMaxPower;
	
	if(SystickCount_us > LastZeroCross) //make sure it is not an overflow situation if so dont update the zero crossperiod
	{
		ZeroCrossPeriod  = SystickCount_us - LastZeroCross ;
	}
	
	//save the current count
	LastZeroCross = SystickCount_us;
	ZeroCrossCycleId++; //increase the zero cross id
	
	//check if certain critical factors have changed then lets compute the power table and total system power
	if((AttenuationFactor != LastAttenuationFactor) || (MAX_POWER != LastMaxPower))
	{
	//refactor the power table	this might take a while
	//please wait ! ! ! ! !
	RefactorPowerTable();
	LastAttenuationFactor = AttenuationFactor;
	LastMaxPower  = MAX_POWER ;	
	}
	

//clear the columns or rows in case any one has just been triggered so we dont leave it on whist this is active
	//this may not be neccessary as the triac would have already been triggered by the time this interrupt is called
//	for(x = 0 ;x < TOTAL_IR_TEST_COLUMNS; x++)
//		{
//			//reset the column
//			IRE_Columns[x].IO_Port->BRR = IRE_Columns[x].IO_Pin;	
//		}
	
	
	//clear the trigger count atr every zero crossing		
	//TotalElements = 	IRE_CLUSTER_ARRAY[0]->ElementsColumns * IRE_CLUSTER_ARRAY[0]->ElementsRows;
		
//use the holdoff period to update from the shadow only once per cycle so we use the cycle id

		for(x = 0; x < TOTAL_IRES;x++)
		{
			//compare the shadow cluster data to the real one and transfer power settings
			if(IRE_CLUSTER_ARRAY[0]->ElementsShadow[x].PowerLevel != IRE_CLUSTER_ARRAY[0]->Elements[x].PowerLevel)
			{
				//check the last update time
				
				PowerDiff = IRE_CLUSTER_ARRAY[0]->ElementsShadow[x].PowerLevel - IRE_CLUSTER_ARRAY[0]->Elements[x].PowerLevel;
				//check if this is an increment
				if (PowerDiff > (int)SoftStartSteps) //cast to int for proper comparisonif power is increasing by more than max softsrat level
				{
				//check the minimum increase update interval
					if((ZeroCrossCycleId - IRE_CLUSTER_ARRAY[0]->Elements[x].LastUpdateCycleID) > SoftStartCyclesDelay )
					{
						//copy the current power level
						NewPowerLevel = IRE_CLUSTER_ARRAY[0]->Elements[x].PowerLevel; // ;
						//add the minimum power increase and move to the next element
						NewPowerLevel += SoftStartSteps ; 
						
						//ensure we dont request too low power as it will be unneccessary
						if((NewPowerLevel < MINIMUM_LEVEL))
						{
							NewPowerLevel = MINIMUM_LEVEL ;
						}
						else if(NewPowerLevel > MAXIMUM_LEVEL)
						{
							NewPowerLevel = MAXIMUM_LEVEL ;
							//truncate the shadow that is beyond the max power level
							IRE_CLUSTER_ARRAY[0]->ElementsShadow[x].PowerLevel = MAXIMUM_LEVEL ;
						}
						
						//check that the total system power will not be exceeded by this increment
						//subtract current element power from total and add new power level
						NewTotalPower = IRE_CLUSTER_ARRAY[0]->TotalPower - PowerTable[IRE_CLUSTER_ARRAY[0]->Elements[x].PowerLevel].Power + \
						PowerTable[NewPowerLevel].Power;
						//test if total exceeds the maximum
						if(NewTotalPower > MAX_POWER)
						{
						
							//reset the newpowerlevel to the pcurrent
							NewPowerLevel =  IRE_CLUSTER_ARRAY[0]->Elements[x].PowerLevel;
							//truncate the shadow power level	to the current level
						IRE_CLUSTER_ARRAY[0]->ElementsShadow[x].PowerLevel =	NewPowerLevel;
							
						}
						else
						{
							IRE_CLUSTER_ARRAY[0]->TotalPower = NewTotalPower;
						}
						

						
						IRE_CLUSTER_ARRAY[0]->Elements[x].PowerLevel = NewPowerLevel ;
						//save the cycle time for this update
						IRE_CLUSTER_ARRAY[0]->Elements[x].LastUpdateCycleID = ZeroCrossCycleId;
					}
			
				continue;					
				}
				
				//get the new power level from element shadow
				NewPowerLevel = IRE_CLUSTER_ARRAY[0]->ElementsShadow[x].PowerLevel;
				
				//ensure we dont request too low power as it will be unneccessary
				if((NewPowerLevel > 0) && (NewPowerLevel < MINIMUM_LEVEL))
				{
					NewPowerLevel = MINIMUM_LEVEL ;
					//reset the shadow to the minimum level
					IRE_CLUSTER_ARRAY[0]->ElementsShadow[x].PowerLevel = MINIMUM_LEVEL ;
				}
				else if(NewPowerLevel > MAXIMUM_LEVEL)
				{
					NewPowerLevel = MAXIMUM_LEVEL ;
					//truncate the shadow that is beyond the max power level
					IRE_CLUSTER_ARRAY[0]->ElementsShadow[x].PowerLevel = MAXIMUM_LEVEL ;
				}				
				
				//check that the total system power will not be exceeded by this change
				//subtract current element power from total and add new power level
				NewTotalPower = IRE_CLUSTER_ARRAY[0]->TotalPower - PowerTable[IRE_CLUSTER_ARRAY[0]->Elements[x].PowerLevel].Power + \
				PowerTable[NewPowerLevel].Power;
				//test if total exceeds the maximum
				if(NewTotalPower > MAX_POWER)
				{
					//reset the newpowerlevel to the pcurrent
					NewPowerLevel =  IRE_CLUSTER_ARRAY[0]->Elements[x].PowerLevel;
						//truncate the shadow power level	to the current level
					IRE_CLUSTER_ARRAY[0]->ElementsShadow[x].PowerLevel =	NewPowerLevel;
				}
				else
				{
					IRE_CLUSTER_ARRAY[0]->TotalPower = NewTotalPower;
				}
	 							
				IRE_CLUSTER_ARRAY[0]->Elements[x].PowerLevel = NewPowerLevel ;
				
				//save the cycle time for this update
				IRE_CLUSTER_ARRAY[0]->Elements[x].LastUpdateCycleID = ZeroCrossCycleId;
			}
			
			//store the max triger count
		//	IRE_CLUSTER_ARRAY[0]->Elements[x].MaxTrigger = IRE_CLUSTER_ARRAY[0]->Elements[x].TriggerCount;
			IRE_CLUSTER_ARRAY[0]->Elements[x].TriggerCount = 0;	
		}
		
	//	CURRENT_SLOT = 0;
		
}

