#ifndef ringBuffer_H
#define ringBuffer_H

#define RINGBUF_SIZE 1024
class RingBuffer
{
public:
    RingBuffer();
    float write(float value);
    float read(void);
    RingBuffer *getBufPtr(void);
    void rewriteBuf(RingBuffer *oldRingBuffer);
    float data[RINGBUF_SIZE];
        int readTail(void);
        void writeTail(int tailVal);
    int avail(void);

protected:
    int tail;
    int head;
    int end;
    int readHead(void);
        int fillCount;
};

#endif
