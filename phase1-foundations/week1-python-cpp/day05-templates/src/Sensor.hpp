#pragma once
#include <optional>
template<typename T>
class Sensor {
public:
    std::optional<T> read() const { return last_; }
    void update(const T& v) { last_ = v; }
private:
    std::optional<T> last_;
};
