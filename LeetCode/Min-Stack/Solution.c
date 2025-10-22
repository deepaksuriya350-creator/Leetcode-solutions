#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX 30000

typedef struct {
    int data[MAX];
    int minData[MAX];
    int top;
} MinStack;

MinStack* minStackCreate() {
    MinStack* stack = (MinStack*)malloc(sizeof(MinStack));
    stack->top = -1;
    return stack;
}

void minStackPush(MinStack* obj, int val) {
    obj->top++;
    obj->data[obj->top] = val;
    if (obj->top == 0)
        obj->minData[obj->top] = val;
    else
        obj->minData[obj->top] = (val < obj->minData[obj->top - 1]) ? val : obj->minData[obj->top - 1];
}

void minStackPop(MinStack* obj) {
    if (obj->top >= 0)
        obj->top--;
}

int minStackTop(MinStack* obj) {
    return obj->data[obj->top];
}

int minStackGetMin(MinStack* obj) {
    return obj->minData[obj->top];
}

void minStackFree(MinStack* obj) {
    free(obj);
}
