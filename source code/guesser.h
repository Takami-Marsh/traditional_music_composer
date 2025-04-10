#include <bits/stdc++.h>
#include "solver.h"
using namespace std;

vector<pair<string, string>> melody_interval_up(string pitch);
vector<pair<string, string>> melody_interval_down(string pitch);

// 旋律の次の高い音の候補を音程から(存在しない場合：配列から削除)
vector<pair<string, string>> melody_interval_up(string pitch)
{
  int loop_count = melody_intervals.size();
  vector<pair<string, string>> pitches;
  for (int i = 0; i < loop_count; i++)
  {
    string val = high_pitch_solver(pitch, melody_intervals[i]);
    if (val != "None")
    {
      pitches.push_back({melody_intervals[i], val});
    }
  }
  return pitches;
}

// 旋律の次の低い音の候補を音程から(存在しない場合：配列から削除)
vector<pair<string, string>> melody_interval_down(string pitch)
{
  int loop_count = melody_intervals.size();
  vector<pair<string, string>> pitches;
  for (int i = 0; i < loop_count; i++)
  {
    string val = low_pitch_solver(pitch, melody_intervals[i]);
    if (val != "None")
    {
      pitches.push_back({melody_intervals[i], val});
    };
  }
  return pitches;
}

// 旋律の候補から音の重なりで可能なものを列挙(存在しない場合：配列から削除)
vector<vector<string>> melody_and_pitch(vector<pair<string, string>> melodies, string pitch)
{
  vector<vector<string>> out;
  for (auto melody : melodies)
  {
    string val = interval_solver(pitch, melody.second);
    if (val != "D4" && val != "P4" && val != "A4" && val != "D5" && val != "D7" && val != "m7" && val != "M7" && val != "A7" && val != "D2" && val != "m2" && val != "M2" && val != "A2" && val != "Error")
    {
      out.push_back({val, melody.first, melody.second});
    }
  }
  return out;
}

// 一つの音から可能な組み合わせを全列挙
vector<vector<string>> guess_all(string pitch)
{
  vector<vector<string>> out;
  for (auto test_v : test)
  {
    // string val = interval_solver(pitch, test_v);
    // if (val != "D4" && val != "P4" && val != "A4" && val != "D5" && val != "D7" && val != "m7" && val != "M7" && val != "A7" && val != "D2" && val != "m2" && val != "M2" && val != "A2" && val != "Error")
    // {
    //   string tmp = test_v;
    //   tmp += "+";
    //   out.push_back({val, tmp});
    // }
    string val2 = interval_solver(test_v, pitch);
    if (val2 != "D4" && val2 != "P4" && val2 != "A4" && val2 != "D5" && val2 != "D7" && val2 != "m7" && val2 != "M7" && val2 != "A7" && val2 != "D2" && val2 != "m2" && val2 != "M2" && val2 != "A2" && val2 != "Error")
    {
      string tmp2 = test_v;
      // tmp2 += "-";
      out.push_back({val2, tmp2});
    }
  }
  return out;
}