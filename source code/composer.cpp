#include <bits/stdc++.h>
#include "guesser.h"
using namespace std;

int main()
{
  while (true)
  {
    string prev_melody, pitch, option;
    vector<pair<string, string>> out_m;
    vector<vector<string>> out;
    cout << "Previous melody: ";
    cin >> prev_melody;
    cout << "Pitch: ";
    cin >> pitch;
    cout << "Up or Down: ";
    cin >> option;
    if (option == "U")
    {
      out_m = melody_interval_up(prev_melody);
    }
    else
    {
      out_m = melody_interval_down(prev_melody);
    }
    out = melody_and_pitch(out_m, pitch);
    for (auto val : out)
    {
      cout << val[0] << " : " << val[1] << " = " << val[2] << endl;
    }
    cout << endl;
  }
}
