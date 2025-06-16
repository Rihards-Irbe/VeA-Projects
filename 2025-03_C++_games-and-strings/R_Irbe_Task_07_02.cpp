/* Šī programma izvada tabulā datus ar metamā kauliņa katra cipara biežumu procentuāli. Šinī gadījumā tiek simulētas
* 100 metamo kauliņu situācijas.
* Rihards Irbe ITB1
* 7. nodarbība, 2 uzdevums
* Pēdejais izmaniņas datums: 17/03/2025
*/



#include <iostream>
#include <iomanip>
#include <ctime>
#include <string>
using namespace std;

//Atgriež nejaušu skaitli no a līdz b
int my_rand(int a, int b){

    return rand() % b + a;
}

//Šo funkciju izveidoju, lai varētu iekopēt šo funkciju un izprintēt automātiski formatētu tabulu, vienkārši padodot headers/augšas vērtības un datus.
void universal_generate_table(string header_values[], int header_arr_size, string values[6][3]) {
    int const desiered_table_width{44};
    string header_combined_text, line_string;

    for (int i = 0; i < header_arr_size; i++) {
        header_combined_text += header_values[i];
    }
    if (header_combined_text.length() > desiered_table_width) {
        cout << "Too many provided header values to make a table with desiered width of: " << desiered_table_width << endl;
    }else if (desiered_table_width % 2 != 0) {
        cout << "Desiered table width has to be an even number (because of formatting issues): " << desiered_table_width << endl;
    }else {
        double width_math = (desiered_table_width - header_combined_text.length()) / header_arr_size;
        int width = (int)(width_math + 0.5);
        int total_width = (width * header_arr_size) + header_combined_text.length() + width;

        string spaces;
        for (int i = 0; i < total_width; i++) {
            line_string += "-";
        }
        for (int i = 0; i < width; i++) {
            spaces += " ";
        }
        cout << line_string << endl;
        for (int i = 0; i < header_arr_size; i++) {
            if (i == 0) {
                cout << "|" << spaces.substr(0, spaces.length() - 1) << header_values[i];
            }else if (i == header_arr_size - 1) {
                cout << spaces << header_values[i] << spaces.substr(0, spaces.length() - 1) << "|";
            }else {
                cout << spaces << header_values[i];
            }
        }
        cout << endl;
        cout << line_string << endl;

        for (int i = 0; i < 6; i++) {
            if (i != 0){
            cout << endl;
            }
            for (int j = 0; j < header_arr_size; j++) {
                int value_length = values[i][j].length();
                int spaces_total = total_width / header_arr_size - value_length;

                string spaces_left, spaces_right;

                for (int x = 0; x < spaces_total / 2; x++) {
                    spaces_left += " ";
                }
                for (int y = 0; y < spaces_total - (spaces_total / 2); y++) {
                    spaces_right += " ";
                }

                if (j == 0) {
                    cout << "|" << spaces_left << values[i][j] << spaces_right;
                } else if (j == header_arr_size - 1) {
                    cout << spaces_left << values[i][j] << spaces_right << "|";
                } else {
                    cout << spaces_left << values[i][j] << spaces_right;
                }
            }
        }
    }
    cout << endl;
    cout << line_string << endl;
}

int main() {
    srand(time(0));
    int one_dropped{0}, two_dropped{0}, three_dropped{0}, four_dropped{0}, five_dropped{0}, six_dropped{0};
    double one_dropped_perc{0}, two_dropped_perc{0}, three_dropped_perc{0}, four_dropped_perc{0}, five_dropped_perc{0}, six_dropped_perc{0};
    int loop_times{100};

    for (int i = 0; i < loop_times; i++) {
        int dropped_number = my_rand(1, 6);
        switch (dropped_number) {
            case 1:
                one_dropped ++;
            break;
            case 2:
                two_dropped++;
            break;
            case 3:
                three_dropped++;
            break;
            case 4:
                four_dropped++;
            break;
            case 5:
                five_dropped++;
            break;
            case 6:
                six_dropped++;
            break;
        }
    }

    one_dropped_perc = (one_dropped * 1.0 / loop_times) * 100;
    two_dropped_perc = (two_dropped * 1.0 / loop_times) * 100;
    three_dropped_perc = (three_dropped * 1.0 / loop_times) * 100;
    four_dropped_perc = (four_dropped * 1.0 / loop_times) * 100;
    five_dropped_perc = (five_dropped * 1.0 / loop_times) * 100;
    six_dropped_perc = (six_dropped * 1.0 / loop_times) * 100;

    string headers[3] = {"Number", "Dropped (Times)", "Percentage"};
    string table_values[6][3] = {
        {"1", to_string(one_dropped), to_string(one_dropped_perc) + "%"},
        {"2", to_string(two_dropped), to_string(two_dropped_perc) + "%"},
        {"3", to_string(three_dropped), to_string(three_dropped_perc) + "%"},
        {"4", to_string(four_dropped), to_string(four_dropped_perc) + "%"},
        {"5", to_string(five_dropped), to_string(five_dropped_perc) + "%"},
        {"6", to_string(six_dropped), to_string(six_dropped_perc) + "%"}
    };
    universal_generate_table(headers, (sizeof(headers) / sizeof(headers[0])), table_values);
}
