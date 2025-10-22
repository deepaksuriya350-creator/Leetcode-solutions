#include <stdio.h>
#include <stdbool.h>

#define MAX 100

typedef struct {
    int data[MAX];
    int front;
    int rear;
} Queue;

void initQueue(Queue *q) {
    q->front = 0;
    q->rear = 0;
}

bool isEmptyQueue(Queue *q) {
    return q->front == q->rear;
}

void enqueue(Queue *q, int x) {
    q->data[q->rear++] = x;
}

int dequeue(Queue *q) {
    return q->data[q->front++];
}

int frontQueue(Queue *q) {
    return q->data[q->front];
}

typedef struct {
    Queue q1;
    Queue q2;
} MyStack;

MyStack* myStackCreate() {
    MyStack* stack = (MyStack*)malloc(sizeof(MyStack));
    initQueue(&stack->q1);
    initQueue(&stack->q2);
    return stack;
}

void myStackPush(MyStack* obj, int x) {
    enqueue(&obj->q2, x);
    while (!isEmptyQueue(&obj->q1)) {
        enqueue(&obj->q2, dequeue(&obj->q1));
    }
    Queue temp = obj->q1;
    obj->q1 = obj->q2;
    obj->q2 = temp;
}

int myStackPop(MyStack* obj) {
    return dequeue(&obj->q1);
}

int myStackTop(MyStack* obj) {
    return frontQueue(&obj->q1);
}

bool myStackEmpty(MyStack* obj) {
    return isEmptyQueue(&obj->q1);
}

void myStackFree(MyStack* obj) {
    free(obj);
}
