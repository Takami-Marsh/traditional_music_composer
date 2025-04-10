#include <bits/stdc++.h>
#include "musical_values.h"
using namespace std;

string interval_solver(string low, string high);
string high_pitch_solver(string pitch, string interval);
string low_pitch_solver(string pitch, string interval);
pair<string, string> pitch_solver(string pitch, string interval);
int two_pitch_distance_solver(string low, string high);

// 二音の鍵盤上の位置
pair<int, int> two_pitch_position_solver(string low, string high)
{
  int loop_count = piano.size(), low_where, high_where, flag = 0;
  for (int i = 0; i < loop_count; i++)
  {
    // 同じ鍵盤に二つの音が存在する場合
    if (piano[i][0] == '#' || piano[i][0] == 'b')
    {
      if ((piano[i][0] == low[0] && piano[i][1] == low[1]) || (piano[i][3] == low[0] && piano[i][4] == low[1]))
      {
        low_where = i;
        flag++;
      }
      if ((piano[i][0] == high[0] && piano[i][1] == high[1]) || (piano[i][3] == high[0] && piano[i][4] == high[1]))
      {
        high_where = i;
        flag++;
      }
      // LowとHigh両方が見つかったときにbreak
      if (flag == 2)
      {
        break;
      }
    }
    // 一つの鍵盤に一つの音しかない場合
    else
    {
      if (piano[i][0] == low[0] && piano[i][1] == low[1])
      {
        low_where = i;
        flag++;
      }
      if (piano[i][0] == high[0] && piano[i][1] == high[1])
      {
        high_where = i;
        flag++;
      }
      // LowとHigh両方が見つかったときにbreak
      if (flag == 2)
      {
        break;
      }
    }
  }
  if (high_where < low_where)
  {
    return {low_where, high_where + loop_count - 1};
  }
  return {low_where, high_where};
}

// 二音間の距離
int two_pitch_distance_solver(string low, string high)
{
  int loop_count = notes.size(), low_where, high_where, flag = 0;
  for (int i = 0; i < loop_count; i++)
  {
    if (notes[i] == low[1])
    {
      low_where = i;
      flag++;
    }
    if (notes[i] == high[1])
    {
      high_where = i;
      flag++;
    }
    // LowとHigh両方が見つかったときにbreak
    if (flag == 2)
    {
      break;
    }
  }
  if (high_where < low_where)
  {
    return ((high_where + loop_count + 1) - low_where);
  }
  return (high_where - low_where) + 1;
}

// 二音間の音程(PADMA表がカバーしていない場合のエラー出力："Error")
string interval_solver(string low, string high)
{
  // 二音の位置, 距離
  pair<int, int> low_high = two_pitch_position_solver(low, high);
  int low_p = low_high.first, high_p = low_high.second, distance = two_pitch_distance_solver(low, high), distance_k;
  // 二音間の鍵盤距離
  distance_k = high_p - low_p;
  // 音程取得とエラー出力
  try
  {
    return intervals[distance - 1].at(distance_k);
  }
  catch (out_of_range &oor)
  {
    return "Error";
  }
}

// 低い音から特定の音程高い音(存在しない場合：None)
string high_pitch_solver(string low, string interval)
{
  int loop_count = test.size();
  for (int i = 0; i < loop_count; i++)
  {
    if (interval == interval_solver(low, test[i]))
    {
      return test[i];
      break;
    }
  }
  if (interval == "P8")
  {
    return "+" + low;
  }
  return "None";
}

// 高い音から特定の音程低い音(存在しない場合：None)
string low_pitch_solver(string high, string interval)
{
  int loop_count = test.size();
  for (int i = 0; i < loop_count; i++)
  {
    if (interval == interval_solver(test[i], high))
    {
      return test[i];
      break;
    }
  }
  if (interval == "P8")
  {
    return "-" + high;
  }
  return "None";
}

// 音から特定の音程高い/低い音(存在しない場合：None)
pair<string, string> pitch_solver(string pitch, string interval)
{
  return {low_pitch_solver(pitch, interval), high_pitch_solver(pitch, interval)};
}