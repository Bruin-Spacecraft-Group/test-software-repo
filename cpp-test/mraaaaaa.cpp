#include "adxl345.hpp"
#include <iostream>
#include <string>
#include <unistd.h>

using namespace std;

#define ADXL_BUS = 0; // TODO: figure out what a bus is

int flag = true;

int main() {
  Adxl345 accel (ADXL_BUS);
  while (flag) {
    float* vals = accel.getAcceleration();
    cout << "(" << vals[0] << "," << vals[1] << "," << vals[2] << ")" << endl;
    usleep(1000000);
  }
}