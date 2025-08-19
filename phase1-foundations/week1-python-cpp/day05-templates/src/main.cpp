#include "Sensor.hpp"
#include <iostream>
int main(){
    Sensor<double> temp;
    temp.update(25.4);
    if (auto v = temp.read()) std::cout << "temp=" << *v << "\n";
    return 0;
}
