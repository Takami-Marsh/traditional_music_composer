#include <bits/stdc++.h>
using namespace std;

const vector<string> piano{"#B/mC", "#C/bD", "mD", "#D/bE", "bF/mE", "#E/mF", "#F/bG", "mG", "#G/bA", "mA", "#A/bB", "bC/mB", "#B/mC"};
const vector<map<int, string>> intervals{
    {{
        {0, "P1"},
        {1, "A1"},
    }},
    {{
        {0, "D2"},
        {1, "m2"},
        {2, "M2"},
        {3, "A2"},
    }},
    {{
        {2, "D3"},
        {3, "m3"},
        {4, "M3"},
        {5, "A3"},
    }},
    {{
        {4, "D4"},
        {5, "P4"},
        {6, "A4"},
    }},
    {{
        {6, "D5"},
        {7, "P5"},
        {8, "A5"},
    }},
    {{
        {7, "D6"},
        {8, "m6"},
        {9, "M6"},
        {10, "A6"},
    }},
    {{
        {9, "D7"},
        {10, "m7"},
        {11, "M7"},
        {12, "A7"},
    }},
    {{
        {11, "D8"},
        {12, "P8"},
    }},
};
const vector<char> notes{'C', 'D', 'E', 'F', 'G', 'A', 'B'};
const vector<string> test{"#B", "mC", "#C", "bD", "mD", "#D", "bE", "bF", "mE", "#E", "mF", "#F", "bG", "mG", "#G", "bA", "mA", "#A", "bB", "bC", "mB", "#B", "mC"};
const vector<string> melody_intervals{"P1", "A1", "D2", "m2", "M2", "A2", "D3", "m3", "M3", "A3", "P4", "P5", "P8"};