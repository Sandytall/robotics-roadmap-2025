#include <thread>
#include <chrono>
#include <iostream>
void run(const char* name, int ms, int count){
    for(int i=0;i<count;++i){
        std::cout << "[" << name << "] " << i << "\n";
        std::this_thread::sleep_for(std::chrono::milliseconds(ms));
    }
}
int main(){
    std::thread a(run, "imu", 100, 8);
    std::thread b(run, "lidar", 250, 4);
    a.join(); b.join();
    std::cout << "done\n";
    return 0;
}
