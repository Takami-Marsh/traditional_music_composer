#include <bits/stdc++.h>
#include "./solver.h"
using namespace std;

int main()
{
  while (true)
  {
    string low, high;
    cout << "Low: ";
    cin >> low;
    cout << "High: ";
    cin >> high;
    cout << interval_solver(low, high) << endl << endl;
  }
}