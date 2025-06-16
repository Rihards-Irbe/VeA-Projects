/* Šī programma ļauj lietotājam iegādāties vienu no pieejamām sēdvietām, kā arī izprintē groza saturu.
* Visām šīm darbībām ir lietotājam draudzīga saskarne.
* Rihards Irbe ITB1
* 8. nodarbība, 8 uzdevums
* Pēdejais izmaniņas datums: 03/04/2025
*/


#include <iostream>
using namespace std;

const int ROW{8}, COL{12}, MAX_ORDERS{20};

//izprintē pieejamās vietas ar to cenām un atzīmē aizņemtās vietas ar "xx"
void available_spaces_layout(int bieletes[ROW][COL], string vietas[ROW][COL]) {
    string numeration{"   "}, lines{"---|"};
    for (int i = 0; i < COL; i++) {
        if (i < 10) {
            numeration += "  " + to_string(i + 1);
        } else {
            numeration += " " + to_string(i + 1);
        }
    }
    for (int i = 4; i < numeration.length(); i++) {
        lines += "-";
    }

    cout << numeration << endl;
    cout << lines << endl;
    for (int i = 0; i < ROW; i++) {
        cout << " " << (i + 1) << " | ";
        for (int j = 0; j < COL; j++) {
            if (vietas[i][j] == "b") {
                cout << bieletes[i][j] << " ";
            }else {
                cout << "xx" << " ";
            }
        }
        cout << endl;
    }
}

/*Līdzīgi, kā tabulas ģenerēšanas funkciju, varu iekopēt funkciju un tā pildīs savu pienākumu katrā uzdevumā.
 *Funkcija validē padotos datus un atgriež padoto vērtību, ja visi nosacījumi sakrīt. */
int validation(int expected_answer_1, int expected_answer_2, string error_message, string input_message, bool range=false) {
    while (true) {
        int user_input;
        cout << input_message << endl;
        cin >> user_input;

        if (range) {
            if (user_input >= expected_answer_1 && user_input <= expected_answer_2) {
                return user_input;
            }else {
                cout << error_message << endl;
            }
        }else {
            if (user_input == expected_answer_1 || user_input == expected_answer_2) {
                return user_input;
            }else {
                cout << error_message << endl;
            }
        }
    }
}

/*Šo funkciju izmantoju katram uzdevumam, kas pieprasa tabulas izvadi.
 *Planoju turpināt attīstīt šo funkciju, lai varētu viņu pielietot vairākos gadījumos. */
void universal_generate_table(string header_values[], int header_arr_size, string values[][3], int actual_rows, bool calculate_total=false) {
    int const desiered_table_width{52}; //!Value needs to be adjusted if any one of tables contents is out of width!
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
    int user_input_row, user_input_col, user_input;
    string user_orders[MAX_ORDERS][3];
    int order_count = 0;
    string admin_account = "admin, admin";

    int teatra_biletes[ROW][COL] = {
        {40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40},
        {40, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 40},
        {40, 40, 50, 50, 50, 50, 50, 50, 50, 50, 40, 40},
        {40, 40, 50, 50, 50, 50, 50, 50, 50, 50, 40, 40},
        {30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 30, 30},
        {30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 30, 30},
        {30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30},
        {20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20},
        };

    string teatra_vietas[ROW][COL] = {
        {"b", "a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b"},
        {"b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"},
        {"b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"},
        {"b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"},
        {"b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"},
        {"b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"},
        {"b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"},
        {"b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"},
        };

    while (true) {

        user_input = validation(1,2, "Nepareiza ievade izvelies 1 - 2!", "Izvelies (1) pirksi biletes vai (2) partrauksi bilesu pirksanu: ");
        if (user_input == 1) {
            available_spaces_layout(teatra_biletes, teatra_vietas);

            user_input_row = validation(0,8, "Nepareiza ievade, jaizvelas rinda no 1 - 8 (Ievadi 0, ja velies atgreizties)!", "Izvelies rindu no 1 - 8: ", true);
            if (user_input_row == 0) {
                continue;
            }

            user_input_col = validation(0,12,  "Nepareiza ievade, jaizvelas rinda no 1 - 12 (Ievadi 0, ja velies atgreizties)!", "Izve1lies vietu no 1 - 12: ", true);
            if (user_input_col == 0) {
                continue;
            }

            user_input_row--;
            user_input_col--;
            if (teatra_vietas[user_input_row][user_input_col] == "b") {
                teatra_vietas[user_input_row][user_input_col] = "r";

                user_orders[order_count][0] = to_string(user_input_row + 1);
                user_orders[order_count][1] = to_string(user_input_col + 1);
                user_orders[order_count][2] = to_string(teatra_biletes[user_input_row][user_input_col]); // Price
                order_count++;

                if (order_count >= MAX_ORDERS) {
                    cout << "Maximum number of orders reached!" << endl;
                    break;
                }
            }else {
                string status;
                if (teatra_vietas[user_input_row][user_input_col] == "a") {
                    status = "aiznemta";
                }else if (teatra_vietas[user_input_row][user_input_col] == "r") {
                    status = "rezerveta";
                }
                cout << "Si vieta ir: " << status << " izvelies vietu, kura ir atzimeta ar cenu" << endl;
            }
        }else if (user_input == 2) {
            if (order_count == 0) {
                cout << "Jusu grozs ir tukss" << endl;
                continue;
            }

            string headers[] = {"Rindas nr", "Vietas nr", "Cena"};

            universal_generate_table(headers, (sizeof(headers) / sizeof(headers[0])), user_orders, order_count, true);

            user_input = validation(0,8, "Nepareiza ievade izvelies 1 - 2!", "Izvelies ievadi 1 vai 2 (1 - velies apstiprinat bilesu iegadi un 2 - atteikties no bilesu iegades)", true);
            if (user_input == 1) {

                int row_to_set, col_to_set;
                for (int i = 0; i < order_count; i++) {
                    row_to_set = stoi(user_orders[i][0]) - 1;
                    col_to_set = stoi(user_orders[i][1]) - 1;

                    teatra_vietas[row_to_set][col_to_set] = "a";
                }

                string username, password;
                cout << "Ievadi lietotajvardu: " << endl;
                cin >> username;
                cout << "Ievadi paroli: " << endl;
                cin >> password;

                if (admin_account == username + ", " + password) {
                    cout << "Programma partraukta";
                    break;
                }

            }else {
                int row_to_remove, col_to_remove;
                for (int i = 0; i < order_count; i++) {
                    row_to_remove = stoi(user_orders[i][0]) - 1;
                    col_to_remove = stoi(user_orders[i][1]) - 1;

                    teatra_vietas[row_to_remove][col_to_remove] = "b";
                }

                order_count = 0;
            }

        }
    }

    return 0;
}