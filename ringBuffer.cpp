#include "mbed.h"
#include "ringBuffer.h"

/* Constructor should initialize the ring buffer */
RingBuffer::RingBuffer()
{
    head = 0; // write at the head
    tail = 0; // read from the tail
    end = RINGBUF_SIZE-1;
      fillCount = 0;
}

/* Write one float to the head of the ring buffer */
float RingBuffer::write(float value)
{
    // if we've reached the end of the linear array, loop around to begining
    if(head > end) {
        head = 0;
        }

    // write a single float into the buffer, increment the head and adjust the fill count
        data[head] = value;
        head++;
        fillCount++;
    return value;
}

/* Read one float from the tail of ring buffer */
float RingBuffer::read(void)
{
    float returnValue;

    // tail is beyond the end of the linear buffer, so wrap it back around
    if(tail > end) {
        tail = 0;
    }
        // read a single float from the buffer, incrememnt tail, and adjust fill count
        returnValue = data[tail];
        tail++;
        fillCount--;

    return returnValue;
}

/* Return the tail. */
int RingBuffer::readTail(void)
{
    return tail;
}

/* Write a new tail value. */
void RingBuffer::writeTail(int tailVal)
{
    tail = tailVal;
}

/* Return the head. */
int RingBuffer::readHead(void)
{
    return head;
}

/* Return a pointer to the entire object. */
 RingBuffer* RingBuffer::getBufPtr(void)
{
    return this;
}

/* Rewrite the entire buffer object. */
void RingBuffer::rewriteBuf(RingBuffer *oldRingBuffer)
{
    memcpy(this, oldRingBuffer, sizeof(RingBuffer));
}

/* Return the fill count to indicate if there is any new data in the buffer */
int RingBuffer::avail(void)
{
    return fillCount;
}
