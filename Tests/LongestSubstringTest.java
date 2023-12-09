package Tests;

import LongestSubstring.Solution;
import org.junit.Assert;
import org.junit.Test;

public class LongestSubstringTest {

    @Test
    public void test1() {
        Assert.assertEquals(new Solution().lengthOfLongestSubstring("abcabcbb"), 3);
    }

    @Test
    public void test2() {
        Assert.assertEquals(new Solution().lengthOfLongestSubstring("bbbbb"), 1);
    }

    @Test
    public void test3() {
        Assert.assertEquals(new Solution().lengthOfLongestSubstring("pwwkew"), 1);
    }
}
