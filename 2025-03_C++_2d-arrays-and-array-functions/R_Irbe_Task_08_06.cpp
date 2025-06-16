/* Šī programma ļauj ar lietotāja pieskari veikt darbības ar masīviem (pievienot elementu un noņemt elementus).
 * šis masīvs nedrīkst pārsniegt 10 elementus.
* Rihards Irbe ITB1
* 8. nodarbība, 6 uzdevums
* Pēdejais izmaniņas datums: 03/04/2025
*/


#include <iostream>
using namespace std;

const int N{10};
int s{0};

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

//Itirēju caur masīvu un izprintēju to līdzīgā formātā, kā uzdevumā prasīts.
void print_array(int arr[], int array_size) {
    cout << "The array: " << endl;
    cout << "[ ";
    for (int i = 0; i < array_size; i++) {
        cout << arr[i] << " ";
    }
    cout << "]" << endl;
    cout << "The number of free places in the array: " << N - s << endl;
}

void BubbleSort (int arry[], int array_size) //https://www.shiksha.com/online-courses/articles/bubble-sort-in-c-blogId-156625
{
    int i, j;
    for (i = 0; i < array_size; ++i)
    {
        for (j = 0; j < array_size-i-1; ++j)
        {
            if (arry[j] > arry[j+1])
            {
                arry[j] = arry[j]+arry[j+1];
                arry[j+1] = arry[j]-arry[j + 1];
                arry[j] = arry[j]-arry[j + 1];
            }
        }
    }
}

//Ši funkcija atrod padoto elementu iekš masīva un noņem to, kā arī samaina masīva izmēru atbilstoši s vērtībai.
void remove_an_element_from_arr(int arr[], int array_size, int element_to_remove) {
    int i;
    bool found = false;
    for (i = 0; i < array_size; ++i) {
        if (arr[i] == element_to_remove) {
            found = true;
            s--;
            break;
        }
    }
    if (found) {
        for (int j = i; j < array_size - 1; ++j) {
            arr[j] = arr[j + 1];
        }
    }
}

int main() {
    int arr[N];
    int user_input;
    const char *TEXT = "(1) Add an element to the array.\n"
                       "(2) Remove the element from the array.\n"
                       "(3) Quit the program.\n"
                       "==> ";
    while (true) {

        user_input = validation(1,3, "Please provide a number between 1 and 3", TEXT, true);

        if (user_input == 1) {
            if (s < 10) {
                cout << "Enter the integer to add to the array ==> ";
                cin >> user_input;
                arr[s] = user_input;
                s++;
                BubbleSort(arr, s);
                print_array(arr, s);
            }else {
                cout << "Such action is not possible. The array is full.";
                print_array(arr, s);
            }
        } else if (user_input == 2) {
            if (s > 0) {
                cout << "Enter the integer to remove from the array ==> ";
                cin >> user_input;
                remove_an_element_from_arr(arr, s, user_input);

                BubbleSort(arr, s);
                print_array(arr, s);
            }else {
                cout << "This action is not possible. The array is empty." << endl;
            }

        } else if (user_input == 3) {
            cout << "Thank you for using this program! Goodbye!" << endl;
            cout << ":)";
            break;
        }

    }

}
