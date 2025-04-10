#include <bits/stdc++.h>
#include "guesser.h"
using namespace std;

int main()
{
  while (true)
  {
    string pitch;
    vector<vector<string>> out;
    cout << "Pitch: ";
    cin >> pitch;
    out = guess_all(pitch);
    for (auto val : out)
    {
      cout << val[0] << " : " << val[1] << endl;
    }
    cout << endl;
  }
}
