#include "MotorDriver.hpp"
#include <iostream>
int main(){
    MotorDriver m(9);
    m.setSpeed(0.6);
    std::cout << m.info() << std::endl;
    return 0;
}
