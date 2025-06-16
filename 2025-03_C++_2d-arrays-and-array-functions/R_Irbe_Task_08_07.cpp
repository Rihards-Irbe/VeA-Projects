/* Šī programma izvada tabulā katras valsts medaļas, medaļu skaitu un kopējos punktus, kā arī izvada valstis
* ar vislielāko punktu skaitu.
* Rihards Irbe ITB1
* 8. nodarbība, 7 uzdevums
* Pēdejais izmaniņas datums: 03/04/2025
*/


#include <iostream>
using namespace std;

const int COUNTRIES{7}, MEDALS{3};

/*Šo funkciju izmantoju katram uzdevumam, kas pieprasa tabulas izvadi.
 *Planoju turpināt attīstīt šo funkciju, lai varētu viņu pielietot vairākos gadījumos. */
void universal_generate_table(string header_values[], int header_arr_size, string values[][6], int actual_rows, bool calculate_total=false) {
    int const desiered_table_width{58}; //!Value needs to be adjusted if any one of tables contents is out of width!
    int total_spaces{0}, total_price{0}, space_right_width{0};
    bool calculate_once = false;
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

        for (int i = 0; i < actual_rows; i++) {
            if (i != 0){
            cout << endl;
            }
            for (int j = 0; j < header_arr_size; j++) {
                int value_length = values[i][j].length();
                int spaces_total = total_width / header_arr_size - value_length;

                if (calculate_total == true && calculate_once == false) {
                    for (int x = 0; x < header_arr_size; x++) {
                        total_spaces += values[i][x].length();
                    }
                    total_spaces += (spaces_total / 2) * header_arr_size + (spaces_total - (spaces_total / 2)) * header_arr_size;
                    calculate_once = true;
                }

                string spaces_left, spaces_right;

                for (int x = 0; x < spaces_total / 2; x++) {
                    spaces_left += " ";
                }

                for (int y = 0; y < spaces_total - (spaces_total / 2); y++) {
                    spaces_right += " ";
                }
                space_right_width = spaces_right.length();

                if (j == 0) {
                    cout << "|" << spaces_left << values[i][j] << spaces_right;
                } else if (j == header_arr_size - 1) {
                    cout << spaces_left << values[i][j] << spaces_right << "|";
                    if (calculate_total) {
                        total_price += stoi(values[i][j]);
                    }

                } else {
                    cout << spaces_left << values[i][j] << spaces_right;
                }
            }
        }

        cout << endl;
        cout << line_string << endl;

        if (calculate_total) {
            string calculated_text = "Total price:";
            string total_price_str = to_string(total_price);
            string right_formatting;

            int spaces_needed = total_width - calculated_text.length() - total_price_str.length() - space_right_width - 3;

            string total_space_str;
            for (int x = 0; x < spaces_needed; x++) {
                total_space_str += " ";
            }

            for (int y = 0; y < space_right_width; y++) {
                right_formatting += " ";
            }

            cout << "| " << calculated_text << total_space_str << total_price << right_formatting << "|" << endl;
            cout << line_string << endl;
        }
    }
}

/*Dēļ atšķirīgu tabulas rindu izmēru man nācās šo funkciju nokopēt un samainīt masīva izmēru. Noteikti pārveidošu
 *šo funkciju, lai varētu padot vektoru nevis arrayu, lai šādi gadījumi neatkārtotos. */
void universal_generate_table_2(string header_values[], int header_arr_size, string values[][8], int actual_rows, bool calculate_total=false) {
    int const desiered_table_width{106}; //!Value needs to be adjusted if any one of tables contents is out of width!
    int total_spaces{0}, total_price{0}, space_right_width{0};
    bool calculate_once = false;
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

        for (int i = 0; i < actual_rows; i++) {
            if (i != 0){
            cout << endl;
            }
            for (int j = 0; j < header_arr_size; j++) {
                int value_length = values[i][j].length();
                int spaces_total = total_width / header_arr_size - value_length;

                if (calculate_total == true && calculate_once == false) {
                    for (int x = 0; x < header_arr_size; x++) {
                        total_spaces += values[i][x].length();
                    }
                    total_spaces += (spaces_total / 2) * header_arr_size + (spaces_total - (spaces_total / 2)) * header_arr_size;
                    calculate_once = true;
                }

                string spaces_left, spaces_right;

                for (int x = 0; x < spaces_total / 2; x++) {
                    spaces_left += " ";
                }

                for (int y = 0; y < spaces_total - (spaces_total / 2); y++) {
                    spaces_right += " ";
                }
                space_right_width = spaces_right.length();

                if (j == 0) {
                    cout << "|" << spaces_left << values[i][j] << spaces_right;
                } else if (j == header_arr_size - 1) {
                    cout << spaces_left << values[i][j] << spaces_right << "|";
                    if (calculate_total) {
                        total_price += stoi(values[i][j]);
                    }

                } else {
                    cout << spaces_left << values[i][j] << spaces_right;
                }
            }
        }

        cout << endl;
        cout << line_string << endl;

        if (calculate_total) {
            string calculated_text = "Total price:";
            string total_price_str = to_string(total_price);
            string right_formatting;

            int spaces_needed = total_width - calculated_text.length() - total_price_str.length() - space_right_width - 3;

            string total_space_str;
            for (int x = 0; x < spaces_needed; x++) {
                total_space_str += " ";
            }

            for (int y = 0; y < space_right_width; y++) {
                right_formatting += " ";
            }

            cout << "| " << calculated_text << total_space_str << total_price << right_formatting << "|" << endl;
            cout << line_string << endl;
        }
    }
}

int main() {
    string headers[] = {"Country", "Gold", "Silver", "Bronze", "Total", "Points"};

    int medal_counts[COUNTRIES][MEDALS] = {
        {1, 0, 1},
        {1, 1, 0},
        {0, 0, 1},
        {1, 0, 0},
        {0, 1, 1},
        {0, 1, 1},
        {1, 1, 0}
    };

    string countries[COUNTRIES] = {"Canada", "China", "Germany", "Korea", "Japan", "Russia", "USA"};
    string table_values[COUNTRIES][MEDALS + 3];

    for (int i = 0; i < COUNTRIES; i++) {
        int total_medals{0}, total_points{0};

        table_values[i][0] = countries[i];

        for (int j = 0; j < MEDALS; j++) {
            table_values[i][j + 1] = to_string(medal_counts[i][j]);
            total_medals += medal_counts[i][j];

            if (j == 0) total_points += medal_counts[i][j] * 4;
            else if (j == 1) total_points += medal_counts[i][j] * 2;
            else if (j == 2) total_points += medal_counts[i][j] * 1;
        }

        table_values[i][4] = to_string(total_medals);
        table_values[i][5] = to_string(total_points);
    }

    universal_generate_table(headers, 6, table_values, COUNTRIES);

    string headers_2[] = {"Medal", "Canada", "China", "Germany", "Korea", "Japan", "Russia", "USA"};
    string medal_types[MEDALS] = {"Gold", "Silver", "Bronze"};
    string table_values_2[MEDALS][COUNTRIES + 1];

    for (int i = 0; i < MEDALS; i++) {
        table_values_2[i][0] = medal_types[i];

        for (int j = 0; j < COUNTRIES; j++) {
            table_values_2[i][j + 1] = to_string(medal_counts[j][i]);
        }
    }

    universal_generate_table_2(headers_2, 8, table_values_2, MEDALS);

    int max_points = 0;

    for (int i = 0; i < COUNTRIES; i++) {
        int total_points = stoi(table_values[i][5]);
        if (total_points > max_points) {
            max_points = total_points;
        }
    }

    cout << "The country or countries with the most points " << endl;
    for (int i = 0; i < COUNTRIES; i++) {
        int total_points = stoi(table_values[i][5]);
        if (total_points == max_points) {
            cout << countries[i] << ": " << total_points << endl;
        }
    }

    return 0;
}
