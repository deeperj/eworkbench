#!/bin/bash

arm-none-eabi-gcc -c -mcpu=cortex-a8 hw-entry.c -o hw-entry.o

arm-none-eabi-as -mcpu=cortex-a8 hw-startup.s -o hw-startup.o

arm-none-eabi-ld -T hw-boot.ld hw-entry.o hw-startup.o -o hw-boot.elf

arm-none-eabi-objcopy -O binary hw-boot.elf hw-boot.bin

arm-none-eabi-objdump -d hw-boot.elf
