/* Šī programma aprēķina vārda SCRABBLE vērtību, izmantojot noteiktus burtu vērtības noteikumus. Tā nejauši izvēlas burtu, lietotājam jāievada vārds, kas sākas ar šo burtu, un programma pārbauda ievades pareizību, aprēķina vārda vērtību un izvada rezultātu.
* Rihards Irbe ITB1
* 7. nodarbība, 6 uzdevums
* Pēdejais izmaniņas datums: 17/03/2025
*/



#include <iostream>
#include <string>
#include <cctype>
#include <cstdlib>
using namespace std;

//Atgriež viena burta SCRABBLE vērtību (0, ja tas nav derīgs burts)
int scrabble_letter_value(char character) {
    character = toupper(character);

    if (string("AEILNORSTU").find(character) != string::npos) {
        return 1;
    } else if (string("DG").find(character) != string::npos) {
        return 2;
    } else if (string("BCMP").find(character) != string::npos) {
        return 3;
    } else if (string("FHVWY").find(character) != string::npos) {
        return 4;
    } else if (character == 'K') {
        return 5;
    } else if (string("JX").find(character) != string::npos) {
        return 8;
    } else if (string("QZ").find(character) != string::npos) {
        return 10;
    } else {
        return 0;
    }
}

// Atgriež vārda kopējo SCRABBLE vērtību, saskaitot tā burtu vērtības.
int scrabble_word_value(string word) {
    int total_value = 0;
    for (int i = 0; i < word.length(); i++) {
        total_value += scrabble_letter_value(word[i]);
    }
    return total_value;
}

// Salīdzina vārda pirmo burtu ar doto burtu un atgriež 'true', ja tie sakrīt.
bool compare_first_letter(string word, char letter) {
    if (word.empty()) {
        return false;
    }
    return tolower(word[0]) == tolower(letter);
}

int main() {
    srand(time(0));
    char random_letter = 'A' + rand() % 26;
    string user_input;
    bool game_running = true;

    while (game_running) {
        cout << "Enter a word starting with letter '" << random_letter << "' ==> ";
        cin >> user_input;

        if (compare_first_letter(user_input, random_letter)) {
            int value = scrabble_word_value(user_input);
            cout << "Scrabble value: " << value << endl;
            break;
        } else {
            cout << "Incorrect input!" << endl;
        }
    }

    return 0;
}
