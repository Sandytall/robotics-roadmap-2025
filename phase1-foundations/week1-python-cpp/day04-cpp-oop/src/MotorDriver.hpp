#pragma once
#include <string>
class MotorDriver {
public:
    explicit MotorDriver(int pwm_pin): pwm_pin_(pwm_pin), speed_(0.0) {}
    void setSpeed(double s) { speed_ = s; }
    double speed() const { return speed_; }
    std::string info() const;
private:
    int pwm_pin_;
    double speed_;
};
