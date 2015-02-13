/*
Read analog pin and spew data over serial.
*/
#include "imuData.h"
#include "mbed.h"
#include "ringBuffer.h"

#define mbedSF 3.3
#define pcBaud 115200

AnalogIn xGyro(p15), yGyro(p16), xAccel(p17), yAccel(p18), zAccel(p19);
DigitalOut led1(LED1);
BusOut unused(p20);
Serial pc(USBTX,USBRX);
Ticker timerInterrupt;
tImuData imuData;     // Struct for holding the IMU's data
float readVal;
RingBuffer ringBuf;
RingBuffer ringBufMemSafe;
float testVal;
float returnVal;

void measure(void)
{
    //TODO: write data to ring buffer, set flag and printf from main
    ringBuf.write(xGyro.read()*mbedSF);
    ringBuf.write(yGyro.read()*mbedSF);
    ringBuf.write(xAccel.read()*mbedSF);
    ringBuf.write(yAccel.read()*mbedSF);
    ringBuf.write(zAccel.read()*mbedSF);

    led1 != led1;
    
    //returnVal = ringBuf.write(testVal);
    //testVal++;
}

int main(void)
{
    pc.baud(pcBaud);
    timerInterrupt.attach(&measure,.01); //100Hz

    while(1) {
            if(ringBuf.avail()) {
        // make memory safe
              int oldTail = ringBufMemSafe.readTail(); // need to keep track of where we are reading from
        ringBufMemSafe.rewriteBuf(ringBuf.getBufPtr()); // put a copy of the data into the memory safe instance;
              ringBufMemSafe.writeTail(oldTail);
              pc.printf("%f,%f,%f,%f,%f\n",ringBufMemSafe.read(),ringBufMemSafe.read(),ringBufMemSafe.read(),ringBufMemSafe.read(),ringBufMemSafe.read());
    }
    }
}
