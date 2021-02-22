#include <iostream>
#include "PCB.cpp"
#include "RCB.cpp"
#include <queue>

using namespace std;

//  Hafa föll í private þangað til einhver notar þau
class Manager
{
private:
    /* data */
    int _myNumber;
    void destroy();
    void request();
    void release();
    void timeout(); // in here?
    void scheduler();
    void init();
    queue<PCB*> *_processees;


public:
    Manager(/* args */);
    Manager(int myNumber);
    Manager(queue<PCB*> *processees);     //  Staðsetning á vinnsluminni
    ~Manager();

    int getMyNumber();
    void setMyNumber(int);

    // void create(int priority);
    void create();

};


//  Constructor. Byrjar að keyra þetta þegar maður býr til nýtt tilvik af klasa.
//  Call by reference, processes is created someplace else
Manager::Manager(queue<PCB*> *processees)
{
    _processees = processees;
    cout << "Manager was created" << endl;
}


//  Destructor. Þegar maður eyðir tilviki af klasa
Manager::~Manager()
{
    cout << "Manager was destructed." << endl;

    //  TODO: Delete all new PCB
    //  TODO: 
    for (size_t i = 0; i < _processees-> size(); i++)
    {
        delete _processees->front;
    }
}

int Manager::getMyNumber() {
    return _myNumber;
}

void Manager::setMyNumber(int myNumber) {
    cout << myNumber << endl;
    return;
}


//  Á að núlstilla forritið. Input frá notanda (skrá), á að vera hægt að núllstilla alla lista
void Manager::init() {

}


void Manager::create() {

    //  Allocate new PCB[j]

    //  Hér er hluturinn búinn til út fyrir (heap). Deletast ekki nema að við köllum sérstaklega í delete
    PCB *myNewPCB = new PCB();

    _processees ->push(myNewPCB);

    //  When we finish using everything that was created with the keyword new, we must delete it from the memory heap
    // delete myNewPCB;        //  Til þess að deleta. Annars verður minnisleki

    //  Þetta er geymt í vinnsluminninu sem er bara fyrir þetta fall
    // PCB myNewPCB = PCB() //  Virkar ekki



    //  state = ready

    //  Gera þetta í construnctorinum á PCB


    //  insert j into list of children of i
    //  (j is the new process, i is its parent)
    //  Verkefnið snýst svolítið um að búa til bókhald og passa að gögnin stemmi




    
    //  parent = i
    //  children = null
    //  insert j into RL (ready list)
    //  display "process j created"


    

}