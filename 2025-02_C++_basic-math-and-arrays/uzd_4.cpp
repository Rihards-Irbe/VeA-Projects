#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main() {
    string product1, product2, product3;
    double price1, price2, price3;
    int quantity1, quantity2, quantity3;

    cout << "Enter the first product name, price, and quantity ==> ";
    cin >> product1 >> price1 >> quantity1;

    cout << "Enter the second product name, price, and quantity ==> ";
    cin >> product2 >> price2 >> quantity2;

    cout << "Enter the third product name, price, and quantity ==> ";
    cin >> product3 >> price3 >> quantity3;

    double total1 = price1 * quantity1;
    double total2 = price2 * quantity2;
    double total3 = price3 * quantity3;
    double totalAmount = total1 + total2 + total3;

    cout << "----------------------------------------------------------\n";
    cout << left << setw(20) << "Product"
         << right << setw(12) << "Price"
         << setw(12) << "Quantity"
         << setw(12) << "Total" << " |\n";
    cout << "----------------------------------------------------------\n";

    cout << left << setw(20) << product1
         << right << setw(12) << fixed << setprecision(2) << price1
         << setw(12) << quantity1
         << setw(12) << total1 << " |\n";

    cout << left << setw(20) << product2
         << right << setw(12) << fixed << setprecision(2) << price2
         << setw(12) << quantity2
         << setw(12) << total2 << " |\n";

    cout << left << setw(20) << product3
         << right << setw(12) << fixed << setprecision(2) << price3
         << setw(12) << quantity3
         << setw(12) << total3 << " |\n";

    cout << "----------------------------------------------------------\n";
    cout << left << setw(20) << "Total Amount:"
         << right << setw(36) << totalAmount << " |\n";
    cout << "----------------------------------------------------------\n";

    return 0;
}