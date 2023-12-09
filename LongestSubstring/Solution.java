package LongestSubstring;

import java.util.HashSet;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] a = int[6];
        a.length
        HashSet<Character> set = new HashSet<>();
        for (char c : s.toCharArray()){
            set.add(c);
        }

        int max = set.size();
        while(max > 1) {
            for (int i = 0; i < s.length() - max; i++){
                set = new HashSet<>();
                for (int j = i; j < i + max; j++){
                    set.add(s.charAt(j));
                }
                if (set.size() == max) {
                    return max;
                }
            }
            max--;
        }
        return max;
    }
}