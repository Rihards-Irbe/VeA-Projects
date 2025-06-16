#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double kopeja_summa;
    int gimenes_pieauguso_sk[3], gimenes_bernu_sk[3];
    cout << "Input the total charge before tax ==> ";
    cin >> kopeja_summa;

    cout << "Input total amount of grown ups in the first family ==> ";
    cin >> gimenes_pieauguso_sk[0];
    cout << "Input total amount of grown ups in the second family ==> ";
    cin >> gimenes_pieauguso_sk[1];
    cout << "Input total amount of grown ups in the third family ==> ";
    cin >> gimenes_pieauguso_sk[2];

    cout << "Input total amount of children in the first family ==> ";
    cin >> gimenes_bernu_sk[0];
    cout << "Input total amount of children in the second family ==> ";
    cin >> gimenes_bernu_sk[1];
    cout << "Input total amount of children in the third family ==> ";
    cin >> gimenes_bernu_sk[2];

    double nodoklis = kopeja_summa * 0.095;
    double apkalposana = kopeja_summa * 0.10;
    double kopejaSummaArMaksam = kopeja_summa + nodoklis + apkalposana;

    cout << "Total amount to be paid (including tax and service): " << kopejaSummaArMaksam << " $" << endl;

    double kopejais_dalijums = 0.0;

    for (int i = 0; i < 3; i++) {
        kopejais_dalijums += gimenes_pieauguso_sk[i] * 1.0 + gimenes_bernu_sk[i] * 0.75;
    }

    for (int i = 0; i < 3; i++) {
        double gimenes_dal = (gimenes_pieauguso_sk[i] * 1.0 + gimenes_bernu_sk[i] * 0.75) / kopejais_dalijums;
        double gimenes_cena = gimenes_dal * kopejaSummaArMaksam;

        cout << "Family " << i + 1 << " pays: " << gimenes_cena << " $" << endl;
    }

    return 0;
}
