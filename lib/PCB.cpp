#include "../constants/processStates.cpp"
#include <vector>

using namespace std;

class PCB
{
private:
    /* data */
    int _state;
    PCB* _parent;
    vector<PCB*> _children; //  listi
    int _resources;
    int _priority;  //  extended


public:
    PCB(int priority);
    ~PCB();
    void test();
};

PCB::PCB(int priority)
{
    //  State = READY
    _state = READY; //1
    _priority = priority;
}

PCB::~PCB()
{
}
