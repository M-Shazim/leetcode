class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int flag=0;
        for(int i=0;i<nums.size();i++){
            for(int j=0;j<nums.size();j++){
                if(i<j){
                    if(nums[i]==nums[j]){
                        flag++;
                    }
                }
            }
        }
        return flag;
    }
};