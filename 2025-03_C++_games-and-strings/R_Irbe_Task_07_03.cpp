/* Šī programma izvada no lietotāja ievadīto string 10 random burtus.
* Rihards Irbe ITB1
* 7. nodarbība, 3 uzdevums
* Pēdejais izmaniņas datums: 17/03/2025
*/



#include <iostream>
using namespace std;

//Atgriež nejaušu skaitli no a līdz b
int my_rand(int a, int b){

    return rand() % b + a;
}

//Atgriež nejaušas izvēles burtu no stringa
char random_choice(string s) {
    return s[my_rand(0, (s.length() - 1))];
}

int main() {
    srand(time(0));
    string argument_string{"Rihards"};

    cout << "Ievadi rakstzimju virkni bez atstarpem: " << endl;
    cin >> argument_string;
    for(int i = 0; i < 10; i++) {
        cout << random_choice(argument_string);
    }
}
