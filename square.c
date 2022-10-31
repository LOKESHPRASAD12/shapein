#include<stdio.h>

float squareArea(float side);
float circleArea(float rad);
float rectangleArea(float a, float b);

int main(){
   
   float side1=12.0;
   float side2=10.0;
   
   printf("area is:%f",rectangleArea(side1, side2));
    return 0;
}
float squareArea(float side){
    float area=0;
    for(int i =0;i<side;i++)
    {
        area = area + side;
    }
    return(area);
}
float circleArea(float rad){
    float area=0;
    for(int i =0;i<rad;i++)
    {
        area = area + rad;
    }
    return 3.14*area;
}
float rectangleArea(float a, float b){
    float area=0;
    for(int i =0;i<a;i++)
    {
        area = area + b;
    }
    return area;
}
