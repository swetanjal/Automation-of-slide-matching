#include "bits/stdc++.h"
using namespace std;

int main()
{
    cout << "Enter the path to the directory of test cases folder containing _rollno_.txt: " << endl;
    string s;
    cin >> s;
    if(s[s.size() - 1] == '/'){
        string command = "./sort.sh " + s + "_rollno_.txt";
        system(&command[0]);
    }
    else{
        string command = "./sort.sh " + s + "/_rollno_.txt";
        system(&command[0]);
    }
    ifstream f1("./c.txt");
    ifstream f2("./d.txt");
    int total = 0;
    int correct = 0;
    while(true){
        
        char a[256], b[256];
        for(int i = 0; i < 256; ++i){
            a[i] = '\0';
            b[i] = '\0';
        }
        f1.getline(a, 256);
        f2.getline(b, 256);
        if(a[0] == '\0')
            break;
        total++;
        if(strcmp(a, b) == 0)
            correct++;
        else{
            cout << "Participant's output: " << a << endl;
            cout << "Expected output:  "  << b << endl;
            cout << "********************************************************************************\n";
        }  
    }
    cout << "Number of Test Cases passed: " << correct << "/" << total << "(" << (correct * 100.0) / total << "%)" << endl;
    return 0;
}