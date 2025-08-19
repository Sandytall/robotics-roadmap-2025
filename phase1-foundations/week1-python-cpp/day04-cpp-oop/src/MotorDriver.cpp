#include "MotorDriver.hpp"
#include <sstream>
std::string MotorDriver::info() const {
    std::ostringstream oss;
    oss << "MotorDriver(pin=" << pwm_pin_ << ", speed=" << speed_ << ")";
    return oss.str();
}
