class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        if(nums.size()==1){
            return 0;
        }
        int l=0;
        int r=nums.size()-1;
        while(l<=r){
            int mid=l+(r-l)/2;
            long long before=LLONG_MIN;
            long long after=LLONG_MIN;
            if(mid>0){
                before=nums[mid-1];
            }
            if(mid<nums.size()-1){
                after=nums[mid+1];
            }
            if((long long)nums[mid]>before && (long long)nums[mid]>after){
                return mid;
            } else if((long long)nums[mid]>before){
                l=mid+1;
            } else if((long long)nums[mid]>after){
                r=mid-1;
            } else {l=mid+1;}
        }
        return -1;
    }

    // while(l<=r){
    //     int mid=l+(r-l)/2;
    //     if(mid!=0 && nums[mid-1]>nums[mid]){
    //         l=mid+1;
    //     }
    // }
};