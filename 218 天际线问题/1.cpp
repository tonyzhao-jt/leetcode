class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<pair<int, int>> h; // store the skyline point
        multiset<int> m; // store the
        vector<vector<int>> res;

        // fetch data from the buldings
        for(const auto&b : buildings)
        {
            h.push_back({b[0], -b[2]});
            h.push_back({b[1], b[2]});
        }

        sort(h.begin(), h.end());
        int prev = 0, cur = 0;
        m.insert(0);

        for(auto i:h)
        {
            if(i.second < 0) m.insert(-i.second); // left point, add
            else m.erase(m.find(i.second)); // right point, out
            cur = *m.rbegin(); // get the highest current value
            if(cur != prev) // if not the same, skyline
            {
                res.push_back({i.first, cur});
                prev = cur;
            }
        }
        return res;
    }
};