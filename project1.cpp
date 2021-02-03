#include <iostream>
#include <fstream>
#include <queue>
#include <vector>



//  My libs
#include "lib/Manager.cpp"
#include "../constants/priority.cpp"

//  Google things: C++ and function
//  Geeksforgeeks command line arguments in cpp

using namespace std;

string getNextWord(string command);
string getFirstWord(string command);

int main(int argc, char *argv[]) {


    //  Scope 1 (main)
    if(2 > 3) {

        //  Scope2 (if)
    }

    /*

    std::cout << "Hello world" << endl;
    printf("Hello again, what is your name?\n");

    string userName = "";

        //  One word input from user
       cin >> userName;
        char myString[32] = "blablabla";
         cout<< "Hello " << userName << " Welcome to the jungle" << endl;    //  tekur bara annað nafnið mitt
         printf("Hello %s welcome to the jungle!\n", userName.c_str());  // Converta yfir í char array
*/

/*

    //  Multi input from user
    getline(cin, userName);   //  Vill fá straum af gögnum/efni. Notum strauminn cin og setjum inn í strenginn username

    //  Get next word prufa
    printf("Complete sentence: %s, secondWord %s\n", userName.c_str(), getNextWord(userName).c_str());
    printf("First word: %s, secondWord %s\n", getFirstWord(userName).c_str(), getNextWord(userName).c_str());
*/

    if (argc > 1)
    {

    // ifstream myFile(argv[1]);

    // for(string line; getline(myFile, line);) {
    //     cout << line << endl;
    
    // }
    // }

    // cout << argc << endl;
    // cout << argv[1] << endl;;

    // //  Basic Class calling (One scope)
    // Manager myMan = Manager();
    // cout << myMan.getMyNumber() << endl;
    // myMan.setMyNumber(23);
    // cout << myMan.getMyNumber();

    // cout << "myMan2" << endl;

    // Manager myMan2 = Manager(1500);
    // cout << myMan2.getMyNumber() << endl;
    // myMan2.setMyNumber(23);
    // cout << myMan2.getMyNumber() << endl;

    // //  Class calling with pointer
    // Manager* myMan = new Manager();    // Pointer á manager breytu

    // cout << myMan << endl;
    // cout << myMan->getMyNumber() << endl;
    }

    //  Manager myMan = Manager();      GEYMA
    //  A process descriptor array PCB[16]
    queue<PCB*> processes;   //  H0ldum utan um alla PCBana sem er búið til. Viljum geyma pointera á þessu hér. Innihaldið á hverju staki hér er pointer.

    // processees.front()->test = 5; // Ef það væri fall inní pcb

    //  A RCB array of size 4

    queue<RCB*> resources;
    //  A ready list with priority levels 0,1,2
    //  An array of 3 elements would be ideal but vector is also good
   // queue<int> readyList;   //  Einfaldara væri að búa til array með 3 stökum, eða nota vector

    vector <queue<int>> readyList;  //  Vector af queue af integer

    //Lítur svona út

    /*

    { 1,2,3,4,5},
    {8},
    {0}
    */

    Manager myMan = Manager(&processes);
    myMan.create(PRIORITY_LOW);

    PCB* firstValue = processes.front();
    processes.pop();

    cout << processes.front() << endl;

    return 0;
}


//  Fall sem á að skila streng

string getNextWord(string command) {
    return command.substr(command.find(" ")+1);
}

string getFirstWord(string command) {

    return command.substr(0,command.find(" "));

}