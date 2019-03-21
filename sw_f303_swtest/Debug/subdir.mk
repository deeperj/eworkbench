################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../main.cpp 

OBJS += \
./main.o 

CPP_DEPS += \
./main.d 


# Each subdirectory must supply rules for building sources it contributes
%.o: ../%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: MCU G++ Compiler'
	@echo $(PWD)
	arm-none-eabi-g++ -mcpu=cortex-m4 -mthumb -mfloat-abi=softfp -mfpu=fpv4-sp-d16 '-DDEVICE_CRC=1' -DTARGET_STM32F303RE '-D__MBED__=1' '-DDEVICE_I2CSLAVE=1' '-D__FPU_PRESENT=1' '-DDEVICE_PORTOUT=1' '-DDEVICE_PORTINOUT=1' -DTARGET_RTOS_M4_M7 '-DDEVICE_RTC=1' '-DDEVICE_MPU=1' '-DDEVICE_SERIAL_ASYNCH=1' -D__CMSIS_RTOS -DTOOLCHAIN_GCC '-DDEVICE_CAN=1' -DTARGET_CORTEX_M '-DDEVICE_I2C_ASYNCH=1' -DTARGET_LIKE_CORTEX_M4 '-DDEVICE_ANALOGOUT=1' -DTARGET_M4 '-DCOMPONENT_PSA_SRV_IMPL=1' -DTARGET_NUCLEO_F303RE '-DDEVICE_SPI_ASYNCH=1' '-DDEVICE_LPTICKER=1' '-DDEVICE_PWMOUT=1' '-DDEVICE_INTERRUPTIN=1' -DTARGET_CORTEX '-DDEVICE_I2C=1' '-DTRANSACTION_QUEUE_SIZE_SPI=2' -D__CORTEX_M4 '-DDEVICE_STDIO_MESSAGES=1' -DTARGET_FF_MORPHO -DTARGET_FAMILY_STM32 -DTARGET_STM32F303xE -DTARGET_FF_ARDUINO '-DDEVICE_PORTIN=1' -DTARGET_RELEASE -DTARGET_STM '-DDEVICE_SERIAL_FC=1' '-DCOMPONENT_PSA_SRV_EMUL=1' '-DDEVICE_USTICKER=1' '-DMBED_BUILD_TIMESTAMP=1552841619.64' -DTARGET_LIKE_MBED -D__MBED_CMSIS_RTOS_CM '-DDEVICE_SLEEP=1' -DTOOLCHAIN_GCC_ARM '-DDEVICE_SPI=1' '-DCOMPONENT_NSPE=1' '-DDEVICE_SPISLAVE=1' -DTARGET_STM32F3 '-DDEVICE_ANALOGIN=1' '-DDEVICE_SERIAL=1' '-DDEVICE_FLASH=1' -DARM_MATH_CM4 -DMBED_DEBUG '-DMBED_TRAP_ERRORS_ENABLED=1' -DMBED_DEBUG '-DMBED_TRAP_ERRORS_ENABLED=1' -DNDEBUG -DNDEBUG -I"C:/Users/John/OneDrive - Phoenix Materials Testing Ltd/work/eworkbench/sw_f303_swtest/mbed" -I"C:/Users/John/OneDrive - Phoenix Materials Testing Ltd/work/eworkbench/sw_f303_swtest/mbed/TARGET_NUCLEO_F303RE/TOOLCHAIN_GCC_ARM" -I"C:/Users/John/OneDrive - Phoenix Materials Testing Ltd/work/eworkbench/sw_f303_swtest/mbed/drivers" -I"C:/Users/John/OneDrive - Phoenix Materials Testing Ltd/work/eworkbench/sw_f303_swtest/mbed/hal" -I"C:/Users/John/OneDrive - Phoenix Materials Testing Ltd/work/eworkbench/sw_f303_swtest/mbed/platform"  -includeC:/Users/John/OneDrive - Phoenix Materials Testing Ltd/work/eworkbench/sw_f303_swtest/mbed_config.h -O0 -funsigned-char -fno-delete-null-pointer-checks -fomit-frame-pointer -fmessage-length=0 -fno-builtin -g3 -Wall -Wextra -Wvla -Wno-unused-parameter -Wno-missing-field-initializers -ffunction-sections -fdata-sections -c -fno-exceptions -fno-rtti -ffunction-sections -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


