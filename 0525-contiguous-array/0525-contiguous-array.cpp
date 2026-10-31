class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        vector<int> prefixSum;
        prefixSum.push_back(nums[0]==0 ? -1:1);
        for(int i=1;i<nums.size();i++){
            prefixSum.push_back(nums[i]==0 ? prefixSum[i-1]-1 : prefixSum[i-1]+1);
        }
        int ans=0;
        map<int, int> map;
        for(int i=0;i<prefixSum.size();i++){
            if(prefixSum[i]==0){
                    ans=max(ans, i+1);
                }
            else if(map.find(prefixSum[i])==map.end()){
                map[prefixSum[i]] = i;
            } else {
                int currLen=i-map[prefixSum[i]];;
                ans=max(ans, currLen);
            }
        }
        return ans;
    }
};