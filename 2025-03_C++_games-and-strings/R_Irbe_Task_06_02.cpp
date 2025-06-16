/* Šī programma simulē spēli, kur lietotājs un dators met 2 kauliņus. Šīem kauliņiem ir custom punktu sistēma,
*kur uzvar pirmais spēlētājs, kurš sasniedz req_points_to_win punktus (100 šinī gadījumā).
* Rihards Irbe ITB1
* 6. nodarbība, 2 uzdevums
* Pēdejais izmaniņas datums: 17/03/2025
*/



#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

//Atgriež nejaušu skaitli no a līdz b
int my_rand(int a, int b){

    return rand() % b + a;
}

//Šī funkcija atgriež custom punktus, balstoties uz abu mesto kauliņu rezultātu, lai padarītu šo spēli interesantāku
int point_calculation_requirements(int throw_1, int throw_2, int total_points) {
    if (throw_1 == throw_2 && throw_1 != 1 && throw_2 != 1) {
        return (throw_1 + throw_2) * 2;
    }else if (throw_1 == 1 && throw_2 != 1 || throw_1 != 1 && throw_2 == 1) {
        return 0;
    }else if (throw_1 == 1 && throw_2 == 1) {
        return -total_points;
    }else {
        return throw_1 + throw_2;
    }
}

int main() {
    int total_player_points, total_computer_points;
    int const req_points_to_win{100};
    bool game_running = true;
    srand(time(0));

    while (game_running) {
        int throw_1 = my_rand(1, 6), throw_2 = my_rand(1, 6);
        total_player_points += point_calculation_requirements(throw_1, throw_2, total_player_points);
        cout << "Lietotajs: " << throw_1 << " " << throw_2 << " | " << total_player_points << endl;
        throw_1 = my_rand(1, 6), throw_2 = my_rand(1, 6);
        total_computer_points += point_calculation_requirements(throw_1, throw_2, total_computer_points);
        cout << "Dators:    " << throw_1 << " " << throw_2 << " | " << total_computer_points << endl;

        if (total_computer_points > req_points_to_win) {
            game_running = false;
            break;
        }else if (total_player_points > req_points_to_win) {
            game_running = false;
            break;
        }
    }
    cout << endl;

    if (total_computer_points < total_player_points) {
        cout << "Lietotajs pirmais sasniedza " << req_points_to_win << " punktus!" << endl;
    }else {
        cout << "Dators pirmais sasniedza " << req_points_to_win << " punktus!" << endl;
    }

    cout << "Ieguti punkti: " << endl;
    cout << "Lietotajs: " << total_player_points << endl;
    cout << "Dators: " << total_computer_points << endl;
}
