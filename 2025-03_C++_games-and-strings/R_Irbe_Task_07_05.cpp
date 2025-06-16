/* Šī programma izvada lielākā veselā skaitļa ciparu daudzumu, izvada lietotāja ievadīto skaitļa ciparu daudzumu
* un no šī ievadītā skaitļa atgriež n-to skaitli no labās puses.
* Rihards Irbe ITB1
* 7. nodarbība, 5 uzdevums
* Pēdejais izmaniņas datums: 17/03/2025
*/



#include <iostream>
#include <string>
#include <limits>
using namespace std;

//Aprēķina cik cipari atrodās padotajā skaitlī.
unsigned ciparu_skaits(unsigned long long skaitlis) {
    unsigned skaits = 0;

    while (skaitlis != 0) {
        skaitlis /= 10;
        skaits++;
    }

    return skaits;
}

//Atgriež padotā skaitļa n-to skaitli no labās puses.
int cipars(unsigned long long skaitlis, unsigned n) {
    string skaitlis_str = to_string(skaitlis);

    if (n > skaitlis_str.length()) {
        return -1;
    }else {
        return skaitlis_str[skaitlis_str.length() - n] - '0';
    }
}

int main() {
    unsigned long long a;
    unsigned n;
    bool validation = false;

    cout << "3 noc 1: " << ciparu_skaits(numeric_limits<unsigned long long>::max()) << endl;

    cout << "ievadi veselu nenegativu skaitli";
    cin >> a;
    cout << "3 noc 2: " << ciparu_skaits(a) << endl;

    while (validation == false) {
        cout << "ievadi naturalu skaitli n (n <= 20)";
        cin >> n;
        if (n > 0 && n <= 20 && n <= to_string(a).length()) {
            cout << "3 noc 3: " << cipars(a, n) << endl;
            validation = true;
        }else {
            cout << "Nepareizi ievadiji skaitli!" << endl;
        }
    }
}
