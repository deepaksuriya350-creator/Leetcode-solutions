#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *queue;
    int front;
    int rear;
    int size;
} RecentCounter;

RecentCounter* recentCounterCreate() {
    RecentCounter* obj = (RecentCounter*)malloc(sizeof(RecentCounter));
    obj->queue = (int*)malloc(sizeof(int) * 10000);
    obj->front = 0;
    obj->rear = -1;
    obj->size = 0;
    return obj;
}

int recentCounterPing(RecentCounter* obj, int t) {
    obj->rear++;
    obj->queue[obj->rear] = t;
    obj->size++;

    while (obj->queue[obj->front] < t - 3000) {
        obj->front++;
        obj->size--;
    }

    return obj->size;
}

void recentCounterFree(RecentCounter* obj) {
    free(obj->queue);
    free(obj);
}
