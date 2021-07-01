/* --------------------------------------------------------------------- 

Module 3: Temperature Sense Unit with RTOS 

Two threads are implemented:  

1. Display an incrementing counter on the LCD  2. Blink the on-board LED 

*---------------------------------------------------------------------*/ 

 

#include "mbed.h" 

#define ENABLE 0x08         // ORed in to data value to strobe E bit 
#define COMMAND_MODE 0x00   //clears LCD RS line, for command transfer 
#define DATA_MODE 0x04      //sets LCD RS line to 1, for data transfer 

DigitalOut  led(LED1);      //Nucleo LED 
DigitalOut CS(D10);         //SPI Chip Select 
SPI ser_port(D11, D12, D13); //Initialise SPI, using default settings 

//Function Prototypes 
void clr_lcd(void); 
void init_lcd(void); 
void print_lcd(const char *string); 
void shift_out(int data); 
void write_cmd(int cmd); 
void write_data(char c); 
void write_4bit(int data); 

// Temp sensor variables
I2C temp_sensor(I2C_SDA, I2C_SCL); //Configure I2C interface 
BufferedSerial pc(USBTX, USBRX, 9600);  
const int temp_addr = 0x90; //I2C address of temperature sensor DS1631 
char commands[] = {0x51, 0xAA}; 
char read_temp[2]; 
char LCD_result[9];            //holds result to be displayed on LCD.  

// LED test brightness
PwmOut      LED_var(D3);          
AnalogIn    pot1(A0);  


//-------------- Threads -----------------// 


Thread thread1;   //Blink an LED 
void led1_thread(void const *args){ 
    led = 0; 
    while(true) { 
        led = !led; 
        thread_sleep_for (500); 
    } 
} 

Thread thread2; 
//Display a counter on the LCD 
void count_thread(void const *args){ 
    char k = 0; 
    while(1) { 
        write_cmd(0xc0);   //set cursor to start of second line 
        wait_us(40); 
        print_lcd("Count is "); 
        write_data(k|0x30); //OR in 0x30 to produce the ASCII code for k 
        k++; 
        if (k>9)k=0; 
        thread_sleep_for (1000); 
    } 
} 

Mutex lcd_mutex;
Thread thread3;
//Read temp and display on LCD 
void temp_thread(void const *args){ 
    while(1) { 
        lcd_mutex.lock(); 
//Write 0xAA to sensor to read the last converted temp 
        temp_sensor.write(temp_addr, &commands[1], 1, false);  
//Read temp into the read_temp array 
        temp_sensor.read(temp_addr, read_temp, 2);   
//Convert temp to Celsius. Shift MS byte right by 8 bits, OR in ls byte, 
  //then divide all by 256, with float result. 
        float temp = (float((read_temp[0]<<8)|read_temp[1])/256); 
//convert float to character string 
        sprintf(LCD_result, "%d.%d", int(temp), int((temp-int(temp))*10));  
        write_cmd(0x80);   //set cursor to start of first line 
        wait_us(40); 
        for (char i=0; i<4; i++) {   //write 5 characters from string 
            write_data(LCD_result[i]); 
            }           //end of for() 
        print_lcd(" degrees C"); 

//Write 0x51 to the DS1631 (address 0x90) to start next temp conversion 
        temp_sensor.write(temp_addr, &commands[0], 1, false); 
        lcd_mutex.unlock(); 
        thread_sleep_for(1000); 
    } 
}

Thread thread4;
void breadboardled_thread(void const *args){ 
    while(1) {
        LED_var = pot1;
    }
}

//----------- MAIN function---------------// 

int main(){ 
    init_lcd();  //Initialise the LCD display 
    clr_lcd();   //Clear the LCD 
    thread1.start(callback(led1_thread,&led)); 
    thread2.start(callback(count_thread,&ser_port)); 
    thread3.start(callback(temp_thread,&temp_sensor));
    thread4.start(callback(breadboardled_thread, &pot1));

    while(true) {                                //Wait for timer interrupt 
        __wfi(); 
    } 
} 

//----------------- LCD functions---------------------// 

void init_lcd(void){      //follow designated procedure in data sheet 
    thread_sleep_for (40); 
    shift_out(0x30);    //function set 8-bit 
    wait_us(37); 
    write_cmd(0x20);    //function set 
    wait_us(37); 
    write_cmd(0x20);    //function set 
    wait_us(37); 
    write_cmd(0x0C);    //display ON/OFF 
    wait_us(37); 
    write_cmd(0x01);    //display clear 
    wait_us(1520); 
    write_cmd(0x06);    //entry-mode set 
    wait_us(37); 
    write_cmd(0x28);    //function set 
    wait_us(37); 
} 

void write_4bit(int data, int mode){ //mode is RS line, cmd=0, data=1 
    int hi_n; 
    int lo_n; 
    hi_n = (data & 0xF0);  //form the two 4-bit nibbles that will be sent 
    lo_n = ((data << 4) &0xF0); 

//send each word twice, strobing the Enable line 
    shift_out(hi_n | ENABLE | mode);  
    wait_us(1); 
    shift_out(hi_n & ~ENABLE); 
    shift_out(lo_n | ENABLE | mode); 
    wait_us(1); 
    shift_out(lo_n & ~ENABLE); 
} 

void shift_out(int data){        //Sends word to SPI port 
    CS = 0; 
    ser_port.write(data); 
    CS = 1; 
} 

void write_cmd(int cmd){         //Configures LCD command word 
    write_4bit(cmd, COMMAND_MODE); 
} 

void write_data(char c){        //Configures LCD data word 
    write_4bit(c, DATA_MODE);    //1 for data mode 
} 

void clr_lcd(void){      //Clears display and waits required time 
    write_cmd(0x01);    //display clear 
    wait_us(1520); 
} 

void print_lcd(const char *string){  //Sends character string to LCD 
    while(*string) { 
        write_data(*string++); 
        wait_us(40); 
    } 
} 